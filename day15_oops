#FUNCTION OVERLOADING
'''
class calc:
    def add(a=0,b=0,c=0,d=0,e=0):
        print(a+b+c+d+e)

c = calc
c.add()
c.add(1)
c.add(1,1)   
c.add(1,1,1)
c.add(1,1,1,1)
c.add(1,1,1,1,1)

#OPERATOR OVERLOADING

a = 10
b = 10
print(a+b)

c="hello"
d=" world"
print(c+d)

e="11"
f="12"
print(e+f)
'''
#FUNCTION OVERRIDING

class plane:
    def __init__(self):
        print("""
======================================
               PLANE
======================================
""")
    def takeoff(self):
        print("Plane take off at CBE")
    def planeCarry(self):
        print("Plane should carry something")
    def height(self):
        print("Plane should fly in a average height")
    def land(self):
        print("Plane land at SALEM")

class cargoPlane(plane):
    def __init__(self):
        print("""
======================================
             CARGO PLANE
======================================
""")
    def takeoff(self):
        print("cargoPlane take off at BLR")
    def planeCarry(self):
        print("cargoPlane should carry Goods")
    def height(self):
        print("cargoPlane should fly in a low height")
    def land(self):
        print("cargoPlane land at SALEM")

class passengerPlane(plane):
    def __init__(self):
        print("""
======================================
          PASSENGER PLANE
======================================
""")
    def takeoff(self):
        print("passengerPlane take off at BLR")
    def planeCarry(self):
        print("passengerPlane should carry passengers")
    def height(self):
        print("passengerPlane should fly in a mid height")
    def land(self):
        print("passengerPlane land at SALEM")

class fighterPlane(plane):
    def __init__(self):
        print("""
======================================
            FIGHTER PLANE
======================================
""")
    def takeoff(self):
        print("fighterPlane take off at Kashmir")
    def planeCarry(self):
        print("fighterPlane should carry Weapons")
    def height(self):
        print("fighterPlane should fly in a upper height")
    def land(self):
        print("fighterPlane land at Lahore")

p = plane()
p.takeoff()
p.planeCarry()
p.height()
p.land()

cp = cargoPlane()
cp.takeoff()
cp.planeCarry()
cp.height()
cp.land()

pp = passengerPlane()
pp.takeoff()
pp.planeCarry()
pp.height()
pp.land()

fp = fighterPlane()
fp.takeoff()
fp.planeCarry()
fp.height()
fp.land()


  
