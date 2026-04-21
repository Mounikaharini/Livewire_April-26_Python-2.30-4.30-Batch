'''
#write a python program to check whether the given number is +ve ,
#two digit number and should be the range between 2 to 100
n = int(input("Enter a number :"))
if n>0 and (n>=10 and n<=99)and(n>=2 and n<=100):
    print("Yes")
else:
    print("No")


#task 2

n = int(input("Enter a number :"))
if n%2==0 and (n>=10 and n<=99)and(n>=2 and n<=5000):
    print("Yes")
else:
    print("No")

#multiple of 9 and 10 , three digit
n = int(input("Enter a number :"))
if n%10==0 and n%9==0 and (n>=100 and n<=999):
    print("Yes")
else:
    print("No")
#1 2 3 4 5

for i in range(1,6,1):
    print(i,end=" ")


# 5 4 3 2 1

for i in range(5,0,-1):
    print(i,end=" ")


a = [1,2,3,4,5,6,7,8,9,10]
s=0
for i in a:
    s = s + i
print(s)


a = [1,2,3,4,5,6,7,8,9,10]
s=0
for i in a:
    if i%2==1:
        s = s + i
print(s)
'''
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
#& - & - &

'''
for i in range(0,5,1):
    print("*",end=" ")

for i in range(1,6,1):
    if i%2!=0:
        print("&",end=" ")
    else:
        print("-",end=" ")

for j in range(0,5,1):

    for i in range(0,5,1):
        print("*",end=" ")
    print()

'''
for j in range(1,6,1):
    for i in range(1,6,1):
        if i%2!=0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()

for j in range(1,6,1):
    for i in range(1,6,1):
        if i%2!=0 or j%2!=0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()

for j in range(1,6,1):
    for i in range(1,6,1):
        if i==3 or j==3:
            print(1,end=" ")
        else:
            print(" ",end=" ")
    print()

