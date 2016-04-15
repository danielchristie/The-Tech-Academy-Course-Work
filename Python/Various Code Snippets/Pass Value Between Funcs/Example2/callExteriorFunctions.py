from callFunctionsExample import checkforNumber

#This will call the function checkforExample() that is stored in another module file, hence the import
#This is an example of how to call a function from within another file and gain access to the stored variable
#for use within this program.

#So with the checkforExample(), we can get the user's number selection and check it for a valid input and
#convert it into a integer for further calculation within this program but without having to rewrite all of
#that functions coding. I can simply make that particular function modular and call to it whenever required. 

def main():  
    getDigit = checkforNumber() #Calling a function from another file that checks if user input is a digit
    print(getDigit)
    result = (7 + getDigit)
    print("7 + {} = ".format(result))

if __name__ == '__main__':
    main()
