#Creating a more sophisticated user directory

user_directory_dict = { 'MICHAEL ADAMS' : ['123@gmail.com', 1],
                        'TOMMY JARVIS' : ['456@gmail.com', 2],
                        'BILL KARNOV' : ['789@gmail.com', 3],
                        'REBECCA ANDERSON' : ['101112@gmail.com', 4],
                        }
def searchDirectory(personsInfo):         

    try:

        #checks to see if the typed in name exists in the directory
        #if the name is not present, yield a message indicating such.
        personsInfo = user_directory_dict[fullName]
        firstName = raw_input('Please type in your FIRST name: ').upper()
        lastName = raw_input('Please type in your LAST name: ').upper()
        fullName = firstName + ' ' + lastName
        print 'Name: ' + fullName
        print 'Email: ' + personsInfo[0]
        print 'Phone: ' + str(personsInfo[1])

    except:

        #If there are no instances of the name, then this code will process
        print 'I am sorry, the name you have typed does not appear in the list.'

        
newSearch = True
while newSearch == True:
    #User indicated their desire to search again
    firstName = raw_input('Please type in your FIRST name: ').upper()
    lastName = raw_input('Please type in your LAST name: ').upper()
    fullName = firstName + ' ' + lastName
    searchDirectory(personsInfo)
    newSearch = False
