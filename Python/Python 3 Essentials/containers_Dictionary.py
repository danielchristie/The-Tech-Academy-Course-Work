#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    #Syntax to generate a dictionary
    d = dict(One = 1, Two = 2, Three = 3, Four = 4, Five = 5)

    #Reports the data type stored to d
    print(type(d))

    print('---------------------------------------')
    

    #Says for every key in dictionary named d, print the key
    for key in d: print(key)

    print('---------------------------------------')
    

    #Says for every item in dictionary, print the key and corrisponding values
    for key, value in d.items(): print(key,value)

    print('---------------------------------------')
    

    #Says for every item in dictionary, print the key and corrisponding values
    #but do so in an alphabetical order
    print(sorted(d))

    print('---------------------------------------')
    

    #Says serach for the key, "One" and report its corrisponding value
    print(d.get('One'))

    print('---------------------------------------')

    #but there could easily be an error if there is no key, "One" so
    #we can do the following to report ot the user that the item is not in the list
    print(d.get('Tne', 'Item not found.'))

    print('---------------------------------------')
    
    #Append new entries into the dictionary from another dictionary
    d2 = dict(Six = 6)
    d.update(d2)
    for key, value in d.items(): print(key,value)

    print('---------------------------------------')
    
    #Checks if key exits and then deletes an entry from the dictionary
    if 'Six' in d:
        del d['Six']
    for key, value in d.items(): print(key,value)

    print('---------------------------------------')

    #Replaces a value for the specified key
    d['One'] = 9
    for key, value in d.items(): print(key,value)

    print('---------------------------------------')

    #Updates a new entry into the dictionary
    d['Six'] = 6
    for key, value in d.items(): print(key,value)

    print('---------------------------------------')

    #Yields the length of the dictionary
    length = len(d)
    print(length)

    print('---------------------------------------')

    #Lists the keys, values, or both from the dictionary
    print(d.keys())
    print(d.values())
    print(d.items())

if __name__ == "__main__": main()
