#!/usr/bin/python

#Create a hash for the female and male
#hash of arrays with each day being an array
#conditional statement that only counts if the previous line's seconds and minutes are certain difference.

import re
import sys
import os
import datetime

#InFileName = "*.TXT"
#OutFileName = "practice.txt"

directory = './'

for filename in os.listdir(directory):
	if filename.endswith(".txt"):
		match = re.search(r'GPRRDATA_(\d{2}\-\dH)\_([\d\w]{10})\_(M)\_([\d\w]{10})\_(F).txt', filename)
		male = (match.group(2))
		#print(male)
		female = (match.group(4))
		#print(female, male)
		f = open(filename)
		next(f)
		male_li = dict()
		female_li = dict()
		for lines in f:	
			match1 = re.search(r'([\d\w]{10})\s(\d{2}\/\d{2}\/\d{2})\s(\d{2}\:\d{2}\:\d{2})', lines)
			if match1.group(1) == male:
				male_li.setdefault(match1.group(2), []).append(match1.group(3))
			if match1.group(1) == female:
				female_li.setdefault(match1.group(2), []).append(match1.group(3))
		count1 = 0
		
		for yep in male_li:
			count1 += 1
			count2 = 0	
			for yepyep in male_li[yep].items():
				count2 += 1
				
				print(yepyep)
			
		#print(female_li.items())