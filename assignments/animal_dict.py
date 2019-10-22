#!/usr/bin/python

#This script creates a dictionary in which the keys are animals
#and the values are the animal sizes

#prints out the keys to the dictionary
# uses a conditional to print out:
# "big" for animals over 20 g 
#& "small" for the animals under 20 g

#creates empty dictionary
animal_dict = {}
#populates dictionary with 6 key/value pairs
animal_dict['GiantAfricanLandSnail'] = 20
animal_dict['GardenSnail'] = 1
animal_dict['RomanSnail'] = 3
animal_dict['Abalone'] = 5
animal_dict['CommonPeriwinkle'] = 1
animal_dict['HUGESnail'] = 31
#prints out a list of keys found in the dictionary
print (animal_dict.keys())

#for loop interates through each key/value pair
for key, value in animal_dict.items():
#if value is equal to or greater than 20 print 
#the corresponding key and "BIG"
	if (value >= 20):
		print (f"{animal_dict[key]} BIG")
#if the value is less than 20 print the 
#corresponding key and "SMALL"
	else:
		print (f"{animal_dict[key]} SMALL")
