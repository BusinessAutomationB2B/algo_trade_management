class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print(self)
    
  def sayHello(self):
      print("My name is %s, and age is %s" % (self.name, self.age))


if __name__ == "__main__":
    p1 = Person("John", 36)
    print(__name__)
    print(p1.name)
    print(p1.age)
    p1.sayHello()