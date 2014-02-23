#!/usr/bin/env python
#
# Student:    Kevin S. Young
# Assignment: Homework Week 6
# Instructor: Robert Rucker
# Due Date:   Feb 21, 2014
# Desc:       Part I (4 points), Write a function find_longest_word(wordList) 

# A function to find the longest word in a sentance
# accepts a list of strings, returns the first word with the most characters
def find_longest_word(wordList):
  print("The list of words entered is:")
  print(wordList.split()) # print the list of words
  print(max(wordList.split(), key=len)) # find first word with the most characters

    
find_longest_word(input("Enter a few words and I will find the longest:\n")) #ask the user for input, call function with input
