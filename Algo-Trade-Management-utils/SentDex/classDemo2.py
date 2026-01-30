class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'
# test the class
x = MyClass()
print x

# complex class. self = 'this'
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
# test the class
x = Complex(3.0, -4.5)
print x.r
print x.i


# hello class
class Hello:
    #def __init__(self,msg):
    #    print msg
    def printfunction(self, msg):
        print msg
# x = Hello("hello")   #worked
x= Hello().printfunction("hello from function")


