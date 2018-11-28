# Раздел функций

    # Обработка данных и их сохранение в словаре cook_book
def converter_to_cook_book():
    dump_list = open('list.txt').readlines()        # открываем исходный файл, читаем все в один список
    cook_book = {}
    dish_flag = False                   # False - если записи блюда не было в cook_book
    for string in dump_list:
        pos = dump_list.index(string)   # позиция строки в дампе
        if not dish_flag:
            dish_key = string.rstrip()  # взять название блюда, отсечь \n
            cook_book[dish_key] = []    # создаем новый ключ по названию блюда и список к нему
            dish_flag = True
            num_i = int(dump_list[pos + 1])                         # получить число ингридиентов
            for i in range(num_i):
                i_list = dump_list[pos + 2 + i].rstrip().split('|') # в списке ингридиентов отсекаем \n,
                                                                    # делаем список строк по '|'
                # очистка записей в i_list от лишних пробелов
                for s in i_list:
                    i_list[i_list.index(s)] = s.strip()
                # вкладываем словарь с ингридиентом в список блюда
                cook_book[dish_key].append(dict(zip(['ingridient_name', 'quantity', 'measure'], i_list)))
        if string == '\n':              # при встрече новой строки --> вписать новое блюдо
            dish_flag = False
    return cook_book

    # Составление перечня закупок продуктов под требуемое кол-во блюд
def get_shop_list_by_dishes(dishes_list, person_count):
    shop_list = {}
    cook_book = converter_to_cook_book()                        # обращаемся к функции генерации словаря cook_book
    for dish in dishes_list:
        for dish_key in cook_book:
            if dish == dish_key:                                # нашли нужное блюдо в cook_book
                for string in range(len(cook_book[dish_key])):
                    i_list = cook_book[dish_key][string]        # извлечь строку ингридиентов из cook_book
                    i_name = i_list['ingridient_name']          # получить из строки ингридиентов название продукта
                    if i_name in shop_list: # если запись о продукте уже есть --> складываем количество, умножаем на
                        shop_list[i_name]['quantity'] += int(i_list['quantity']) * person_count             # кол-во блюд
                    else:                   # иначе, делаем новую запись о продукте с учетом требуемого кол-ва
                        shop_list[i_name] = dict(measure=i_list['measure'], quantity=int(i_list['quantity']) * person_count)

    return shop_list


# Главный модуль

print('*'*8, 'ЗАДАЧА 1', '*'*8)
print(converter_to_cook_book())

print('\n', '*'*8, 'ЗАДАЧА 2', '*'*8)
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))
