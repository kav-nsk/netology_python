# Поиск общих друзей с помощью API VK
import requests

tokenX = '39c09d07ea08438d2c6483fd3a43567162ffa7fbe664061b8ec34cfd32e8e9571a2e1046ab77fc2bc7e9e'  # X-User, это я
#idX = '520465149'
tokenS = '7cc4f2b1731c4ccb8306314d995c64bf597cdf40ba4f8cea4a2267b6c5328138c49d8c4f8c5002c8201dd'  # Sulicko, это жена
#idS = '3720771'

class User:
    def __init__(self, token):
        self.token = token
        self.userId = str(self.getUserInfo({})['response'][0]['id'])    # сразу получаем параметром id пользователя
        return

    def __and__(self, other):
        friendsSelfSet, friendsOtherSet = set(), set()
        instancesFriends = []
        friendsSelf = self.getFriends()['response']['items']
        friendsOther = other.getFriends()['response']['items']

        for i in range(len(friendsSelf)):
            friendsSelfSet.add(friendsSelf[i]['id'])
        for i in range(len(friendsOther)):
            friendsOtherSet.add(friendsOther[i]['id'])

        mutualFriendsSet = friendsSelfSet & friendsOtherSet

        for i in mutualFriendsSet:
            F = 'Fr' + str(i)
            F = Frend()
            instancesFriends.append(F)
        return instancesFriends

    def __repr__(self):
        """Посредством print выводит адрес страницы."""
        response = self.getUserInfo({'fields': 'domain'})
        return 'https://vk.com/' + str(response['response'][0]['domain'])

    def getUserInfo(self, inputParams):
        '''Дает инфу о пользователе VK. В {inputParams} перечислить нужные поля.'''
        url = 'https://api.vk.com/method/users.get'
        params = {'access_token': self.token, 'v': '5.92'}  # по умолчанию
        params.update(inputParams)
        response = requests.get(url, params)
        return response.json()
    
    def getFriends(self):
        '''Отдает список ID друзей и другую информацию из поля 'fields'.'''
        url = 'https://api.vk.com/method/friends.get'
        params = {'access_token': self.token, 'v': '5.92', 'fields': 'first_name'}
        response = requests.get(url, params)
        return response.json()
    
    def getMutualFriends(self, targetId, targetIds):
        '''Выдает список общих друзей текущего пользователя.
           targetId - Пользователь с которым нужно искать общих друзей
           targetIds - Список пользователей с которыми нужно искать общих друзей'''
        url = 'https://api.vk.com/method/friends.getMutual'
        params = {'access_token': self.token, 'v': '5.92', 'source_uid': self.userId, 'target_uid': targetId, 'target_uids': targetIds}
        response = requests.get(url, params)
        return response.json()['response']

class Frend:
    pass
    

sUser = User(tokenS)
xUser = User(tokenX)

# Узнать о общих друзьях xUser и sUser используя методы API
mutualFriendsId = xUser.getMutualFriends(sUser.userId, '')
for i in mutualFriendsId:
    print('ID общих друзей:', i)
    print('Имя:', xUser.getUserInfo({'user_id': mutualFriendsId})['response'][0]['first_name'])

# Обработка оператора '&' c экземплярами класса
L = xUser & sUser
print('\nПолучили результат xUser & sUser типа:', type(L))
print('Список содержит в себе:')
for i in range(len(L)): print(type(L[i]))

# Отработка экземпляром функции print
print('\nСсылка на страницу текущего пользователя:')
print(xUser)


