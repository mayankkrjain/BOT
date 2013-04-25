##Author: InfoBot Team
##This program acts as a central command for this Infobot projects
#!/usr/bin/python
import tagger		##This imports code snippets of tagger.py
import quest_parse as qp	##quest_parse.py
import json
import json_parser as jp
import bot_search as bs
from fuzzywuzzy import fuzz
def main():
	print "Fe Li & Co invites you to Felicity 2013 :)\nFeel free to ask any Question to us\n"
	root=[]
	while True:
		fp=open('Data_json','r').read()
		data=json.loads(fp)
		(entity_list,domain_list,synonym_list)=jp.get_list_attributes(data)
		model=tagger.train_tagger(entity_list)
		line=raw_input('Question:\n')
		line=line.strip(' \n')
		line.lower()
		line.replace("'s",' ')
		tagged_line=tagger.tagit(line,model)
		(ans,root)=qp.chat_bot(tagged_line,entity_list,domain_list,synonym_list,data,root,line)
		print ans

if __name__=="__main__":
	main()
