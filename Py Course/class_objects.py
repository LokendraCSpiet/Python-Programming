class MyClass:
    variable = "blah"

    def function(self,arg1):
        print(arg1)
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjectx.function("hii")



#The __init__() function, is a special function that is called when the class is being initiated.
class NumberHolder:

   def __init__(self, number):
       self.lnumber = number

   def returnNumber(self):
        return self.lnumber
var = NumberHolder(7)  
print(var.returnNumber()) #Prints '7'


