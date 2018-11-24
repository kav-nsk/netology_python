# Задача № 1
# Вариант программы вычисления выражения состоящего из одного оператора и
# двух операндов в польской нотации с выполнением проверки корректности ввода данных

# глобальные объекты

# определение функций
def calcFromPol(s):
    # проверки на корректность записи выражения с помощью исключений. Если на позиции символ оператора, а не число, то...
    rezult = -1, None               # возвращаемый результат функции при отказе от вычисления
    try:                       # ...если оператор последний, вырубаем вычисления
        int(s[2])
    except ValueError:
        return rezult

    try:                        # ...если оператор первый, вычисляем в соответствии с ним
        int(s[0])
    except ValueError:
        try:                    # ...если оператор стоит по ошибке еще и вторым, вырубаем вычисления
            int(s[1])
        except ValueError:
            return rezult
        if s[0] == '+':
            rezult = int(s[1]) + int(s[2])
        if s[0] == '-':
            rezult = int(s[1]) - int(s[2])
        if s[0] == '*':
            rezult = int(s[1]) * int(s[2])
        if s[0] == '/':
            rezult = int(s[1]) / int(s[2])
        return rezult, False

    try:                        # если оператор посередине, вычисляем в соответствии с ним
        int(s[1])               # и выставляем флаг предупреждения
    except ValueError:
        s[0], s[1], s[2] = s[1], s[0], s[2]     # перекомпоновка выражения перед рекурсивным вызовом функции
        return calcFromPol(s)[0], True


# главный модуль
print('Введите выражение в польской нотации, разделяя оператор и операнды пробелами >>> ', end='')
s = input().split(' ')
answer = calcFromPol(s)

if False in answer:
    print('Ответ:', answer[0])
elif True in answer:
    print('Вы не знаете польскую запись выражений, но я все равно вычислю. Ответ:', answer[0])
elif None in answer:
    print('Неправильная запись выражения. Вычисление невозможно.')

