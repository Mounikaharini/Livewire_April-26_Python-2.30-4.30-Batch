def greet():
    print("🍧 The Frozen Scoop 🍨")
def menu():
    menulist = {1:"Cone Ice",2:"Cup Ice",3:"Kulfi",4:"Cassata",5:"Stick Ice"}
    for i in menulist:
        print(i,".",menulist[i])
    ch = int(input("Enter the choice (1/2/3/4/5):"))
    if ch==1:
        coneIce()
    elif ch==2:
        cupIce()
    elif ch==3:
        kulfi()
    elif ch==4:
        kasata()
    elif ch==5:
        stickIce()
    else:
        print("Currently Not Available")
        menu()
def coneIce():
    print("Cone Ice Categories")
    flavours = {1:{"name":"Chocolate","price":80},
                2:{"name":"Vanilla","price":100},
                3:{"name":"Strawberry","price":60},
                4:{"name":"Butter Scotch","price":120}}
    for i in flavours:
        print(i,".",flavours[i]["name"],"- Rs.",flavours[i]["price"])
    fch = int(input("Enter the choice (1/2/3/4):"))
    q = int(input("Enter the quantity (In Numbers):"))
    bill(flavours,fch,q)
    
def bill(flavours,ch,q):
    print()
    item = flavours[ch]["name"]
    price = flavours[ch]["price"]
    quantity = q
    x = input("If You Want any Toppings (Yes / No):" )
    if x.lower()=="yes":
        toppinsPrice = 30
    else:
        toppinsPrice = 0
        
    bill=f"""  🍧 The Frozen Scoop 🍨
--------------------------
Item     :{item}
Quantity :{quantity}
Price    :Rs.{price}
Extra    :Toppins
Price    :Rs.{toppinsPrice * quantity}
--------------------------
Amount to pay :Rs.{(quantity*price) + (toppinsPrice * quantity)}
--------------------------
Thank you for visiting ✌✌️
"""
    print(bill)
    import pywhatkit as p
    p.sendwhatmsg_instantly("+919384542020",bill)
def cupIce():
    print("Cup Ice Categories")
    flavours = {1:{"name":"Chocolate","price":80},
                2:{"name":"Vanilla","price":100},
                3:{"name":"Strawberry","price":60},
                4:{"name":"Butter Scotch","price":120}}
    for i in flavours:
        print(i,".",flavours[i]["name"],"- Rs.",flavours[i]["price"])
    fch = int(input("Enter the choice (1/2/3/4):"))
    q = int(input("Enter the quantity (In Numbers):"))
    bill(flavours,fch,q)
def kulfi():
    print("Kulfi Categories")
    flavours = {1:{"name":"Chocolate","price":80},
                2:{"name":"Vanilla","price":100},
                3:{"name":"Strawberry","price":60},
                4:{"name":"Butter Scotch","price":120}}
    for i in flavours:
        print(i,".",flavours[i]["name"],"- Rs.",flavours[i]["price"])
    fch = int(input("Enter the choice (1/2/3/4):"))
    q = int(input("Enter the quantity (In Numbers):"))
    bill(flavours,fch,q)
def kasata():
    print("Kasata Categories")
    flavours = {1:{"name":"Chocolate","price":80},
                2:{"name":"Vanilla","price":100},
                3:{"name":"Strawberry","price":60},
                4:{"name":"Butter Scotch","price":120}}
    for i in flavours:
        print(i,".",flavours[i]["name"],"- Rs.",flavours[i]["price"])
    fch = int(input("Enter the choice (1/2/3/4):"))
    q = int(input("Enter the quantity (In Numbers):"))
    bill(flavours,fch,q)
def stickIce():
    print("Stick Ice Categories")
    flavours = {1:{"name":"Chocolate","price":80},
                2:{"name":"Vanilla","price":100},
                3:{"name":"Strawberry","price":60},
                4:{"name":"Butter Scotch","price":120}}
    for i in flavours:
        print(i,".",flavours[i]["name"],"- Rs.",flavours[i]["price"])
    fch = int(input("Enter the choice (1/2/3/4):"))
    q = int(input("Enter the quantity (In Numbers):"))
    bill(flavours,fch,q)
greet()
while True:
    menu()
