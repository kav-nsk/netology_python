# Программа поиска строки в файлах. Выводит список файлов, содержащих требуемую строку и общее количество найденных файлов.
# Далее ожидается снова ввод строки и очередной поиск в ранее найденном перечне файлов. Выход через   ctr + C.

# Global data objects
#remoteDir = '/home/kav/Документы/Учебные курсы/Python develop/Python_base/1.9 Пути, файлы, запуск программ/Migrations/'
remoteDir = '/home/kuzovlevav/PycharmProjects/python_develop/Files&Path/Migrations'
listFilesFilesForDel = []

# Import library
import os

# Clases

# Function
def subtraction(sourceList, subList):
    """Удаляет записи из списка-источника, записи в списке указанном вторым параметром."""
    return list(set(sourceList) - set(subList))

# Main section
os.chdir(remoteDir)
listFiles = os.listdir(remoteDir)   # исходный список файлов

for files in listFiles:             # удаляем не .sql файлы из списка файлов, записывая их в отдельный список...
    if not '.sql' in files:
        listFilesFilesForDel.append(files)
listFiles = subtraction(listFiles, listFilesFilesForDel)    # ...и пропуская его через функцию

while True:
    i = 0
    listFilesForDel = []            # обнуляем для последующего использования
    s = input('Введите строку которую ищите в sql файле >>> ')

    for nameFiles in listFiles:                                             # цикл по списку .sql файлов
        flagForDel = True
        for line in open(nameFiles, encoding='utf-8', errors='ignore'):     # цикл по строкам в файле
            str(line.strip('\t'))
            str(line.strip(' '))
            str(line.strip('\n'))
            if line.find(s) != -1:          # есть вхождение!
                flagForDel = False
        if flagForDel:                      # ...иначе, вносим файл в список на удаление
            listFilesForDel.append(nameFiles)
        else:
            i += 1
            print(nameFiles)
    listFiles = subtraction(listFiles, listFilesForDel)     # изменяем исходный список имен файлов
    print('Всего файлов в котором найдена строка:', i)
