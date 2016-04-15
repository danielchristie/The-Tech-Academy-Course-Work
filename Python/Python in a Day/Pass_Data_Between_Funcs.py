#Serialization (Pickling) Example
#Pickling is used to store python objects.
#Perform timely calculations, algorithms, or create a long dictionaries
#once and then store it to a variable (an object), and then pickle it.
#The pickle module, is a part of the standard library within Python

def main():
    #Import pickle to use it
    import pickle
    #Then we define an example dictionary, which is a Python object.
    example_calc = (4 * 2)

    #Open a file (note that we open to 'write bytes(wb)' in Python 3+)
    pickle_out = open("addNum.pickle","wb")
    
    #Calls the Pickle module's function using two req paramaters, what
    #we are going to dump the date, (example_dict) and where to dump the
    #data,("pickle_out").
    pickle.dump(example_calc, pickle_out)
    
    #save dict.pickle file and then close it.
    pickle_out.close()

    #Call another function to show that the dict was successfully
    #passed from this function into another function.
    anotherFunc()

def anotherFunc():
    #Import pickle to use it once again.
    import pickle
    
    #Open the pickle file.
    #Use pickle.load() to get the stored dict and load into the
    #variable, example_dict so it can be used in this function.
    pickle_in = open("addNum.pickle","rb") #read bytes(rb)
    example_calc = pickle.load(pickle_in)

    #This shows the retained information from the dict data-type.
    print(int(example_calc))
    print(example_calc + 2)
    print('Stored int value 8 from different function + 2. Should get: 10')

if __name__ == "__main__": main()
