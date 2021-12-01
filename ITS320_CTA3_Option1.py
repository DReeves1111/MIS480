#----------------------------------------------------------------------------------------------------------------------
#Program Name: ITS320_CTA3_Option1-------------------------------------------------------------------------------------
#Author: David Reeves--------------------------------------------------------------------------------------------------
#Date: January 3, 2021-------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#Pseudocode:
# 1) Create a program that reads in a year and outputs the approximate value of a Ferrari 250 GTO for that year
# 2) Using if and elif statements create a price range estimate for how much a Ferrari 250 GTO cost for that year
# 3) Use relational operators to assign a price range to certain year models of the Ferrari 250 GTO
# 4) Enter the year of your choice and the program will produce an estimated value of the Ferrari 250 for that year
#----------------------------------------------------------------------------------------------------------------------
#Program Inputs: A table containing the estimated value of Ferrari GTOs from 1962 to 2014
#Program Inputs: Enter a year of your choice into the program to determine the estimated value of the GTO for that year
#Program Outputs: An estimated price of the Ferrari 250 GTO for the year that you put into the program
#----------------------------------------------------------------------------------------------------------------------


year = int(input('Enter year:\n'))

if year < 1962:
    print('Car had not been made yet.')
elif year <= 1964:
    print('$', 18500)
elif year <= 1968:
    print('$', 6000)
elif year <= 1971:
    print('$', 12000)
elif year <= 1975:
    print('$', 48000)
elif year <= 1980:
    print('$', 200000)
elif year <= 1985:
    print('$', 650000)
elif year <= 2012:
    print('$', 35000000)
elif year <= 2014:
    print('$', 52000000)
elif year > 2014:
    print('Please enter a year before 2015.')


