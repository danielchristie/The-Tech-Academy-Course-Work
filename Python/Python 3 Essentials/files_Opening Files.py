#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC



def main():
    #opens file and places content into variable FH
    #When just filename is specified the second argument of mode is
    #defaulted to readonly.
    #Possible modes are write, read, read + write, append,
    #read binary, write binary (for image files)
    #Read = open('lines.txt', 'r')
    #Read and Write open('lines.txt', 'r+')
    #Write = open('lines.txt', 'w')
    #Append = open('lines.txt', 'a')
    #Read Binary = open('image.jpg', 'rb')
    #Write Binary = open('image.jpg', 'wb')
    
    fh = open('lines.txt') #fh is the file handle object that iterable
    for line in fh.readlines(): #In iteration mode, it can report one line at a time
        print(line, end='')

    #To copy lines.txt and save it as a new file
    infile = open('lines.txt', 'r')
    outfile = open('lines2.txt', 'w')
    for line in infile: 
        print(line, file = outfile, end='')
    print('\n--------------------------')
    print('File has been copied to a new file.')
    print('--------------------------')
    
    #To create a empty new file
    outfile = open('lines3.txt', 'w')
    print(file = outfile, end='')
    print('New file has been created.')

    #To copy an image file we will need to set a buffer
    #since the file may be very large. To copy a file you are
    #essentially placing original content in a buffer and then
    #copying contents from that buffer to the new file.
    #Images files require binary instead of txt.
    buffersize = 50000
    infile = open('boat2.png', 'rb')
    outfile = open('new.png', 'wb')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        buffer = infile.read(buffersize)
        print('--------------------------')
        print('New file has been created.')

if __name__ == "__main__": main()
