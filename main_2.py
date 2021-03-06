""" Вывести в файл groups.json список групп (с частью их параметров) в которых состоит пользователь,
но в которых нет его друзей. С применением API VK.
"""

import requests
import json
import time
from threading import Thread

token = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'
#id = '171691064'
userName = 'eshmargunov'


class UserInformer:

    def __init__(self, userName, token):
        self.token = token
        self.groupsInfo = {}    # Словарь с информацией о группах, в которых участвует экземпляр
        self.userId = str(self.user_info()['response'][0]['id'])    # Сразу запрашиваем id пользователя
        return

    def user_info(self):
        '''Дает инфу о пользователе VK.
        '''
        url = 'https://api.vk.com/method/users.get'
        params = {'access_token': self.token, 'v': '5.92'}
        response = requests.get(url, params)
        return response.json()

    def friends(self):
        '''Отдает список ID друзей и другую информацию из поля 'fields'.
        '''
        url = 'https://api.vk.com/method/friends.get'
        params = {'access_token': self.token, 'v': '5.92'}
        response = requests.get(url, params)
        return response.json()['response']['items']
    
    def groups(self):
        '''Выдает словарь в котором ключи, это id групп текущего пользователя, а значение - словарь с параметрами группы.
        '''
        url = 'https://api.vk.com/method/groups.get'
        params = {'access_token': self.token, 'user_id': self.userId, 'extended': 1, 'fields': 'members_count', 'v': '5.92'}
        response = requests.get(url, params)
        responseList = response.json()['response']['items']
        self.groupsInfo.update({i['id']: {'name': i['screen_name'], 'members_count': i['members_count']} for i in responseList})
        return True


def groups_of_friends(friendsId):
    '''Выдает множество id групп из списка друзей friendsId. Вторым пар-ром (j): число успешно опрошенных друзей;
    третьим (k):  число ошибок от сервера.
    '''
    url = 'https://api.vk.com/method/groups.get'
    params = {'access_token': token, 'v': '5.92'}
    j, k = 0, 0
    allGroupsFriends = set()

    #for i in [4929, 7858, 11952, 48807]:      # Для быстрой отладки
    for i in friendsId:
        params.update({'user_id': i})
        response = requests.get(url, params)
        if response.status_code != 200:
            k += 1
        if not 'error' in response.json().keys():
            allGroupsFriends = allGroupsFriends.union(response.json()['response']['items'])
            print('.')
            j += 1

    return allGroupsFriends, j, k

def save_to_json(inputData):
    with open("groups.json", "w") as dataFile:
        jsonData = inputData
        json.dump(jsonData, dataFile, ensure_ascii=False, indent=2)
    return True

# ================ MAIN SECTION =======================

infoShmargunov = UserInformer(userName, token)

# Ускоритель в отдельном потоке (получение групп и информации о них для текущего пользователя)
threadOne = Thread(target=infoShmargunov.groups)
threadOne.start()

friends = infoShmargunov.friends()

# Обработчик исключений для потенциально проблемного вызова функции
i = 1
while True: 
    try:
        allGroupsFriends = groups_of_friends(friends)
    except PermissionError:
        print('Есть проблемы с передачей данных. Пауза перед', i, 'попыткой 3с.')
        print('Для завершения программы нажмите ctr+C')
        time.sleep(3)
        i += 1
    else:
        break

print('Успешно опрошено', allGroupsFriends[1], 'из', len(friends), 'друзей')
print('Получено ошибок от сервера:', allGroupsFriends[2])

groupsUserWithoutFriends = set(infoShmargunov.groupsInfo.keys()) - allGroupsFriends[0]

dataToSave = [{'name': infoShmargunov.groupsInfo[i]['name'], 'gid': i, 'members_count': infoShmargunov.groupsInfo[i]['members_count']}
                for i in groupsUserWithoutFriends]
                
#print(time.clock())    # Скорость выполнения для отладки
save_to_json(dataToSave)
