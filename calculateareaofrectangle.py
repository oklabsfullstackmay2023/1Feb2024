#1. class defination
class MyClass():
    #1. property/variable
    l=7
    h=6
    #2. constrcutor/esp.function
    def __init__(self):
        pass
    #3. function/method
    def myFunction(self,l,h):
        return l*h
        pass


#2. create class external object 
ceo1=MyClass()
print(ceo1.myFunction(7,6))
