def user_input():
    ask = int(input("Выбери ниже\n 1- записать пользователя\n 2- найти по имени\n"
                    "3-сортировка по имени\n 4-сортировка по дате рождения\n"
                    "5- вывод только имени\n 6- вывод всего файла\n"
                    "7-удалить\n 8- изменить\n 9- выход\n"))
    return ask

def person():
    name = input("введите имя: ")
    last_name = input("введите фамилию: ")
    patronymic = input("введите отчество: ")
    date_of_birth = input("введите дату рождения: ")
    telephone = input("введите номер телефона:")
    data = name + "; " + last_name + ";" + patronymic + "; " + date_of_birth +"; " + telephone + "; " + "\n"
    return data.lower()

def search():
    str_search = input("строка для поиска  ").lower()
    return str_search

def select_num():
    num = int(input("выбери строку для удаления: "))
    return num