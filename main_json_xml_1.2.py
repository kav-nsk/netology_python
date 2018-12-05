# Чтение и обработка json и xml файлов. Требуется составить топ-10 наиболее часто встречающихся слов из новостных лент
#           длиною более 6 символов.

# Global data objects
allWordsSet = set()                 # Множество всех встречающихся слов.
allTextDict = {}                    # Словарь с текстом новостей.

# Import library
import json
from xml.etree.ElementTree import XMLParser, ElementTree

# Clases

# Functions
def get_word_over_six_let(incomingText):
    """Выдает множество со словами из более чем шести букв."""
    outputSet = set()
    incomTextList = incomingText.split(' ')
    incomTextList.sort(key=len ,reverse=True)
    for word in incomTextList:              # Ищем слова длиннее 6 букв.
        if len(word) > 6:
            outputSet.add(word.lower())     # Добавляем их в результирующее множество в нижнем регистре.
        else: break
    return outputSet

def get_top10_words_from_news(allWordsSet, allTextDict):
    """На основе множества встречающихся слов allWordsSet и текстового словаря с новостями, выдает словарь со списками слов. Ключ списка соотвествует
    числу повторений слова (слов) из allWordsSet во входящем словаре."""
    resultOverlapsDict = {}         # Словарь списков с данными результатов.

        # Внешний цикл - перебор по множеству уникальных слов, внутренний цикл - поиск на совпадение слова в новости ленты.
    for word in allWordsSet:
        it = 0                      # Число повторений слова в текстах новостей
        for i in range(len(allTextDict)):    
            if word in allTextDict[i]:
                it += 1
        if it > 1:
            if it in resultOverlapsDict.keys():  # Если ключ соответствующий числу повторов слова уже был, дополняем список новым словом.
                resultOverlapsDict[it].append(word)
            else:                                # Или создаем новую запись c ключом равным числу повторений слова.
                resultOverlapsDict[it] = [word]
    return resultOverlapsDict

def print_result_top10(resultOverlapsDict, title):
    """Вывод результата работы на экран в удобном виде."""
    #print(resultOverlapsDict)
    keyList = list(resultOverlapsDict.keys())
    keyList.reverse()
    del keyList[10:]    # Используем только 10 первых записей.
    print('++++ 10 слов длиннее шести букв наиболее часто встречающихся в новостных лентах формата %s ++++' % title)
    n = 0
    l = []
    for i in keyList:
        for j in range(len(resultOverlapsDict[i])): l.append(resultOverlapsDict[i][j])
        n += len(resultOverlapsDict[i])
        if n >=10: break
    for i in range(10): print(l[i])
    return True


# Main section
    # Обработка json файла -------------------------------------------------------------------------------------
newsFile = open('newsafr.json')
jsonText = json.load(newsFile)
lenJsonText = len(jsonText['rss']['channel']['items'])

        # Создаем словарь новостных строк с ключами в виде номера итерации.
for i in range(lenJsonText):
    allTextDict[i] = jsonText['rss']['channel']['items'][i]['description'].lower()

        # Заполняем множество allWordsSet всеми встречающимися в description словами длиннее 6 букв для дальнейшего поиска совпадений.
for i in range(lenJsonText):
    description = jsonText['rss']['channel']['items'][i]['description']
    allWordsSet = allWordsSet | get_word_over_six_let(description)
        # Наиболее часто втречающиеся в новостях слова оборачиваем в словарь.
resultOverlapsDict = get_top10_words_from_news(allWordsSet, allTextDict)

        # Вывод результата.
print_result_top10(resultOverlapsDict, '.json')

    # Обработка XML файла ------------------------------------------------------------------------------------
tree = ElementTree()
xmlTree = tree.parse('newsafr_2.xml')

        # Создаем словарь новостных строк с ключами в виде номера итерации.
textList, idList = [], []
for nodeDesc in xmlTree.findall('channel/item/description'):
    text = nodeDesc.text
    textList.append(text.lower())

for i in range(len(textList)):
    idList.append(i)
    
allTextDict = dict(zip(idList, textList))

        # Заполняем множество allWordsSet всеми встречающимися в description словами длиннее 6 букв для дальнейшего поиска совпадений.
lenText = len(idList)
for i in range(lenText):
    allWordsSet = allWordsSet | get_word_over_six_let(text)

        # Определяем наиболее часто втречающиеся в новостях слова.
resultOverlapsDict = get_top10_words_from_news(allWordsSet, allTextDict)

        # Вывод результата.
print_result_top10(resultOverlapsDict, '.xml')