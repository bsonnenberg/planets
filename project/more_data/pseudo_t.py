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
		male_li = []
		female_li = [] 
		visit = 0
		for lines in f:	
			#print(lines)	
			match1 = re.search(r'([\d\w]{10})\s(\d{2}\/\d{2}\/\d{2}\s\d{2}\:\d{2}\:\d{2})', lines)
			if match1.group(1) == male:
				male_li.append(match1.group(2))
			if match1.group(1) == female:
				female_li.append(match1.group(2))
		#print(female_list)	
		
		male_list = iter(male_li)
		female_list = iter(female_li)
		try:
			for a in male_list:
				#print(a)
				male_match = re.search(r'(\d{2})\/(\d{2})\/(\d{2})\s(\d{2})\:(\d{2})\:(\d{2})', a)
				month1 = int((male_match.group(1)))
				day1 = int((male_match.group(2)))
				year1 = int((male_match.group(3)))
				timeH1 = int((male_match.group(4)))
				timeM1 = int((male_match.group(5)))
				timeS1 = int((male_match.group(6)))
				feed = datetime.datetime(year1, month1, day1, timeH1, timeM1, timeS1)
				#print(feed)
				next_male = next(male_list)
				male_match2 = re.search(r'(\d{2})\/(\d{2})\/(\d{2})\s(\d{2})\:(\d{2})\:(\d{2})', next_male)
				month2 = int((male_match2.group(1)))
				day2 = int((male_match2.group(2)))
				year2 = int((male_match2.group(3)))
				timeH2 = int((male_match2.group(4)))
				timeM2 = int((male_match2.group(5)))
				timeS2 = int((male_match2.group(6)))
				feed2 = datetime.datetime(year2, month2, day2, timeH2, timeM2, timeS2)
				delta = feed2 - feed
				#print(delta) 
				yep = delta.total_seconds()
				if yep > 10:
					print('MALE VISIT', yep/60)
				elif yep < 10:
					yep2 = 0
					while yep2 < 10:
						next_next = next(male_list)
						option = re.search(r'(\d{2})\/(\d{2})\/(\d{2})\s(\d{2})\:(\d{2})\:(\d{2})', next_next)
						month3 = int((option.group(1)))
						day3 = int((option.group(2)))
						year3 = int((option.group(3)))
						timeH3 = int((option.group(4)))
						timeM3 = int((option.group(5)))
						timeS3 = int((option.group(6)))
						feed3 = datetime.datetime(year3, month3, day3, timeH3, timeM3, timeS3)
						delta2 = feed3 - feed
						yep2 = delta2.total_seconds()
					else: 
						print('MALE VISIT', yep2/60)

		except StopIteration:
			pass				
########################### FEMALE VISIT LOOP ###########################################			
			
		try:
			for b in female_list:
				#print(a)
				female_match = re.search(r'(\d{2})\/(\d{2})\/(\d{2})\s(\d{2})\:(\d{2})\:(\d{2})', b)
				month1f = int((female_match.group(1)))
				day1f = int((female_match.group(2)))
				year1f = int((female_match.group(3)))
				timeH1f = int((female_match.group(4)))
				timeM1f = int((female_match.group(5)))
				timeS1f = int((female_match.group(6)))
				feed_f = datetime.datetime(year1f, month1f, day1f, timeH1f, timeM1f, timeS1f)
				#print(feed)
				next_female = next(female_list)
				female_match2 = re.search(r'(\d{2})\/(\d{2})\/(\d{2})\s(\d{2})\:(\d{2})\:(\d{2})', next_female)
				month2f = int((female_match2.group(1)))
				day2f = int((female_match2.group(2)))
				year2f = int((female_match2.group(3)))
				timeH2f = int((female_match2.group(4)))
				timeM2f = int((female_match2.group(5)))
				timeS2f = int((female_match2.group(6)))
				feed2_f = datetime.datetime(year2f, month2f, day2f, timeH2f, timeM2f, timeS2f)
				delta_f = feed2_f - feed_f
				#print(delta) 
				yeep = delta_f.total_seconds()
				if yeep > 15:
					print('FEMALE VISIT', yeep/60)
				elif yeep < 15:
					yep2_f = 0
					while yep2_f < 15:
						next_next_f = next(female_list)
						option_f = re.search(r'(\d{2})\/(\d{2})\/(\d{2})\s(\d{2})\:(\d{2})\:(\d{2})', next_next_f)
						month3f = int((option_f.group(1)))
						day3f = int((option_f.group(2)))
						year3f = int((option_f.group(3)))
						timeH3f = int((option_f.group(4)))
						timeM3f = int((option_f.group(5)))
						timeS3f = int((option_f.group(6)))
						feed3f = datetime.datetime(year3f, month3f, day3f, timeH3f, timeM3f, timeS3f)
						delta2f = feed3f - feed_f
						yep2_f = delta2f.total_seconds()
					else: 
						print('FEMALE VISIT', yep2_f/60)
		
		except StopIteration:
			pass



		     

		continue
	else:
		continue 
