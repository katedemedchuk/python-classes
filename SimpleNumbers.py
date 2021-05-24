# import math module for the next commands
import math 
# declare a variable and assign a value to it
number = input("Enter your number: ")
# convert the value of a variable to a numeric type
number = int(number)
# declare a variable and assign a value to it (boolean)
is_simple = True
# declare a variable and use math module which calculates the square root
middle = math.sqrt(number)
# cycle for i in range- the thing which generates a series of numbers within a given range. It doesnt include the last one.
for i in range(2,int(middle)+1):
    # variable rest for the rest of numbers with value number divide with the remainder from the variable middle
    rest = number % middle 
    # here I compare variable rest with the 0
    if rest == 0 :
        # declare variable with false value
        is_simple = False 
        # if value of variable is False cycle breaks
        break
    # f- format/ print value of variables 
print(f'{number} is simple: {is_simple}')