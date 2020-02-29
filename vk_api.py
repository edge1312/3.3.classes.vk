import requests
import time


token = 'укажите здесь свой токен'


params = {
    'access_token': token,
    'v': '5.103'
}


class User():

    params = {
        'access_token': token,
        'v': '5.103'
    }
    
    def __init__(self, user_id):
        self.user_id = user_id


    def __str__(self):
        return self.domain

    
    def get_user_info(self):
        params = self.params
        response = requests.get(f'https://api.vk.com/method/users.get?user_id={self.user_id}&fields=domain', params)
        self.first_name = response.json()['response'][0]['first_name']
        self.last_name = response.json()['response'][0]['last_name']
        self.id = response.json()['response'][0]['id']
        self.domain = f"https://vk.com/{response.json()['response'][0]['domain']}"


    def get_user_friends(self):
        params = self.params
        response = requests.get(f'https://api.vk.com/method/friends.get?user_id={self.user_id}', params)
        self.friends_set = set(response.json()['response']['items'])


def input_id(num):
    try:
        user_id = int(input(f'Введите ID {num} пользователя (integer): '))
    except ValueError:
        print('Вы ввели не число')
        user_id = input_id(num)
    return user_id


def print_common_friends(user_1, user_2):
    common_friends_set = user_1.friends_set.intersection(user_2.friends_set)
    friends_list = []
    if len(common_friends_set) == 0:
        print()
        print('Пользователи')
        print(f'id{user_1.id} {user_1.first_name} {user_1.last_name} ({user_1.domain}) и id{user_2.id} {user_2.first_name} {user_2.last_name} ({user_2.domain})')
        print('не имеют общих друзей')
    else:
        print()
        print('Для пользователей')
        print(f'id{user_1.id} {user_1.first_name} {user_1.last_name} ({user_1.domain}) и id{user_2.id} {user_2.first_name} {user_2.last_name} ({user_2.domain})')
        print('найдены общие друзья:')
        for friend in common_friends_set: 
            friends_list.append(User(friend)) 
        for friend in friends_list:         
            friend.get_user_info()      
            print(f'id{friend.id} {friend.first_name} {friend.last_name} ({friend.domain})')
            time.sleep(0.4)               


user_1_id = input_id('1-го')
user_1 = User(user_1_id)
user_2_id = input_id('2-го')
user_2 = User(user_2_id)

user_1.get_user_info()
user_1.get_user_friends()
user_2.get_user_info()
user_2.get_user_friends()

print_common_friends(user_1, user_2)

print(user_1)
print(user_2)



