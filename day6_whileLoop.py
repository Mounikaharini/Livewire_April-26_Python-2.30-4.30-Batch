'''
for i in range(0,8,1):
    for j in range(0,7,1):
        if i==0 and j==3:
            print("*",end=" ")
        elif (i==1 and j==2)or(i==1 and j==4):
            print("*",end=" ")
        elif (i==2 and j==1)or(i==2 and j==5):
            print("*",end=" ")
        elif (i==3 and j==0)or(i==3 and j==6):
            print("*",end=" ")
        elif i==4:
            print("*",end=" ")
        elif (i==5 and j==0)or(i==5 and j==6):
            print("*",end=" ")
        elif (i==6 and j==0)or(i==6 and j==6):
            print("*",end=" ")
        elif (i==7 and j==0)or(i==7 and j==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(0,8,1):
    for j in range(0,7,1):
        if i==0 or i==7 or j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(0,7,1):
    for j in range(0,7,1):
        if (i==j) or i+j==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(0,7,1):
    for j in range(0,7,1):
        if (i==j) or i+j==6:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


#1 to 10
i=1
while i<=10:
    print(i,end=" ")
    i=i+1

i=2
while i<=10:
    print(i,end=" ")
    i+=2

i=10
while i>=1:
    print(i,end=" ")
    i-=1

i=10
while i>=1:
    print(i,end=" ")
    i-=2

# * * * * *
i=1
while i<=5:
    print("*",end=" ")
    i+=1

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

i=1
while i<=5:
    j = 1
    while j<=5:
        print("*",end=" ")
        j+=1
    print()
    i+=1
'''
#sum of digits
n=123654789
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print(s)


#count the digits
n=123654789
c=0
while n>0:
    n=n//10
    c=c+1
print(c)
