class adding:

    def get_values(self):
        self.x = input("input x ")
        self.y = input("input y ")
        self.z = input("input z ")
    
    def use_values(self):
        print(self.x + self.y + self.z)
    
dave = adding()     #Assigned the class name to the variable dave
dave.get_values()   #Called a function in dave
dave.use_values()   #Called a second function in dave
