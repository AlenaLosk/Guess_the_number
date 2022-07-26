from random import *
from math import *
from time import *


def is_valid(string, border):
    return string.isdigit() and 1 <= int(string) <= border


def get_number(text):
    while True:
        string = input(text)
        if is_valid(string, 100):
            return int(string)
        else:
            print('Некорректный ввод!', end='')


def set_goal_number_and_attempt(b):
    return randint(0, b), ceil(log2(b))


def is_game_win(a, g):
    temp = 0
    while a > 0:
        a -= 1
        temp += 1
        user_number = get_number(f'\nПопытка №{temp}: ')
        if g < user_number:
            print('Слишком много! ', end='')
        elif g > user_number:
            print('Слишком мало! ', end='')
        else:
            print('Ура, угадано! ')
            return True
        if a > 0:
            print('Попробуй еще раз: ', end='')
    return False


flag = True
print('Добро пожаловать в числовую угадайку!\nДанная игра существует благодаря курсу "Поколение Python" '
      'https://stepik.org/course/58852')
while flag:
    upper_border = get_number('Введи любое число от 1 до 100, в рамках которого будет выбрано случайное: ')
    goal_number, attempt = set_goal_number_and_attempt(upper_border)
    print(f'Угадай, какое число было загадано?\nТы можешь {attempt} раз(а) ввести свой/и вариант(ы) ответа.', end='')
    flag = is_game_win(attempt, goal_number)
print('Игра окончена!')
sleep(6)
