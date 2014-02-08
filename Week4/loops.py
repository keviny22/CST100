#!/usr/bin/env python
#
# Student:    Kevin S. Young
# Assignment: Homework Week 4
# Instructor: Robert Rucker
# Due Date:   Feb 9, 2014


# Part I
###########################
# 1)
for j in range(10):
    for i in range(10):
        print(i, end = " ")
    print()

print()    

for j in range(10):
    for i in range(10):
        print(j, end = " ")
    print()
print()

###########################
# 2)
for j in range(1,11):
    for i in range(j):
        print(i, end = " ")
    print()
print()

###########################
# 3)
for j in reversed(range(1,11)):
    for k in range(abs(j-10)):
        print('  ', end = '')
        
    for i in range(j):
        print(i, end = " ")
    print()

print()

###########################
## 4)
n = 9
for j in range(1,10):
    for i in range(j):
        n += 1
        print(n, end = " ")
    print()
print()