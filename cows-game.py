Быки и коровы (https://ru.wikipedia.org/wiki/Быки_и_коровы#Правила_игры)
написать консольное приложение(игра)
Компьютер загадывает четыре неповторяющиеся цифры от 0 до 9
Предлагается пользователю попытаться их угадать 
В ответ выдет количество цифры которые совпали по значению с загаданным и стоят на своем месте (быки)
и количество цифры, которые есть в загаданном числе, но стоят не на своем месте (коровы)
В конце игры вывести сообщение (Муу! Вы победили)

import random
numbers = [0,1,2,3,4,5,6,7,8,9]
cow = []
bull = []
print("Муу! Вы победили")