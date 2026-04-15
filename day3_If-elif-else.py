'''
#multiple of both 5 and 3
x = 25
if x%5==0 and x%3==0:
    print("yes")
else:
    print("no")


#vowel or not
ch = str(input("Enter a character :"))

vowels = ['a','e','i','o','u']

if ch>='a' and ch<='z':
    
    if ch in vowels:
        print("It is a vowel")
        
    else:
        print("It is a consonant")
        
else:
    print("It is not a alphabet")

#check the given input is a number / alphabet / space / symbol

ch = str(input("Enter a single character :"))
if ch>='0' and ch<='9':
    print("It is a number")
elif (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
    print("It is a Alphabet")
elif ch==' ':
    print("It is a space")
else:
    print("It is a symbol")

#laptop discount

price = int(input("Enter the price :"))
print("Price of the laptop:",price)
if price<=50000:
    print("No Discount")
    print("Total Price of the laptop:",price)
elif price>=50001 and price<=100000:
    d = (price//100)*10
    print("Discount Price :",d)
    print("Total Price of the laptop:",price-d)
elif price>=100001 and price<=150000:
    d = (price//100)*15
    print("Discount Price :",d)
    print("Total Price of the laptop:",price-d)
elif price>=150001:
    d = (price//100)*20
    print("Discount Price :",d)
    print("Total Price of the laptop:",price-d)
else:
    print("Invalid Input")
'''
a=int(input("Enter a number"))
if a<0:
    print("Negative")
elif a>0:
    print("Positive")
elif a==0:
    print("zero")
else:
    print("invalid")

