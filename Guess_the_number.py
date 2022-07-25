from random import *
from math import *


def is_valid_digit(string, border):
    return string.isdigit() and 1 <= int(string) <= border


def get_number(text):
    while True:
        string = input(text)
        if is_valid_digit(string, 100):
            return int(string)
        else:
            print('Некорректный ввод!', end='')


upper_border = get_number('Введи любое число от 1 до 100, в рамках которого будет выбрано случайное: ')
goal_number, attempt = randint(0, upper_border), ceil(log2(upper_border))
print(f'Угадай, какое число было загадано? У тебя {attempt} попытки', end='')
temp = attempt + 1

while attempt > 0:
    user_number = get_number(f'\nПопытка №{temp - attempt}: ')

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
