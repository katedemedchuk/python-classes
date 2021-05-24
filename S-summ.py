# declare a variable assign a value to it 
typed_numbers = input("Type your numbers: ")
# declare a variable with value and a split function to it
splited = typed_numbers.split()
# declare a variable with list value
numbers = []
# cycle for execute all items in splitted 
for item in splited:
      #   every item on splitted and append to numbers
   numbers.append(float(item))
   # print all variables
print(typed_numbers)
print(splited)
print(numbers)
print(sum(numbers))
