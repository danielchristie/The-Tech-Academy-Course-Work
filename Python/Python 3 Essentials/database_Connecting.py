#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sqlite3

def main():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row #This reports as row objects and memory address
    db.execute('drop table if exists test') #So we create a new table each time
    db.execute('create table test (t1 text, i1 int)')#Create the table
    db.execute('insert into test (t1, i1) values (?, ?)', ('One', 1))#Add data
    db.execute('insert into test (t1, i1) values (?, ?)', ('Two', 2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('Three', 3))
    db.execute('insert into test (t1, i1) values (?, ?)', ('Four', 4))
    db.commit() #Always commit after any modification to the database

    #Defualt is the order it naturally appears but you can change it manually
    #('select i1, t1 from test order by t1')
    cursor = db.execute('select * from test order by i1')
    for row in cursor:
        #print(row)
        print(dict(row)) #Dictionary mode, there are different modes

    #Other ways to request a print out
    #print(row['t1'])
    #print(row['t1'], row['i1'])


if __name__ == "__main__": main()
