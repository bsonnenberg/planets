#!/usr/bin/python

#This script takes an argument from the command line and turns all characters
#to lowercase, removes spaces, and counts the length of the string. 

string = input("Please enter string")
no_space = string.lower().replace(" ", "")
print (len(no_space))

