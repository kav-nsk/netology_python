# Вариант программы для домашнего задания по теме "Исключения".
# Добавлена функция вывода имен всех владельцев документов. С помощью исключения
# KeyError в функциях get_list_allName и get_list проверяется, есть ли поле "name" у документа.

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "1111111"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_list_allName():                 # Вывести список имен владельцев документа
    return_list_name = []               # с проверкой на ключа "name" в справочнике
    try:
        for i in range(len(documents)):
            return_list_name.append(documents[i]['name'])
    except KeyError:
        print('У документа №',documents[i]['number'],'отсутствует поле "name".')
    return return_list_name

def get_name_on_number(num_doc):        # Получить ФИО по номеру документа
    result = False
    for i in range(len(documents)):
        if num_doc == documents[i]['number']:
            result = documents[i]['name']
    return result

def get_list():                         # Вывод полного списка в формате: doc type/number/name
    return_list_doc = []                # функция дополнена реакцией на отсутствия ключа "name"
    return_list_num = []                # по аналогии с get_list_allName
    return_list_name = []
    try:
        for i in range(len(documents)):
            return_list_doc.append(documents[i]['type'])
            return_list_num.append(documents[i]['number'])
            return_list_name.append(documents[i]['name'])
    except KeyError:
        print('У документа №',documents[i]['number'],'отсутствует поле "name".')
    finally:
        pass
    return (list(zip(return_list_doc, return_list_num, return_list_name)))

def get_dir_on_number(num_doc):         # Получить номер полки по номеру документа
    result = False
    for i in directories.keys():
        for j in range(len(directories[i])):
            if num_doc == directories[i][j]:
                result = i
    return result

def get_add_new(num_doc, type_doc, fio, num_dir):  # Добавить новую запись
    documents.append({'type':type_doc, 'number':num_doc, 'name':fio})
    directories[num_dir] = [num_doc]
    return True

def input_num_doc():                    # для частого ввода номера документа
    return input('Введите номер документа >>> ')


print('Какие действия в справочнике документов хотите выполнить?\nНажмите:\n',
      'n - для вывода списка всех владельцев документов\n',
      'p - для получения ФИО по номеру документа\n',
      'l - для вывода всех записей в формате: вид документа/номер документа/ФИО\n',
      's - узнать номер полки по номеру документа\n',
      'a - добавить новую запись в справочник\n',
      'q - для выхода из программы')

action = ''
while action not in ('n', 'p', 'l', 's', 'a', 'q'):
    action = input('>>> ')

    if action == 'n':
        #print(get_list_allName())
        output_list = get_list_allName()
        for i in output_list:
            print(i)

    if action == 'p':
        num_doc = get_name_on_number(input_num_doc())
        if not num_doc:
            print('Запись не обнаружена.')
        else:
            print('Найден:', num_doc)

    if action == 'l':
        output_list = get_list()
        for i in range(len(output_list)):
            for j in range(len(output_list[i])):
                print(output_list[i][j], end=' ')
            print()

    if action == 's':
      num_dir = get_dir_on_number(input_num_doc())
      if not num_dir:
        print('Запись не обнаружена.')
      else:
        print('Документ лежит на полке №', num_dir)

    if action == 'a':
        fio = input('Введите ФИО >>> ')
        type_doc = input('Введите вид документа >>> ')
        num_doc = input_num_doc()
        num_dir = input('Введите номер полки для хранения >>> ')
        if get_add_new(num_doc, type_doc, fio, num_dir):
            print('Выполнено.')

    if action == 'q':
        break
    action = ''