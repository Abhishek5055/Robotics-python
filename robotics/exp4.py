print("Welcome to the Trip Planner")
a=int(input("Enter the budget of your trip:"))

if(a<1000):
    print("Go to Restaurant")
    
elif(a>1000 and a<5000):
    print("Go to Amboli falls")
    
else:
    print("Go to Goa")