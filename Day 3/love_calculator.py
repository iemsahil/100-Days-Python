print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()
word_t1 = lower_name1.count("t")
word_t2 = lower_name2.count("t")
word_t = int(word_t1)+int(word_t2) 

word_r1 = lower_name1.count("r")
word_r2 = lower_name2.count("r")
word_r = int(word_r1)+int(word_r2) 

word_u1 = lower_name1.count("u")
word_u2 = lower_name2.count("u")
word_u = int(word_u1)+int(word_u2) 

word_e1 = lower_name1.count("e")
word_e2 = lower_name2.count("e")
word_e = int(word_e1)+int(word_e2) 

total1 = int(word_t) + int(word_r) + int(word_u) + int(word_e)


word_l1 = lower_name1.count("l")
word_l2 = lower_name2.count("l")
word_l = int(word_l1)+int(word_l2) 

word_o1 = lower_name1.count("o")
word_o2 = lower_name2.count("o")
word_o = int(word_o1)+int(word_o2) 

word_v1 = lower_name1.count("v")
word_v2 = lower_name2.count("v")
word_v = int(word_v1)+int(word_v2) 


total2 = int(word_l) + int(word_o) + int(word_v) + int(word_e)

total = str(total1)+ str(total2)

totalf = int(total)

if totalf <= 10 or totalf >= 90:
    print(f"your score is {total}, you go together like coke and mentos.")
elif totalf >= 40 and totalf<= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")