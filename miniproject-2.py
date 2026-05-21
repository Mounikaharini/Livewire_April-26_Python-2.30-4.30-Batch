import webbrowser as w
import time
def greet():
    print("""===========================================
             🎧♫♪ Syncaur ♪♫🎧
===========================================
""")

def menu():
    menulist = {1:{"name":"Headphones"},
                2:{"name":"Speakers"},
                3:{"name":"Ear Buds"},
                4:{"name":"Concert Headsets"},
                5:{"name":"Mic"}}
    print()
    for i in menulist:
        print(i,":",menulist[i]["name"])
    print()
    ch=int(input("Enter the choice (1/2/3/4/5):"))
    if ch==1:
        Headphones()
    elif ch==2:
        Speakers()
    elif ch==3:
        EarBuds()
    elif ch==4:
        ConcertHeadsets()
    elif ch==5:
        Mic()
    else:
        print("The product is currently not available")
        menu()
    
def bill(hlist,ch):
    print()
    item = hlist[ch]["name"]
    price = hlist[ch]["price"]
    quantity = int(input("Enter the quantity (In Numbers):"))
        
    bill=f"""         Syncaur
--------------------------
Item     :{item}
Quantity :{quantity}
Price    :Rs.{price}
--------------------------
Amount to pay :Rs.{(quantity*price)}
--------------------------
Thank you for visiting
"""
    print(bill)
    file = open(r"C:\Users\Livewire\Desktop\bill.docx","a")
    file.write(bill)
    file.close()
    
def Headphones():
    hlist = {1:{"name":"Sony","price":2500},
            2:{"name":"JBL:","price":6200},
            3:{"name":"Noise","price":2500},
            4:{"name":"Boat","price":1500},
            5:{"name":"One plus","price":5120}}
    print()
    for i in hlist:
        print(i,":",hlist[i]["name"]," Rs.",hlist[i]["price"])
    print()
    ch=int(input("Enter the choice (1/2/3/4/5):"))
    if ch==1:
        w.open_new_tab("https://www.sony.co.in/headphones")
        time.sleep(10)
        bill(hlist,ch)
        
    elif ch==2:
        w.open_new_tab("https://www.jbl.com/headphones/")
        time.sleep(10)
        bill(hlist,ch)
    elif ch==3:
        w.open_new_tab("https://www.gonoise.com/collections/headphones")
        time.sleep(10)
        bill(hlist,ch)
    elif ch==4:
        w.open_new_tab("https://www.boat-lifestyle.com/pages/searchtap-search?q=headphone")
        time.sleep(10)
        bill(hlist,ch)
    elif ch==5:
        w.open_new_tab("https://www.oneplus.in/oneplus-buds-4")
        time.sleep(10)
        bill(hlist,ch)
    else:
        print("The product is currently not available")
        menu()
greet()
menu()
