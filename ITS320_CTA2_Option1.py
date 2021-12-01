#---------------------------------------------------------------------------------------------------------------------------------------
# ITS320_CTA2_Option1.py
# David Reeves
# December 20, 2020
#---------------------------------------------------------------------------------------------------------------------------------------
# Pseudocode:
# 1) User inputs a string of less than 50 characters.
# 2) Run validation methods on string using str.isalnum, str.isalpha, str.isdigit, str.islower, and str.isupper
# 3) These validation methods help to identify characteristics of the contents of the string
#---------------------------------------------------------------------------------------------------------------------------------------
# Program Inputs: A string of alphabetic characters, alphanumeric characters, and numbers
# Program Outputs: Results of the string validation methods that display true or false pertaining to the results of each validation test
#---------------------------------------------------------------------------------------------------------------------------------------
import sys

user_value = input("Enter a string of less than 50 characters:")
if len(user_value) > 49:
    print ("Error! String must be less than 50 characters!")
    sys.exit()
    
    
    
if user_value.isalnum():
    print("True")
else:
    print("False")

if user_value.isalpha():
    print("True")
else:
    print("False")

if user_value.isdigit():
    print("True")
else:
    print("False")

if user_value.islower():
    print("True")
else:
    print("False")

if user_value.isupper():
    print("True")
else:
    print("False")
    

