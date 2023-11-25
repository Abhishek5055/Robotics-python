print("Welcome to trip Planner!")
b=int(input("Enter Your Age:"))
if b>10:
    print("You can go to trip")
    a=int(input("Enter Your Amount:"))
       
    if(a<=1000):
        print("Go to Restaurant")
    
    elif(a>1000 and a<5000):
        print("Go to Amboli falls")

    else:
        print("Go to Goa")   

else:
    print("You Cannot go to trip alone go with  your parents")