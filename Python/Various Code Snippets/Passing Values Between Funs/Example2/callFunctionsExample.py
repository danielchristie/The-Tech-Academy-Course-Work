
convertToDigit = None

#Anotomy of a function:
#----------------------------------------------------------
#Function's name is F
def f(x): #The parameter is (x)...the value to pass into this fuction
    return x * x * x

#will return the squre of any number placed into f(?)
y = f(2) #The argument that is being passed to the function is (2)
print(y)#y is simply the variable in which we are storing the function's return

#----------------------------------------------------------
#This function will calculate all numbers in a Fibonacci Series from 0 to input
def fib(input):
    a, b = 0, 1
    while a < input:
        print(a,)
        a, b = b, a + b

#----------------------------------------------------------
#This function will calculate if input is an even or odd number
def oddeven(input):
    leftover = input % 2
    if leftover == 0:
        print("\n{} is an even number.".format(input))
    else:
        print("\n{} is an odd number.".format(input))
#----------------------------------------------------------

#This function will check user's input for a number value until
#it receives a number it will instruct the user to enter a number

def checkforNumber():
    count = 0
    while count == 0:
        #as long as count is 0 it will persist
        numInput = input("\nPlease enter a number between 0 and 1000000 to be used later for this program: ")
        if numInput.isdigit(): #check user's input for a number
            count = 1 #When it sees a number, set count to 1 so the loop ends
        else:
            print("\nI am sorry, {} is not a number. Please enter a valid number. ".format(numInput))

    convertToDigit = int(numInput) #Input will be a string, so convert to integer

    #Now that it received a sucessful number and converted into Integer, we can return
    #that user's number to the function that called this function in the first place.          
    return convertToDigit 
#----------------------------------------------------------

def main():
    #This calls the checkforNumber function to get a number input from the user
    calculate = checkforNumber()
    exit = 0
    while exit == 0:
        print()
        print("|=================================================================|")
        print("|            Welcome to the Fibonacci Series number game!         |")
        print("|=================================================================|")
        print("| 1: Calculate the Fibonacci Series                               |")
        print("| 2: Found out if your number indicated is an odd or even number  |")
        print("| 3: Exit this program                                            |")
        print("|=================================================================|")
        menu = input("\nPlease make your selection: ")
        if menu == "1":
            #Pass the user's number input to the fib function
            fib(calculate)
            print("")
        elif menu == "2":
            #Pass the user's number input to the odd/even function
            oddeven(calculate)
        elif menu == "3":
            exit = 1
        else:
            print("\nThat is not a valid selection. Please make your selection from 1 through 3. ")
#---------------------------------------------------------

#This will only run main() if code is ran by this file. If functions are being called from
#outside of this file then it will only run the function being called not the entire program.
if __name__ == '__main__':
    main()







              
              
