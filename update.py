#!/usr/bin/python
import json
import json_parser as jp
from collections import defaultdict
fp=open('Data_json','r').read()
data=json.loads(fp)
logical=data['logical']
my_dict={}
my_dict=defaultdict(lambda:[],my_dict)
(entity_list,domain_list,synonym_list)=jp.get_list_attributes(data)
for each_key in entity_list:
	for key in domain_list:
		if key in logical[each_key].keys():
			my_dict[key].extend(logical[each_key][key]['tagset'])
for each_key in entity_list:
	for key in domain_list:
		if key in logical[each_key].keys():
			logical[each_key][key]['tagset']=','.join(list(set(my_dict[key])))
fp1=open('Updated','w')			
fp1.write(json.dumps(data, sort_keys=True, indent=9))
	
