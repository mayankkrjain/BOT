import string
import re
import random
import pickle
import json
import urllib

pairs = ()
chat_files = open('Random_chat.pkl', 'rb')
pairs=pickle.load(chat_files)


offensive=['boobs','fuck','suck','dick','bitch','ass','tits','pussy','cock','milf']

reflections = {
  "am"     : "are",
  "was"    : "were",
  "i"      : "you",
  "i'd"    : "you would",
  "i've"   : "you have",
  "i'll"   : "you will",
  "my"     : "your",
  "are"    : "am",
  "you've" : "I have",
  "you'll" : "I will",
  "your"   : "my",
  "yours"  : "mine",
  "you"    : "me",
  "me"     : "you"
}
class Chat(object):
    def __init__(self, pairs,reflections={}):
        """
        Initialize the chatbot.  Pairs is a list of patterns and responses.  Each
        pattern is a regular expression matching the user's statement or question,
        e.g. r'I like (.*)'.  For each such pattern a list of possible responses
        is given, e.g. ['Why do you like %1', 'Did you ever dislike %1'].  Material
        which is matched by parenthesized sections of the patterns (e.g. .*) is mapped to
        the numbered positions in the responses, e.g. %1.

        :type pairs: list of tuple
        :param pairs: The patterns and responses
        :type reflections: dict
        :param reflections: A mapping between first and second person expressions
        :rtype: None
        """

        self._pairs = [(re.compile(x, re.IGNORECASE),y) for (x,y) in pairs]
        self._reflections = reflections

    # bug: only permits single word expressions to be mapped
    def _substitute(self, str):
        """
        Substitute words in the string, according to the specified reflections,
        e.g. "I'm" -> "you are"

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        words = ""
        for word in string.split(string.lower(str)):
            if word in self._reflections:
                word = self._reflections[word]
            words += ' ' + word
        return words

    def _wildcards(self, response, match):
        pos = string.find(response,'%')
        while pos >= 0:
            num = string.atoi(response[pos+1:pos+2])
            response = response[:pos] + \
                self._substitute(match.group(num)) + \
                response[pos+2:]
            pos = string.find(response,'%')
        return response
    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # check each pattern
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)    # pick a random response
                resp = self._wildcards(resp, match) # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp

    # Hold a conversation with a chatbot
    def converse(self, inp):
	    self.inp=inp
            if self.inp:
                response= self.respond(self.inp)
	    	if (('encyclopedia' in response) and (random.randint(1,2) % 2 == 0)):
			search=inp.split()
			search='+'.join(search)
			search='http://lmgtfy.com/?q='+search
			return search
		else:
			return response


rude_chatbot = Chat(pairs, reflections)
def rude_chat(input_line):
	url='http://api.duckduckgo.com/?q=' + str(input_line)+'&format=json&kp=-1&pretty=1'
	data=urllib.urlopen(url).read()
	if '<TITLE>ERROR: The requested URL could not be retrieved</TITLE>' not in data:
		text=json.loads(data)
		text=(str(text['Abstract'])+'\n'+str(text['AbstractURL']))
		if text:
			return text
	else:
		return rude_chatbot.converse(input_line)
