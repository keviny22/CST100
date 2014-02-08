#!/usr/bin/env python
#
# Student:    Kevin S. Young
# Assignment: Homework Week 4
# Instructor: Robert Rucker
# Due Date:   Feb 9, 2014

# Part II - Decoding a secret message

def encrypt(word,key):
    mylist = []
    for i in (list(word)):
        mylist.append(encrypt_char(i,key))
        
    return mylist

def encrypt_char(character,key):
    character = ord(character)
    if (character + key > 126):
        enc_char = ((character + key) - 127) + 32
    else:
        enc_char = (character + key)
        
    return chr(enc_char)

def decrypt(word,key):
    mylist = []
    for i in (list(word)):
        mylist.append(decrypt_char(i,key))
        
    return mylist

def decrypt_char(character,key):
    character = ord(character)
    if (character - key < 32):
        dec_char = ((character - key) + 127) - 32
    else:
        dec_char = (character - key)
        
    return chr(dec_char)
    
    
enc_input = input("Enter a regular message to encode:\n")
enc_key   = int(input("Enter a key value (between 1 and 100) for encoding:\n"))

for i in  encrypt(enc_input,enc_key):
    print(i, end = '')
print()

dec_input = input("Enter an encrypted message to decode:\n")

print("The following are the decoded messages for keys 1 to 100:")
for j in range(1,101):
    print('Key: ' + str(j) + ' -> Decoded Message: ', end='')
    for i in decrypt(dec_input,j):
        print(i, end = '')
    print()

