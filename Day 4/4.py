import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

x = len(names)
randomname = random.randint(0,x-1)

person_pay = names[randomname]


print(person_pay + " is going to buy the meal today.")