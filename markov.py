from __future__ import print_function
import random
import sys
# -*- coding: utf-8 -*-


"""
How to use from command line:

[path]>python markov.py [Number of words in output] [Input text file 1] ...  [Input text file n]

The output will be written to a text file named "[Input text file 1]_output.txt"

"""

INPUT_TEXT_FILES = sys.argv[2:]
table = {}
w1 = ""
w2 = ""

#Generate table from sample input text
for i in range(len(INPUT_TEXT_FILES)):
	with open(INPUT_TEXT_FILES[i], "r") as ins:
		for line in ins:
			for word in line.split():
				word = word.lower()
				table.setdefault( (w1,w2), [] ).append(word)
				w1,w2 = w2,word
	ins.close()


#Use table to print out a random piece of text
MAX_WORDS = int(sys.argv[1])
max_lines = int (MAX_WORDS/20) # 20 is the arbitrary number of words per line
w1 = ""
w2 = ""
output_file = INPUT_TEXT_FILES[0][:-4]+"_output.txt"

with open(output_file, 'a') as out:
	print("\n\n", file=out)
	for j in range(max_lines):
		newLine = ""
		for i in range(20):
			word = random.choice( table[ (w1,w2) ] )
			newLine += " %s"%(word)			
			w1,w2 = w2,word
		print(newLine)
		print(newLine, file=out)
		
out.close()