class tutorials:
    name = "sm9 class"
    difficulty = "easy"
    def yourname(self,yname):
        self.yname = yname
    def hello(self):
        print "Hello ", self.yname, " !!!"

# test class and objects
print tutorials.name

object1 = tutorials
print object1.name

object1.name = "Hey here!"
print object1.name

###function call######

obj1 = tutorials()  # called construtor
obj1.yourname("james")
 

obj2 = tutorials()
obj2.yourname("smith")
 

print obj1.hello()
print obj2.hello()
