'''
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********
'''

level = int(input('Сколько рядов у елки? '))
count_stars = level
while level > 0:
    count_1 = level
    while count_1 > 0:
        print(' ', end='')
        count_1 = count_1 - 1
    print('*', end='')
    level = level - 1
    count_2 = level
    while count_stars > count_2+1:
        print('**', end='')
        count_2 += 1
    print()