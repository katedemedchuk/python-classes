# Написать программу, которая будет принимать целое число (день в году)
# (Считаем, что год начинается с понедельника)
# И выводит какой это день (Рабочий/Суббота/Воскресенье)
day = input('Enter your day: ')
day = int(day)
week_day =  day % 7 
if week_day == 0:
    print("SUN")
if week_day == 6:
    print("SAT")
if week_day > 0 and week_day < 6:
    print("WORKDAY")



