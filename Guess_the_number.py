from random import *
from math import *
upper_border = int(input('Введи любое число от 1 до 100, в рамках которого будет выбрано случайное: '))
print('Угадай, какое число было загадано? ', end='')
goal_number = randint(0, upper_border)
attempt = ceil(log2(upper_border))

while attempt > 0:
    user_number = int(input())
    if goal_number < user_number:
        print('Слишком много! ', end='')
    elif goal_number > user_number:
        print('Слишком мало! ', end='')
    else:
        print('Ура, угадано! ')
        break
    attempt -= 1
    if attempt > 0:
        print('Попробуй еще раз: ', end='')

print('Игра окончена!')
