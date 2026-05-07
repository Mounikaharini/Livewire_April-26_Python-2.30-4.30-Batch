'''
#tuple
a = (1,2,3,4,5)

a.clear()
print(a)

print(a.index(1))
print(a.count(5))
print(min(a))
print(max(a))
print(len(a))
print(sum(a))
print(sorted(a))
print(tuple([1,2,3]))

s = ("viyash","vidyut","gokulakshmi","ajay","sabari","shri krishna")
s1,s2,s3,s4,s5,s6=s
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

#set

s={1,4,5,6,2,3,"hi",1.9,"bye"}
print(s)

s={1,2,3,4,5}
print(s)
s.add(6)
print(s)
s.update([7,8,9,10])
print(s)
s.remove(10)
print(s)
s.pop()
print(s)

s1={1,2,3,4,5}
s2={2,3,4,6,10}
print(s1.union(s2))
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)

print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
s1.clear()
s2.clear()

s1={1,2,3}
s2={4,5,6}
print(s1.isdisjoint(s2))

x={1,2,3,4,5,6,7,8,9,10}
y={5,6,2}
print(x.issuperset(y))
print(y.issubset(x))

#dictionary
d = {1:"watch",2:"iphone",3:"duster",4:"note",5:"laptop"}
print(d)

print(d[5])
print(d.get(1))

d[6]="cap"
print(d)

d.update({7:"spectacles"})
print(d)

d[1]="andriod"
print(d)

d.pop(2)
print(d)

print(d.keys())
print(d.values())
print(d.items())

for i in d:
    print(i," : ",d[i])

for i in d.items():
    print(i)
'''
#selection control - gokulakshmi
#for loop + jumping control - sabari
#while loop + jumping control - ajay
#string - viyash
#list - vidyut

#functions

def demo():
    a=20
    b=30
    print(a+b)
demo()

