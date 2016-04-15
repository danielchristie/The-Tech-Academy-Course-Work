
#Serialization (Pickling) Example
#Pickling is used to store python objects.
#Perform timely calculations, algorithms, or create a long dictionaries
#once and then store it to a variable (an object), and then pickle it.
#The pickle module, is a part of the standard library within Python


def main():
    #Import pickle to use it
    import pickle
    #Then we define an example dictionary, which is a Python object.
    example_dict = {1:"6",2:"2",3:"f"}

    #Open a file (note that we open to 'write bytes(wb)' in Python 3+)
    pickle_out = open("dict.pickle","wb")
    
    #Calls the Pickle module's function using two req paramaters, what
    #we are going to dump the date, (example_dict) and where to dump the
    #data,("pickle_out").
    pickle.dump(example_dict, pickle_out)
    
    #save dict.pickle file in the same directory as the script and then
    #close it.
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
    pickle_in = open("dict.pickle","rb")
    example_dict = pickle.load(pickle_in)

    #This shows the retained information from the dict data-type.
    print(example_dict)
    print(example_dict[3])

if __name__ == "__main__": main()
