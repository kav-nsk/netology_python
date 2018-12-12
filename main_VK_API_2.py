# Поиск общих друзей с помощью API VK
import requests

tokenX = '39c09d07ea08438d2c6483fd3a43567162ffa7fbe664061b8ec34cfd32e8e9571a2e1046ab77fc2bc7e9e'  # X-User, это я
#idX = '520465149'
tokenS = '7cc4f2b1731c4ccb8306314d995c64bf597cdf40ba4f8cea4a2267b6c5328138c49d8c4f8c5002c8201dd'  # Sulicko, это жена
#idS = '3720771'


class User:

    def __init__(self, token):
        self.token = token
        self.userId = str(self.get_User_Info({})['response'][0]['id'])    # сразу получаем параметром id пользователя
        return

    def __and__(self, other):
        urlFriends, friendsSelfId, friendsOtherId = [], {}, {}
        # получить все данные о друзьях
        friendsSelfData = self.get_Friends()['response']['items']        
        friendsOtherData = other.get_Friends()['response']['items']
        # заполнить словари ключами из 'id' и значениями 'domain'
        for i in range(len(friendsSelfData)):
            friendsSelfId[friendsSelfData[i]['id']] = friendsSelfData[i]['domain']
        for i in range(len(friendsOtherData)):
            friendsOtherId[friendsOtherData[i]['id']] = friendsOtherData[i]['domain']

        friendsSet = set(friendsSelfId.keys()) & set(friendsOtherId.keys()) # определить общих друзей
        # сформировать ответ из url адресов на страницы общих друзей
        for i in friendsSet:
            urlFriends.append('https://vk.com/' + friendsSelfId[i])
        return urlFriends

    def __str__(self):
        """Посредством print выводит адрес страницы."""
        response = self.get_User_Info({'fields': 'domain'})
        return 'https://vk.com/' + str(response['response'][0]['domain'])

    def get_User_Info(self, inputParams):
        '''Дает инфу о пользователе VK. В {inputParams} перечислить нужные поля.'''
        url = 'https://api.vk.com/method/users.get'
        params = {'access_token': self.token, 'v': '5.92'}  # по умолчанию
        params.update(inputParams)
        response = requests.get(url, params)
        return response.json()
    
    def get_Friends(self):
        '''Отдает список ID друзей и другую информацию из поля 'fields'.'''
        url = 'https://api.vk.com/method/friends.get'
        params = {'access_token': self.token, 'v': '5.92', 'fields': ['first_name', 'domain']}
        response = requests.get(url, params)
        return response.json()
    
    def get_Mutual_Friends(self, targetId, targetIds):
        '''Выдает список общих друзей текущего пользователя.
           targetId - Пользователь с которым нужно искать общих друзей
           targetIds - Список пользователей с которыми нужно искать общих друзей
        '''
        url = 'https://api.vk.com/method/friends.getMutual'
        params = {'access_token': self.token, 'v': '5.92', 'source_uid': self.userId, 'target_uid': targetId, 'target_uids': targetIds}
        response = requests.get(url, params)
        return response.json()['response']
    

sUser = User(tokenS)
xUser = User(tokenX)

# Узнать о общих друзьях xUser и sUser используя методы API
mutualFriendsId = xUser.get_Mutual_Friends(sUser.userId, '')
for i in mutualFriendsId:
    print('ID общих друзей:', i)
    print('Имя:', xUser.get_User_Info({'user_id': mutualFriendsId})['response'][0]['first_name'])

# Обработка оператора '&' c экземплярами класса
L = xUser & sUser
print('\n', 'Список общих друзей состоит из:', L, sep='')

# Отработка экземпляром функции print
print('\n', 'Ссылка на страницу текущего пользователя:', sep='')
print(xUser)