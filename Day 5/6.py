for number in range (1,101):
    if number in range (15,101,15):
        number = "FizzBuzz"
    elif number in range (3,101,3):
        number = "Fizz"
    elif number in range (5,101,5):
        number = "Buzz"

    print(number)
    
    #another method
    
# for number in range (1,101):
#     if number%3 == 0 and number%5==0:
#         number= "FizzBuzz"
#     elif number%3==0:
#         number = "Fizz"
#     elif number%5 == 0:
#         number = "Buzz"
    
#     print(number)