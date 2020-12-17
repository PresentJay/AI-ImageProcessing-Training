# 밑바닥 딥러닝 chap1 ~
# InjeUniversity - 김상균교수님
# Arrangements by 정현재

""" Python Default  """
# please check your indentation each lines.

# calculating & printing
print(1-2)
print(4*5)
print(7/5)
print(3**2)  # square

# data structure
print(type(10)) # integer type
print(type(2.718)) # float type
print(type('hello')) # string type
print(type('h')) # string type(no character type even if it was just a character)

# variable
x=10  # assignment
print(x)
x=100
print(x)
y=3.14
print(x*y, type(x*y)) # autonomous type transition (integer multiply float -> float)

# array
a=[1,2,3,4,5]  
print(len(a), a[0], a[4])  # len is length of array & the method of call entity in array -> <array name>[0 ~ n-1]
a[4] = 99  # new assignment to existing array entity
print(a)  # show full array
print(a[0:2]) # show a certain range of array (start : end), but it shows start entity to end-1 entity.
print(a[1:])  # if you remain some range value empty, it goes to last entity to maximum or minimum entity by direction.
print(a[:3])  # so it works as 0~3 entity.
print(a[:-1])  # call minus entity means from "maximum (N)", so it works as print ("0 ~ (N-1)")
print(a[:-2])  # <minus 2 -> 0 to N-2 entity>

# dictionary
me = {'height' : 180}  # dictionary contain sets of name and value (in this case, 'height' is name, 180 is value)
print(me['height'])  # you can call dictionary entity as ->  <dictionary name>['<name>']
me['weight'] = 70   # also, you can assign more name & value like this.
print(me)
print(me['weight'])
me['score'] = [90, 90, 50, 80]  # name and value must be one by one structure. but you can make value multi-value. like this(array type)
print(me['score'])

# boolean
hungry = True
sleepy = False
print(type(hungry), not hungry)  # not calculates opposite from original
print(hungry and sleepy)  # and calculates true just when all condition are true (or it returns false)
print(hungry or sleepy) # or calculates true when one or more condition are true
                        # In the same way, it calculates false just when all condition are false (or it returns true)

# condition process  (when after "if" condition satisfy true, the below "if" line can work)
if not hungry:
    print("I'm hungry")
elif not sleepy:   # "elif" condition is for not satisfy "if" condition but additionally can be classified.
    print("but I'm sleepy")
else:  # "else" condition works for all of not satisfying situation.
    print("I'm Not hungry")
    
    
# iteration process
for i in [1,2,3]:  # for must have iterator(in this case, "i"), and iterator's range
    print(i)
    

# function assign & call process
# function means a designed work includes multi-line-able from <input value> to <return value>
def hello(object):  # inside () is the space for <input value>
    return "hello {}!".format(object)  # format is make {} inside in string to some variable value

print(hello("cat"))  # this line prints the string getting from hello function with "cat" input value.add()

# input value can be called as "parameter"


# class assign process & usage
# class is oriented from OOP paradigm (Object-Oriented Programming)
class Man:
    def __init__(self, name, age=0):  # __init__ is create process. it works when you assign this class to a instance
        self.name = name  # As add to above, self is default input value, and if you need to more input value (like "name"), using like this.
        self.age = age
        print("initialzed with ", end="")
        if not age:  # it condition means as (if age == 0) because if age is 0, not is 1. 1 is same with True. so it can run.
            print(name)
        else:
            print(name, ",", str(age) + "!")  # age is integer type variable. but other variable is string type variable.
            # so those different type values can't be assembled. but if you change variable type temporarily, it can be like this.
        
        
    def set_age(self, age):
        self.age = age   # you can add more member-variable to existing class. or add it to __init__ function.
    
    def hello(self):   # it is "member function" of this class(Man). it works just in Man instance.
        print("hello", self.name + "!")
        
    def goodbye(self):
        print("Good-bye", self.name + "!")
        
    def sayYourAge(self):
        print("I'm {} years old".format(self.age))
        
# class usage (like user-maid variable type as "int" in system)
m = Man("David")  # m can be called "instance" (same as object, but we call "instance" in this class)
m.hello()  # call the Man instance's member function.
m.goodbye()

m2 = Man("Minsu")
m2.hello()
m2.goodbye()
m2.set_age(3)
m2.sayYourAge()

m3 = Man("Sungil", 2)
m3.sayYourAge()

class Book:
    # initilize(create process) function with 3 input value(parameter)
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
        print("initialized!")
    
    def print_book(self):
        print("name: {}, author: {}, price: {}").format(self.name, self.author, self.price)
        
b1 = Book("밑바닥부터 시작하는 딥러닝", "사이토", 24000)
b2 = Book("컴퓨터 비전", "오일석", 35000)

b1.print_book()
b2.print_book()