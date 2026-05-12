'''
#positional arguments
def add(a,b,):
    print(a+b)
bhadd(12,12)

n=int(input("Enter a number:"))
m=int(input("Enter a number:"))
add(n,m)

#default arguments
def greet(name="User"):
    print("Hello",name,"Welcome to Our App")
greet()
greet("Ajay")

#keyword arguments
def add(n,m):
    print("N:",n)
    print("M:",m)
add(m=10,n=20)

def details(name,course):
    print("Name   :",name)
    print("Course :",course)
details(name="Mounika",course="Python")

#variable length arguments
def marks(*m):
    s=0
    for i in m:
        s=s+i
    print(s)
marks(90,90,40,20,10)

def student(**l):
    for i in l:
        print(i+" : "+l[i])
student(name1="Viyash",name2="Vidyut",name3="Krishna")


#return type
#with return with parameter
def add(a,b):
    c=a+b
    return c
x = add(12,36)
print(x)


#without return without parameter
def add():
    a=10
    b=10
    print(a+b)
add()

#without return with parameter
def add(a,b):
    print(a+b)
add(58,69)

#with return without parameter
def add():
    a=10
    b=20
    return a+b
print(add())
'''
#recursion
def hi():
    print("hi")
    hi()
hi()

def login():
    u = input("Username :")
    p = int(input("Password :"))
    if u=="admin" and p==1234:
        print("Login Successful ✌")
    else:
        print("Invalid Username / Password")
        login()
login()

def add(a,b):
    print(a+b)
add(12,36)

#lambda function
output = lambda a,b:a+b
print(output(1,2))

#map function
def is_oddOrEven(a):
    if a%2!=0:
        return "Odd"
    else:
        return "Even"
l = [1,2,3,4,5,6,7,8,9,10]
z = list(map(is_oddOrEven,l))
print(z)

#filter function
def is_oddOrEven1(a):
    if a%2==0:
        return "Odd"
l = [1,2,3,4,5,6,7,8,9,10]
z = list(filter(is_oddOrEven1,l))
print(z)




