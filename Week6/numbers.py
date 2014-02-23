#!/usr/bin/env python
#
# Student:    Kevin S. Young
# Assignment: Homework Week 6
# Instructor: Robert Rucker
# Due Date:   Feb 21, 2014
# Desc:       Part II

def allNumAvg(numList):#takes a list of numbers and returns the average of all the numbers in the list.
    return sum(numList) / len(numList) #find the avearge of the list by adding the list and dividing by number of items
     
def posNumAvg(numList): #takes a list of numbers and returns the average of all the numbers in the list that are greater than zero.
    result = [] # a list of stuff we want
    for num in numList: # loop through list passed to function
        if num > 0: #if element is gretar then 0
            result.append(num) # add item to the list of stuff we like
    
    return sum(result) / len(result) # return the average (mean) of the list
    
    
def nonPosAvg(numList): #takes a list of numbers and returns the average of all the numbers in the list that are less than or equal to zero.
    result = [] # a list of stuff we want
    for num in numList: # loop through list passed to function
        if num  < 1: #if element is less then 1
            result.append(num) # add item to the list of stuff we like
    
    return sum(result) / len(result) # return the average (mean) of the list

#main
number_list = list() #create an empty number_list to add input to
while True:
    num = int(input("Enter a number (-9999 to end):")) #ask for input, convert to integer
    if num == -9999: #exit while loop prompting for input when user enters -9999
        break #break out of the while loop to end user input
    
    number_list.append(num) # append the loop with the input

print("The list of all numbers entered is:") #print some words
print(number_list) #print the list 'number_list'
print("The dictonary with average is:") #print some words

# create a dictonary with results of calling said functions
dictonary = {
    "AvgPositive" : posNumAvg(number_list),
    "AvgNonPos"   : nonPosAvg(number_list),
    "AvgAllNum"   : allNumAvg(number_list),
}
print(dictonary) #print the dictonary