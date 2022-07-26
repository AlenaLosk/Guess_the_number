from random import *
from math import *
from time import *


# проверка, что введенная строка string является натуральным числом до границы border включительно
def is_valid(string, border):
    return string.isdigit() and 1 <= int(string) <= border


# запрос числа с предварительным выводом сообщения text
def get_number(text):
    while True:
        string = input(text)
        if is_valid(string, 100):
            return int(string)
        else:
            print('Некорректный ввод!', end='')


# загадываем число (1 элемент) и устанавливаем число попыток (2 элемент)
# с учетом верхней границы border включительно
def set_goal_number_and_attempt(border):
    return randint(0, border), ceil(log2(border))


# игровая логика, где attempts - число попыток, desired_number - загаданное число
def is_game_win(attempts, desired_number):
    temp = 0
    while attempts > 0:
        attempts -= 1
        temp += 1
        user_number = get_number(f'\nПопытка №{temp}: ')
        if desired_number < user_number:
            print('Слишком много! ', end='')
        elif desired_number > user_number:
            print('Слишком мало! ', end='')
        else:
            print('Ура, угадано! ')
            return True
        if attempts > 0:
            print('Попробуй еще раз: ', end='')
    return False


# Основная программа
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
