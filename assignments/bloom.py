#!/usr/bin/python

#Description and Pseudocode
#This script opens a file, Bloom_etal_2018_Reduced_Dataset.csv, to be read.
#It loops through each line (skipping the header) and creates two dictionaries. 
#Both dictionaries will use species as their keys
#The first has the log_size as its value
#The second as the diadromus status as its value
#Then I will use a for loop to loop through the second directory 
#I will then loop through both dictionaries.
#The first will add up the total log body sizes and print out these results
# The second will count out the number of diadromous vs not and print

import re #calls the module for the regex used in line 24

InFileName = "Bloom_etal_2018_Reduced_Dataset.csv" #specifies target file in working directory
InFile = open(InFileName, 'r') #tells python that I'm going open the file and read it


size_dict = {} #creates the two dictionaries that I will abuse below
class_dict = {}
next(InFile) #skips the first line of the file, in this case the header row
for Line in InFile: #initiates a for loop in order to go through the file line by line
		match = re.search(r'(\S+)\,(\d\.\d+|\d)\,(\d+\.\d+)\,(diadromous|non-diadromous)', Line) # a matching statement that captures each row value for each organism
#	print(match.group(1)) #was here for testing

		size_dict[match.group(1)] = float(match.group(2)) #creates first dictionary. Keys are organism and values are log body sizes
		class_dict[match.group(1)] = match.group(4)	#creates second dictionary. Keys are organisms and values are whether or not they are diadromous or non

for key, value in class_dict.items(): #loops through and prints the second dictionary bc it's what JULIE wanted
	print (key, value)

x = 0
sum_ = 0 #establishes two emtpy variables for future addition
#for loop in order to go through each dictionary value. This loop adds each log body size to the last as it loops.
#I also calculated the average log body size for funsies. That's what x was for in order to count the number of times the loop was looped through for the later division
for key in size_dict:
	x += 1
	sum_ += size_dict[key] #calculates the overall log body size sum
av = sum_/x #calculates the average after the loop is over

diad = 0
nondiad = 0 #created two empty variables in order for counting!! 
for key, value in class_dict.items():  #for loop in order to loop through the second dictionary's keys
#	print(value)
	if( value == "diadromous"): #conditional that says if the key equals this than add one to this variable
		diad += 1
	else:
		nondiad += 1 # adds 1 to the nodiad variable if the first condition wasn't met

print('The total sum of the body sizes is', sum_,'\n','There were', nondiad, 'non-diadromous and', diad, 'diadromous organisms')
#prints out the rest of the requested information for the assignment
#First, prints out the sum of the body sizes then skips to a new line and prints the number of non and diadromous organisms in the file.


InFile.close()		


