print("Welcome to BMI Calculator")
a=int(input("Enter your weight:"))
b=float(input("Enter Your Height in meters:"))
c=(a/(b*b))

if(c<18.5):
    print("Under Weight")
    
elif (18.5<=c<24.9):
    print("Normal")

elif (25<=c<29.9):
    print("Over Weight")
    
elif (30<=c<34.9):
    print("Obese")

else:
    print("Extremely Obese")