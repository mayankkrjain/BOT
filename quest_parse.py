##Author: Team infoBot
## This program takes input a POS tagged line and returns a clause which is then used for searching for best answer. In case no such match is found, it invokes the random talk function.
##Entity ==> 'Felicity' Domain ==> 'Time'

#!/usr/bin/python
import string
import bot_search as bs
import wordnet
import random_talk  as rt
def chat_bot(tag_line,entity_list,domain_list,syn_list,data,root,line):
        #This assumes that there is no trailing spaces and other similar characters(\t,\n,'s etc.). The line should have been in lowercase before it was tagged. 
	clause=[]  #Basic query clause
	entities=[] #List of matching entities
	flag=0
	for words in tag_line:
		word_list=[]
		if('.' in words[1]):
			continue
		if((words[0] == 'is') or (words[0] =='are') or (words[0]=='be')):
			continue
		if(words[1][0]=='W'):
			clause.append(words[0])
		if (('N' in words[1]) or ('PP' == words[1])):
			flag=1			#Everything followed by a Noun/Pronoun is included in clause.So flag is set to 1
		if(('JJ' in words[1]) or ('VB' in words[1]) or (flag == 1) or ('IN' == words[1])):
			if('VBG' in words[1]):
				stem_words=[]#wordnet.find_stem(words[0],'v')   #Stemming the verbs: began,begining ==> begin
				clause.append(words[0])
			else:
				clause.append(words[0])
	clause=' '.join(clause)			
	if len(clause) !=0:
		(answer,root)=bs.match_attributes(data,clause,entity_list,domain_list,syn_list)
		if len(answer) ==0 :
		  	return (rt.rude_chat(line),root)
		return (answer,root)
        else:
		return (rt.rude_chat(line),root)
