#NotSoTrivial.py
# A trivia game that asks multiple choice questions and tells the user if they are right or wrong.
#It will have five questions. 


#Welcome screen
print "\n Welcome to some random trivia! :) "
 

#Section 1. The first questions

print "\n 1. In what county is the city of Costa Mesa located in?"
print "a)Los Angeles b)Orange c)San Diego d)Santa Barbara"
answer=raw_input ("\n Your answer: ") #Asks the user for their response and save it as answer

if answer=="b":  #Checks to see if answer is correct. If it is, say that's correct! If it isn't, say so.
	print "You are a smart cookie!"
else:
	print "Nope.Nice try but Costa Mesa is located in Orange County."

#Section 2. The second question

print "\n 2. When is Mexico's Independence day?"
print "a) 5 de Mayo b) September 15 c)September 16 d) November 1"
answer = raw_input ("\n Your answer: ") 

if answer== "c":
	print "Great Job!"
else:
	print "Womp. It is on September 16th when Mexico claimed it's independence from Spain."

#Section 3. The third question
print "\n 3. How many regions are in the state of Oaxaca in Mexico?"
print "a)4 b)5 c)6 d)7"
answer = raw_input ("n\Your answer:")

if answer==  "d":
	print "Yay, not many peopel know that so I am proud of you!"
else: 
	print "Close there are actually 6 regions."








