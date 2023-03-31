
print("Welcome to the Rollercoaster!")
height = int(input("what is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age< 12:
        print("Child tickets are $5.")
        bill=5
    elif age< 18:
        print("youth tickets are $7.")
        bill = 7
    elif age>= 45 and age<= 55:
        print("You avail free tickets.")
    else:
        print("Youth tickets are $12.")
        bill= 12
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo =="y":
        bill += 3
        
    print(f"you final bill is ${bill}")
        
    
else :
    print("Sorry, you have to grow taller ")