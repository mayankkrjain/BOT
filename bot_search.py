#!/usr/bin/python
from fuzzywuzzy import fuzz
from collections import defaultdict
from copy import deepcopy
import random
def recursive_match(dict_instance,root,depth,line,key,match,depth_list,answer,meta_data_match):
		if type(dict_instance) is dict:
			for items in dict_instance.keys():
				if str(items) == 'meta': 
					dict_instance[str(items)]=dict_instance[str(items)].split(',')
					for each_elem in dict_instance[str(items)]:
						if fuzz.partial_ratio(each_elem,line) > 88:
							depth+=1
							if str(key) in match.keys():
								if 'command' in dict_instance.keys():
									ans="<b><i> "+key.item()+" </i></b> : "+dict_instance['command']
									meta_data_match[ans]=1
									match[root]=1
							depth_list[str(root)]=depth
				else:
				 	if str(items) in match.keys():
						depth+=1
						if str(key) in match.keys():
			       				if type(dict_instance[items]) is dict:
						 		if 'command' in dict_instance[items].keys():
									answer[dict_instance[items]['command']]=1
						depth_list[str(items)]=depth
					recursive_match(dict_instance[items],items,depth,line,key,match,depth_list,answer,meta_data_match)
def match_attributes(data,line,entity_list,domain_list,syn_list,default_list):
	match={}
	answer={}
	default_answer={}
	depth_list={}
	depth_list=defaultdict(lambda:1,depth_list)
	meta_data_match={}
	default_list=[]
	match_meta={}
	match_meta=defaultdict(lambda:0,match_meta)
	CC_Meta={}
	CC_Meta=defaultdict(lambda:0,CC_Meta)
	final_meta_data=defaultdict(list)
	find_CC_meta=defaultdict(list)
	final_CC_Meta=defaultdict(list)
	depth=0
	Meta_list=[]
	logical=data['logical']   ##In the given database structure Logical contains the Fest related entities
###############################			Match with tag-set  		######################################	
	for key in syn_list.keys():
		if  fuzz.partial_ratio(key,line) > 88 and len(key)-2 <=len(line):
			if syn_list[key] in logical.keys():
				match[str(syn_list[key])]=1
				depth_list[syn_list[key]]=0  
			else:	
			 	match[str(syn_list[key])]=1
				depth_list[syn_list[key]]=1
###############################			Match with meta-data            ######################################
	for key in logical:
		if type(logical[key]) is dict:
			if 'meta' in logical[key].keys():
				temp=logical[key]['meta'].split(',')
				for each_elem in temp:
					if fuzz.partial_ratio(each_elem,line) > 88 and len(each_elem)-2 <=len(line):
						match_meta[str(key)]+=1
						find_CC_meta[str(each_elem)].append(str(key))
##############################			Updating the Matchlist with meta_match 	#######################					
	flag=0
	for k,v in match_meta.iteritems():
		final_meta_data[v].append(k)
	if len(match_meta.keys()) >0:
		Meta_list=final_meta_data[max(final_meta_data.keys())]
		for each_elem in Meta_list:
			depth_list[str(each_elem)]=0
			match[str(each_elem)]=1
############################			Other category of Meta-Data joind with Conjuction CC ###########################################
	find_cc_meta=deepcopy(find_CC_meta)
	for key in find_cc_meta:
		for key2 in find_CC_meta:
			if len(set(find_cc_meta[key]) & set(find_CC_meta[key2])) ==0:
				CC_Meta[key]+=1
				CC_Meta[key2]+=1
	for k,v in CC_Meta.iteritems():
		final_CC_Meta[v].append(k)
	if len(CC_Meta.keys()) >0:
		Meta_list=final_CC_Meta[max(final_CC_Meta.keys())]
		random.shuffle(Meta_list)
		counter=0
		for each_elem in Meta_list:
			depth_list[str(each_elem)]=0
			match[str(each_elem)]=2
			counter+=1
			if counter ==2:
				break
################################	 Root is present or Not            #################################################
	for key in match.keys():
		#if key in 
		if depth_list[key]==0:
			flag=1
			break
##################################	Making felicity as default root    #########################################
	if flag ==0 and len(match) > 0:
		if len(default_list) == 0:
		   default_list.append('')
		for key in default_list:
			if key in logical:
				depth_list[key]=0
			match[key]=1
################################	Looking for command data 	######################################################		
	for key in logical:	
	    	depth=0
		if key in match.keys() :
			if 'command' in logical[key].keys():
				default_answer[default_key]=key.title()
			for item in logical[key].keys():
				if str(item)=='meta' or str(item) =='command' or str(item)=='tagset':
					continue
				elif str(item) in match.keys():
					depth+=1
					depth_list[str(item)]=depth
					if str(key) in match.keys():
						if 'command' in logical[key][item].keys():
							ans=logical[key][item]['command']
						        answer[ans]=key.title()
					recursive_match(logical[key][str(item)],item,depth,line,key,match,depth_list,answer,meta_data_match)	
	
	(value,root)=return_answer(logical,depth_list,answer)
############### Limiting the number of elements randomly 	#######################################		
	if value:
		new_key=deepcopy(default_answer.keys())
		random.shuffle(new_key)
		for key in new_key:
			if len(default_answer.keys()) < 5:
				break
			else:
				if key in default_answer.keys():
					del default_answer[key]
		new_answer=deepcopy(default_answer.keys())
		random.shuffle(new_answer)
		if len(default_answer.keys())>2:
			for key in new_answer[1:]:
				if default_answer[key].lower() in Meta_list:
					default_answer[str(default_answer[key])]=1
					if key in default_answer.keys():
						del default_answer[key]
		return (str(' <br /> '.join(set(default_answer.keys()))),root)
	else:
		new_key=deepcopy(default_answer.keys())
		random.shuffle(new_key)
		for key in new_key:
			if len(answer.keys()) < 5:
				break
			else:
				if key in answer.keys():
					del answer[key]
		new_answer=deepcopy(answer)
		if len(answer.keys())>2:
			for key in new_answer.keys()[1:]:
				if new_answer[key].lower() in Meta_list:
					answer["<a href='index?question=what is " +str(answer[key]) +" ?'> " +str(answer[key])+ "</a>"]=1
					answer[answer[key]]=1
					if key in answer.keys():
						del answer[key]
						
		return (str(' <br /> '.join(set(answer.keys()))),root) 
def return_answer(logical,match,answer):
#This function checks if a root node is present or not. This helps to 	
	new_match=sorted(match.items(), key=lambda x: x[1])
	root=[]
	non_root=[]
	for item in new_match:
		if item[1]==0:
			root.append(item[0])
		else:
			non_root.append(item[0])
	if len(non_root)==0:
		return (True,root)
	else:	 
		if len(answer.keys())==0:
	  		return (True,root)
	  	return (False,root)

			

