'''
order = input("Enter the pen Brand ('Flair' / 'XO') :")
quantity = int(input("Enter the quantity (In numbers): "))
cost = 10*quantity

#F-String
print(f"""✏ Praveen Stationary ✒
-----------------------
Your Order    = {order}
No.Of.Pens    = {quantity}
Amount to Pay = Rs.{10*quantity}
-----------------------
Thank You For Coming !!
-----------------------
""")


#String Format Function

print("""✏ Praveen Stationary ✒
-----------------------
Your Order    = {}
No.Of.Pens    = {}
Amount to Pay = Rs.{}
-----------------------
Thank You For Coming !!
-----------------------
""".format(order,quantity,cost))

print("""✏ Praveen Stationary ✒
-----------------------
Your Order    = {1}
No.Of.Pens    = {0}
Amount to Pay = Rs.{2}
-----------------------
Thank You For Coming !!
-----------------------
""".format(quantity,order,cost))

print("""✏ Praveen Stationary ✒
-----------------------
Your Order    = {o}
No.Of.Pens    = {q}
Amount to Pay = Rs.{c}
-----------------------
Thank You For Coming !!
-----------------------
""".format(q=quantity,o=order,c=cost))


#percentage
print("""✏ Praveen Stationary ✒
-----------------------
Your Order    = %s
No.Of.Pens    = %d
Amount to Pay = Rs.%d
-----------------------
Thank You For Coming !!
-----------------------
"""%(order,quantity,cost))

#list
a = [1,2,3,4,5]

a.append(11)
print(a)
a.extend([12,12])
print(a)
a.insert(0,36)
print(a)


a.remove(5)
print(a)
a.pop()
print(a)
a.pop(0)
print(a)

a[4]=5
print(a)

#a.clear()
#print(a)

print(a.index(1))
print(a.count(5))
a.reverse()
print(a)
a.sort()
print(a)
print(min(a))
print(max(a))
print(len(a))
print(sum(a))
print(sorted(a))
print(list((1,2,3)))

x = [1,4,2,6,2,4,2,3,4,4]
s=0
for i in x:
    if i%2==0:
        s=s+i
print(s)

'''
x = [1,4,2,6,2,4,2,3,4,4]
s = []
for i in x:
    if not(i in s):
       s.append(i)
print(s)
