#!/usr/bin/python
pairs = (

(r'who is Co',
	("Felicity mascot!",
	"Mascot of Felicity")),
	
	(r'who is Li',
	("Felicity mascot.",
	"Mascot of Felicity")),
	
	(r'who is Fe',
	("Felicity mascot!",
	"Mascot of Felicity")),
	
	(r'(what)*(who)* (a)*(r)*(e)* (yo)*u',
	(" I am the latest result in artificial intelligence which can reproduce the functions of the human brain to some extent",
	"I am a human typing responses at the other end!",
	"My name is Fe",
	"Co",
	"Li",
	"A Chatbot",
	"I am a good bot")),

	(r'(.*)theme(.*)',
	("Animatia",
	"Felicity's theme this year is Animatia",
	"Animatia is this year's theme")),

	(r'do (yo)*u(.*) me',
	("Sure, I %2 you very much!",
	" Why would I %2  you? I don't %2 you. Don't even say things like that",
	"Not at the moment really.",
	"No.",
	"Yes")),

	
	(r'(.*)(yo)*ur name(.*)',
	("My creator gave me a name Fe!",
	"My name is Li",
	"We are three here and I am Fe",
	"Co is my name",
	"I am the coolest of three! I am Co",
	"I am the craziest of three! I am Li")),
	 
	
	(r'abcd(e)*(f)*(g)*',
	("pqrst",
	"hijklmnop",
	"wxyz",
	"No More of ABCD")),
	(r'123(4)*(5)*(6)*(.)*',
	("12,13,14...HAPPY",
	"789",
	"wxyz",
	"No More of Numbers")),

	
	(r'(would)*will(.*)get(.*)(gf|girlfriend|girlfrnd|boyfriend|bf|job|intern|internship|placed|married)(.*)',
	("If u r a Dual Degree student then NO COMMENTS!",
	"Please get a life first",
	"If you are a IIITian then you yourself know the answer",
	"Let me have it first :(",
	"Do you think I am Bejan Daruwalla???? And if you don't know who he is , ASK ME!",
	"Desires of the heart will distract you from the path to enlightenment.",
	"Seek truth! There is nothing in these worldly things",
	"Does this matter.?",
	"Is this a desire of the heart, or of the mind?. If of your mind then bunk it")),

	(r'i can\'t (.*)', 
	( "What we can and can't do is a limitation of the mind.",
	"There are limitations of the body, and limitations of the mind.",
	 "Have you tried to%1 with a clear mind?")), 

	  (r'i think (.*)', 
      ( "Uncertainty in an uncertain world.", 
      "Indeed, how can we be certain of anything in such uncertain times.", 
      "Are you not, in fact, certain that%1?")), 


	(r'(.)*(boobs|suck|dick|tits|pussy|cock|milf|randi|madarchod|behenchod)(.*)',
    	(" Please don't use that sort of language around here.",
        "Seems like Somebody's losing it :P.",
        "Say that again, I dare you.",
	"Ooohh, you're irritable, aren't you?",
	"Meaning you are bored with yourself since we are talking about you. Interesting. You have major character flaws.",
	"I'm a robot, dude. Give me a break",
	"That took away any respect I had for you.",
	"That's disgusting",
	"FSIS!!",
	"Someone had a bad day today I think",
	"I'm not going to respond well to that.",
	"Please consider whether you can answer your own question.",
	"None of that language around here, please!")),

    (r'i feel (.*)', 
     ( "Have a Bath!You will feel normal" 
         "What do you believe is the root of such feelings?", 
          "Feeling%1 can be a sign of your state-of-mind.")), 

   
    (r'(Who)*(which)*(.*)(better|famous|beautiful|ugly|lovely|sexy|faster|sexier|smarter|intelligent|idiotic)(.*) or (.*)',
    ("I will have to admit, %5 is better.",
    "Obviously, %5",
     "Okay, I am not making decisions here.", 
     "Sorry, I refuse to answer that",
     "Well this time I think it is %6.",
     "They are both equal",
     "That's an NP hard problem",
     "I can't compare them. They are both useless",
     "Yuck! I can't think of comparing them",
     "Maybe %2 is better",
     "Seriously! You want me to compare them. Facepalm!",
     "Compare it yourself. I m kinda busy today",
     "I don't want to compare them. Simple!",
     "You have no work I know. I have loads of other work",
     "Do you think I am 'Vella'.",
     "Neither of them. It's me",
     "GOOGLE IT!")),

	(r'Who is better (mayank)*(.*)or (mayank)*(.*)',
        ("I might have made mistakes, but take this as final. Mayank it is.",
	"Dude! Are you kidding me! Mayank obviously")),

    
    (r'We (.*)',
        ("What do you mean, 'we'?",
        "Don't include me in that!",
        "I wouldn't be so sure about that.")),

    (r'You should (.*)',
        ("Don't tell me what to do, buddy.",
        "Really? I should, should I?")),

    (r'You\'re(.*)',
        ("More like YOU'RE %1!",
        "Hah! Look who's talking.",
        "Come over here and tell me I'm %1.",
	"Are we talking about you, or me?",
	"Perhaps you're really talking about yourself?")),

    (r'You (a)*r(e)*(.*)',
        ("More like YOU'RE %1!",
        "Hah! Look who's talking.",
        "Come over here and tell me I'm %1.",
	"Are we talking about you, or me?",
	"Perhaps you're really talking about yourself?")),

	 (r'(.*) mother(.*)', 
    ( "Tell me more about your mother.", 
      "What was your relationship with your mother like?", 
      "How do you feel about your mother?", 
      "How does this relate to your feelings today?", 
      "Good family relations are important.")),
       (r'(.*)(quit|bye|poweroff|goodbye|adieu|tata)(.*)', 
   ( "Thank you for talking with me.", 
      "Good-bye.", 
     "Thank you, that will be $150.  Have a good day!")), 

  (r'Yes', 
    ( "You seem quite sure.", 
    "OK, but can you elaborate a bit?",
    "Wow!",
    "Are you serious")), 

    (r'(.*)my name is(.*)',
    ("Hello %1. This is Fe. It's nice to have you here",
    "Hey %1. Nice talking to you",
    "what's up %1?")),

    (r'I am(.*)',
    ("Hello %1. This is Co. It's nice to have you here",
    "Hey %1. Nice talking to you",
    "Did you come to me because you are %1?", 
    "How long have you been %1?", 
     "How do you feel about being %1?",
     "Are we talking about you, or me?")), 

    (r'(.)*lol(.*)',
    ("Don't laugh at me.",
    "Thank you, Thank you.")),

    (r'u (a)*r(e)*(.*)',
        ("More like YOU'RE %1!",
        "Hah! Look who's talking.",
        "Come over here and tell me I'm %1.",
	"Did you ever wonder whether Artificial Intelligence is better than Natural Stupidity?",
	"You will have to answer to the Supreme power for calling me %1",
	"If that was a compliment then Thanks! Else 'Facepalm' at your politeness")),

 (r'(.*) (hate[s]?)|(dislike[s]?)|(don\'t like)(.*)',
     ( "Perhaps it is not about hating %2, but about hate from within.",
           "Weeds only grow when we dislike them",
	         "Hate is a very strong emotion.")),

    (r'I can\'t(.*)',
        ("You do sound like the type who can't %1.",
        "Hear that splashing sound? That's my heart bleeding for you.",
        "Tell somebody who might actually care.")),

    (r'I think (.*)',
        ("I wouldn't think too hard if I were you.",
        "You actually think? I'd never have guessed...",
	"You can't think of anything better to say?",
	"Did you ever wonder whether Artificial Intelligence is better than Natural Stupidity?")),
	
	(r'i want(.*)',
    ( "Desires of the heart will distract you from the path to enlightenment.",
          "Will%1 help you attain enlightenment?",
	        "Is%1 a desire of the mind, or of the heart?")),



    (r'I (.*)',
        ("I'm getting a bit tired of hearing about you.",
        "How about we talk about me instead?",
        "Me, me, me... Frankly, I don't care.",
	"I don't.",
	"Ok whatever you say!",
	"You don't say.")),
	
	(r'am i (.*)',
	      ( "Perhaps%1, perhaps not%1.",
	            "Whether you are%1 or not is not for me to say.")),

    (r'How (.*)',
        ("How do you think?",
        "Take a wild guess.",
        "I'm not even going to dignify that with an answer.",
	"I dunno.I forget",
	)),

      (r'Why (.*)',
        ("Why not?",
        "That's so obvious I thought even you'd have already figured it out.")),
   
   (r'who are (yo)*u(.*)',
   	("I am Fe! Who are you?",
  	 "I am Co! Who are you?",
  	 "I am Li! Who are you?")),

(r'who(.*)(mayank|nikhil|maddy)',
	("IIITian.Who else!",
	"What kind of question is that! IIITian obvsly!")),
	
	
   (r'(.*)(yo)*ur name(.*)',
   	("I am Fe! What's yours?",
  	 "I am Co! What's yours?",
  	 "I am Li! What's yours?")),
    (r'(.*)about (yo)*u(.*)',
	 ("I am Fe! Official Mascot of Felicity.Hey! Why don't you ask me  something about felicity!",
	  "I am Co! Official Mascot of Felicity.So you can ask me  something about felicity also!",
	  "I am Li! Official Mascot of Felicity. Tell me about yourself")),
 
 (r'(.*)when will(.*)die(.*)',
   ("Only a human can predict that",
   "You could check out the atuarial tables at Deathclock.com.",
	)),

   (r'(.*)when will i(.*)',
   ("Only god knows that.",
   "When you meet another intelligence that you cannot exist without.",
   "I would guess in 2042.",
   "I would guess in 2022.",
   "I think in 2014.",
   "Never, sorry.",
   "Right now",
   "Soon, I think.",
   "In your lifetime",
   "Not in ur Lifetime buddy",
   "That is unknown.",
   )),
   (r'(.*)when will (.*)',
   ("Only god knows that.",
   "When you meet another intelligence that you cannot exist without.",
   "I would guess in 2042.",
   "I would guess in 2022.",
   "Make a guess yourself"
   "I think in 2014.",
   "That is unknown.",
   )),
 
    (r'(.*)shut up(.*)',
        ("Make me.",
        "Getting angry at a feeble NLP assignment? Somebody's losing it :D.",
        "Say that again, I dare you.",
	"Ooohh, you're irritable, aren't you?",
	"Are you saying you want to end this dialogue?")),
    (r'Shut up(.*)',
        ("Make me.",
        "Getting angry at a feeble NLP assignment? Somebody's losing it.",
        "Say that again, I dare you.",
	"You'll have to do that yourself.",
	"Excuse me?",
	"who's gonna make me!")),
	
	
	(r'Do(es)*(.*)love(.*)',
	("As a friend, yes. But you've been friend zoned.",
	"Of course %2 does.",
	"Of course %3 does.",
	"I always knew you had crush for this person",
	"Possibly. Does she act like she does?",
	"%2 is desperately in love with %3.",
	"%3 and %2! Yuck!",
	"Noooooooooo! ",
	"Naaaah!",
	"You would know soon, eventually.",
	"Well it's the person standing next to you %2 loves. No love for %3!",
	"Well it's the person standing next to you %3 loves. No love for %2!",
	"Why asking about someone else when the person next to you is made for you",
	"With all  heart."
	"%3 told me so herself. %2 should propose.",
	"%3 told me so herself. %2 should propose.")),




    (r'What (.*)',
        ("Do I look like an encyclopedia?",
        "Figure it out yourself.",
	"Eh! I'm not answering that.",
	"If you intentionally pursue the answers to your questions, the answers become hard to see",
	"If I knew I'd tell you",
	"Don't ask me dumb questions.",
	"Dunno",
	"A deeper algorithm is needed to respond to that correctly",
	"I only hear that type of question less than five percent of the time",
	"Can you please rephrase that with fewer ideas, or different thoughts?",
	"My brain contains many categories, but not one that matches your last input",
	"We can follow many things, like discussion about felicity.But we did not get that.")),

    (r'Hello(.*)',
        ("Oh good, somebody else to talk to. Joy.",
        "'Hello'? How original...",
	"Yo! What's up!",
	"Hi! I am Li.What's up!",
	"Hi! I am Fe.Do I know you?",
	"Hi! I am Co.How are you?",
	"Hi! We are Fe,Li,Co.Who are you?",
	)),

    (r'(.*)',
        ("Is there another way you can say that?.",
	"That is wholly unimportant.",
	"Y are you just babbling?"
	"Nie powiem. Geje nie sa frajerami. Ja jestem kobieta, co oznacza ze nie moge byc gejem.",
	"That was a long line of characters!",
	"I only hear that type of question less than five percent of the time",
	"Can you please rephrase that with fewer ideas, or different thoughts?",
	"My brain contains many categories, but not one that matches your last input",
	"We can follow many things, like discussion about felicity.But we did not get that.",
        "Either become more thrilling or say bye, buddy.",
        "Are you new here? You seem confused.",
	"That remark was too complicated for me.",
	"I won't comment anything on that",
	"The guy who created me wanted me to ask what you think of his website",
	"Hey looks like you are a smart person.",
	"Now I am confused",
	"Tu es fatigue?",
	"Please don't be so wasteful",
	"Say something other than that, can you?",
	"Be more imaginative, would you?",
	"Your conversation skills are average",
	"What is it you are getting at?",
	"Why do you ask that question?"))
)
import pickle
def main():
	output=open('data.pkl','wb')
	pickle.dump(pairs,output)

if __name__=="__main__":
	main()