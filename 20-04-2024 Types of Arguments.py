def ajith(wish):
    print(wish,"is a Good Boy")
ajith("ajith")


# Cube of a Number

# def cubing (number):
#     print("the Cubing of a",number,"is",number*number*number)
# cubing(4)
# cubing(5)
# cubing(8)

# def add(x,y):
#     return x+y 
# a=add(30,20)
# print("the addition is",a)


# def calculate(e,r):
#     sum=e+r 
#     sub=e-r 
#     mul=e*r 
#     return sum,sub,mul 
# x,y,z = calculate(3,4) 
# print("The Results are",x)
# print("The Results are",y)
# print("The Results are",z)

# Types of Arguments:
# Positional Arguments

def suntract(a,b):
    print(a-b)
suntract(20,10)



# Keyword Arguments

def ajith(name,age):
    print("hii",name,"your age is",age)
ajith(name="ajith",age=21)
ajith(age=56,name="saran")



# Default Arguments => Providing the Default Value in the Positional Arguments.

def welcome(name="ajith"):
    print("hii",name)
welcome("king")
welcome()



# Variable ;ength Arguments...

def suming(*a):
    b=0 
    for i in a:
        b=b+i 
    return b
print(suming(4,6,7,8,2,0))
