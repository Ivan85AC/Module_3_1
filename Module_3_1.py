calls = 0


def count_calls():
    global calls
    calls += 1


def string_info():
    string = input('Введите слово: ')
    tuple_ = tuple((len(string), string.upper(), string.lower()))
    print(tuple_)
    count_calls()


def is_contains():
    string = input('Введите слово: ').lower()
    list_to_serch = [(input('Введите несколько слов: ')).lower()]
    for i in list_to_serch:
        if string in i:
            print(True)
            break
        else:
            print(False)
    count_calls()


string_info()
string_info()
is_contains()
is_contains()
print(calls)
