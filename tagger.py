## Author: InfoBot Team
## This program returns POS tagged line for a given input line. It uses the dafault nltk tagger.
## One can use Brill tagger instead,but learning will take a lot of time.
import nltk
from collections import defaultdict
##Model is used for forcing the tagger to tag elements in entity_list as NN.
def train_tagger(entity_list):
	model={}
	model=defaultdict(lambda:'NN',model)      
	for element in  entity_list:
		model[element]='NN'
	model['seo']='NN'
	model['pro']='NN'
	return model	
	    
def tagit(line,model):
        default_tagger = nltk.data.load(nltk.tag._POS_TAGGER)
	new_tagger = nltk.tag.UnigramTagger(model=model, backoff=default_tagger)
	tokens =line.split() 
#	tagged=default_tagger.tag(tokens)   
	tagged=new_tagger.tag(tokens)	
	return tagged

