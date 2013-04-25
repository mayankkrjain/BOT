#!/usr/bin/python
import nltk
from nltk.corpus import wordnet as wn	
def find_stem(word,pos):
	new_word= wn.morphy(word,pos)
	return new_word

