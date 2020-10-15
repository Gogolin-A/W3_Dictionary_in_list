account1 = {'login': 'ivan','password': 'q1'}
account2 = {'login': 'peter','password': 'q2'}
account3 = {'login': 'olga','password': 'q3'}
account4 = {'login': 'anna','password': 'q4'}
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}
user_list = [user1, user2, user3, user4]
user_list_modify = [user1, user2, user3, user4]
# первая часть:
key = input('Введите ключ (name или account): ').lower()
for i in range(1, 5):
    print('значение ключа name для юзера', i, '=', user_list[i-1].get(key, 'Введенный ключ не найден'))
# Вторая часть:
index_number = int(input('Введите порядковый номер: '))
try:
    temp = user_list[index_number-1]
    print('Данные по юзеру № ', index_number, ':', sep='')
    print('имя:', user_list[index_number-1]['name'])
    print('возраст:', user_list[index_number-1]['age'])
    print('логин:', user_list[index_number-1]['account']['login'])
    print('пароль:', user_list[index_number-1]['account']['password'])
except IndexError:
    print('Пользователь с указанным номером не найден')
# Третья часть:
end_number = int(input('Введите номер пользователя, которого нужно переместить в конец: ')) - 1
element = user_list_modify.pop(end_number)
user_list_modify.append(element)
print('Пользователь с именем', element['name'], 'перемещен в конец списка')
print('Список до изменения:', user_list)
print('Список после изменения:', user_list_modify)
# Четвертая часть:
average_age = (user1['age']+user2['age']+user3['age']+user4['age']) / 4
print('Средний возраст пользователей:', average_age)