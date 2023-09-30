
def RestrEntry():
    rid=int(input("Enter resturant ID"))
    if rid not in restr:
        rname=input("Enter name of customer")
        ritems=input("Enter items ordered")
        rprice=input("Enter total item price")
        restr1=[rname,ritems,rprice]
        restr[rid]= restr1
    else:
        print("Customer is there")

def detailsedit():
    rid=int(input("Enter resturant ID"))
    if rid in restr:
        rname=input("Enter name of customer")
        ritems=input("Enter items ordered")
        rprice= input("Enter total price")
        restr1=[rname, ritems, rprice]
        restr[rid]= restr1
    else:
        print("Restr id not found")


def findcust():
    rname=input("Enter name to find customer")
    for i in restr:
        if restr[i][0]==rname:
            print(restr[i])

restr={}
cont=True
while cont:
    print()
    print()
    print("----------------------------------------------KVS RESTURANT-----------------------------------------")
    print("1. Entry of any customer")
    print("2. Edit customer details")
    print("3. Print all customer details")
    print("4. Find any of customer")
    print("5. Exit")
    print("--------------------------------------------KVS RESTURANT--------------------------------------------")
    choice=int(input("Enter valid choice"))
    if choice==5:
        cont= False
    elif choice ==1:
        RestrEntry()
    elif choice==2:
        detailsedit()
    elif choice==3:
        for i in restr:
            print(i,"   :   ", restr[i])
    elif choice==4:
        findcust()
        
               
