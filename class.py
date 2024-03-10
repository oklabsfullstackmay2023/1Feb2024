#1. class defination
clas; MyClass():
    #1. property/variable
    x=10
    y=50
    #2. constructor/esp.function
    def __init__(self):
        pass
    #3. function/method
    def myFunction(self,x,y):
        return x+y


#2. create class external object
ceo1=MyClass()
print(ceo1.myFunction(10,50)) 
