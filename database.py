def add_data(data):
    with open("db.txt", "a") as file:
        file.write(data)
    print("Тел книга обновлена \n")   

def search_name(name):
     with open("db.txt", "r") as file:
        data = file.readlines()
        flag = False
        for i in data:
            if name in i:
                print(i)
                flag = True
        if flag == False:
            print("Такого не найдено, повторите поиск\n") 

def sort_name():
    with open("db.txt", "r") as file:
        data = file.readlines()     
        data.sort()
    with open("db.txt", "w") as file:
        file.writelines(data)     

def sort_date():
    with open("db.txt", "r") as file:
        data = file.readlines()     
        data.sort(key=lambda x: x[5])
    with open("db.txt", "w") as file:
        file.writelines(data)      

def print_name():
    with open("db.txt", "r") as file:
        data = file.readlines()  
        for i in data:
            print(i.split(";")[0])

def print_all():
    with open("db.txt", "r") as file:
        print(file.read())

def select_person(data):
    count = 1
    new_lst_person = []
    with open("db.txt", "r") as file:
        data_str = file.readlines()     
        for i in data_str:
            if data in i:
                print(f"{count}) {i}")
                count+=1
                new_lst_person.append(i)
    return new_lst_person        

def change_person(last_str, new_str):
    with open("db.txt", "r") as file:
        all_list = file.readlines()     
    with open("db.txt", "w") as file:    
        for i in all_list:
            if i == last_str:
               file.write(new_str)
               continue
            file.write(i)
    print("запись изменена!")     

def delete_person(data):
    with open("db.txt", "r") as file:
        all_list = file.readlines()     
    with open("db.txt", "w") as file:    
        for i in all_list:
            if data == i:
                continue
            file.write(i)
    print("запись удалена!")         
