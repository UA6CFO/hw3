# задача про всяких там юзеров
# ----------------------------
# Стая воробушков к югу промчалась,
# Знать надоело говно им клевать.
# На осине ворона усралась,
# Ну и задачка, иобшумать !!!
# ----------------------------

import os

count = 0 # счётчик записей в словаре
avg_user_age = 0 # для подсчёта на пальцах средннего возраста юзеров

# тупо набиваем данные
account1 = {'login':'ivan', 'password':'q1'} 
account2 = {'login':'petr', 'password':'q2'}
account3 = {'login':'olga', 'password':'q3'}
account4 = {'login':'anna', 'password':'q4'}

# продолжаем тупо набивать данные и чой-то с ними вытворять...
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

user_list = [] # да нехай словарик проинициализируется часом - иногда полезно

# отгружаем апельсины бочками...
user_list.append(user1)
user_list.append(user2)
user_list.append(user3)
user_list.append(user4)

# ну-с, понеслась моча по трубам...
os.system('cls') # почистим карму терминала
key = input('Введите ключ -> ').lower() # и вЫнимательно спросим
# пощщупаем вымя этому словарику с пристрастием
for i in user_list:
    count = count + 1 # посчитаем количество записей юзеров
    avg_user_age = avg_user_age + i.get('age', '') # накопим возраста юзеров для куркулятора
    # а вот тут надо бы помароковать как-бэ покрасивше вывод сварганить...
    if ((str(key) != 'login') and (str(key) != 'password')):
        print('Значение для ключа "{}" для юзера {} = {}'.format(str(key), str(count), i.get(str(key), 'Такого ключа не существует !')))
    else:
        print('Значение для ключа "{}" для юзера {} = {}'.format(str(key), str(count), i['account'][str(key)]))

# применим термоанальный криптоанализатор для одного юзера
key = int(input('Введите порядковый номер (от 0 до ' + str(count - 1) + ') -> ')) # пока обойдёмся без паяльника - рановато исчо...
# не дадим испортить нам обедню злым проискам врагов !
if ((key >= 0) and (key <= count - 1)):
    print('Данные по юзеру № ' + str(key))
    for i in user_list[key]:
        if str(i) != 'account':
            print('{} = {}'.format(str(i), user_list[key][str(i)]))
        else:
            for j in user_list[key]['account']:
                print('{} = {}'.format(str(j), user_list[key]['account'][str(j)]))
else:
    print('Введённое значение вне диапазона !', end='\n\n')

# вау, погоняем данные с конца в конец...
key = int(input('Введите номер пользователя (от 0 до ' + str(count - 1) + '), которого нужно переместить в конец -> '))                
print('Это начальный вариант словаря -> ', end='\n\n')    
print(user_list, end='\n\n')
try:
    element = user_list.pop(key)
    user_list.append(element)
    print('Это _конченный_ вариант словаря -> ', end='\n\n')
    print(user_list, end='\n\n') # м-да, тут даже прокомментировать нечего, абЫднА, да ?!
except: # ну лениво выискивать ошибку при выходе за предел индекса - нехай на всё капкан насторожится...
    print('Перемещения данных не произошло - смотрите что вводите !!!', end='\n\n')    

# рассчитаем средний возраст юзеров
avg_user_age = avg_user_age / count
print('Средний возраст юзеров = ' + str(avg_user_age), end='\n\n')
print('И програмке вот конец, а кто проверял - тот молодец !  ;-)', end='\n\n')
