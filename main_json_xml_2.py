# Чтение и обработка json и xml файлов. Требуется составить топ-10 наиболее часто встречающихся слов из новостных лент
#           длиною более 6 символов.

# Global data objects

# Import library
import json
from xml.etree.ElementTree import XMLParser, ElementTree

# Functions
def get_word_over_six_let(incomingText):
    """Выдает список слов из более чем шести прописных букв."""
    incomingText = incomingText.split(' ')
    output = sorted([word.lower() for word in incomingText], key=len, reverse=True)
    for word in output:
         if len(word) <= 6:                     # Удаляем слова из 6 и менее букв.
             del output[output.index(word):]
             break
    return output

def get_top10_words(allWordsSet, allText):
    """На основе множества уникальных слов allWordsSet и набора слов из новостей,
     выдает словарь со списками слов. Ключ списка соотвествует числу повторений слова (слов) из allWordsSet в новостях."""
    output = {}
    for word in allWordsSet:
        it = 0
        it += allText.count(word)
        if it > 1:
            if it in output.keys():  # Если ключ соответствующий числу повторов слова уже был, дополняем список новым словом.
                output[it].append(word)
            else:                                # Или создаем новую запись c ключом равным числу повторений слова.
                output[it] = [word]
    return output

def print_result_top10(inputDict, title):
    """Вывод результата работы на экран в удобном виде."""
    #print(inputDict)
    keyList = list(inputDict.keys())
    keyList.sort(reverse=True)
    print('++++ 10 слов длиннее шести букв наиболее часто встречающихся в новостных лентах формата %s ++++' % title)
    n = 0
    L = []
    for i in keyList:
        for j in range(len(inputDict[i])): L.append(inputDict[i][j])
        n += len(inputDict[i])
        if n > 10: break
    for i in range(10): print(L[i])
    return True


# Main section
# Обработка json файла -------------------------------------------------------------------------------------
newsFile = open('newsafr.json')
jsonText = json.load(newsFile)
lenJsonText = len(jsonText['rss']['channel']['items'])
allText = ''                    # Строка для всех новостей.

for i in range(lenJsonText):    # Извлекаем слова из всех новостных строк в одну строку.
    allText = allText + (jsonText['rss']['channel']['items'][i]['description'])

allText = get_word_over_six_let(allText)              # Выбираем слова длиннее 6 букв из всех новостей.
    # Повторно втречающиеся в новостях слова оборачиваем в словарь, скармливая множество уникальных слов и весь текст.
resultOverlapsDict = get_top10_words(set(allText), allText)
    # Выводим результат
print_result_top10(resultOverlapsDict, '.json')

# Обработка XML файла ------------------------------------------------------------------------------------
tree = ElementTree()
xmlTree = tree.parse('newsafr_2.xml')
allText = ''

for nodeDesc in xmlTree.findall('channel/item/description'):
    allText += nodeDesc.text

allText = get_word_over_six_let(allText)
resultOverlapsDict = get_top10_words(set(allText), allText)

print_result_top10(resultOverlapsDict, '.xml')