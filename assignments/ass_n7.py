#!/usr/bin/python

#Description and Pseudocode
#This script is meant to trim the description lines in a fasta file and return the file
#Pseudocode: I want to read in the odd lines and write a regex statement that captures the required info from these lines which contain the sequence description
#I also want to capture the complete sequence in the next line. (even lines in this case) 
#I will write the information to a new file for future use. 


import re #calls the module for the regex statements used later in the script

InFileName = "regex.practice1.fasta" #specifies target file in working directory
OutFileName = "regex.practice_output.fasta" #specifies file to write to. 
InFile = open(InFileName, 'r') #tells python that I'm going open the file and read it
OutFile = open(OutFileName, 'w') #tells python that I'm going to write the output of the script to the file named in OutFileName

count = 0 #initiates a counter so that I can count and target even and odd lines
for Line in InFile: #initiates a for loop in order to go through the file line by line
		count +=1 #adds one to the counter for every new line of the file
		if count % 2 != 0: #IF the value of the counter divided by two has a remainder greater than 0 (aka an odd numbered line), then...
			match = re.search(r'(>)(\d+\_\d+\:\S+)\s\{(.*?)}',Line) #matching statment from last week to match and capture only parts of the line name we want
			OutFile.write('>{}\n'.format(match.group(2))) #wites to outfile the fasta format carrot and the second matched group. The brackets and format function allow for no space in the write statement
		else:
			match2 = re.search(r'(\S+)', Line) #for even numbered lines print all non-whitespace which captures the protein sequence
			OutFile.write(match2.group(1)+'\n') #writes the captured sequence to the outfile

	
InFile.close() #close the read statement
OutFile.close() #close the write statement
