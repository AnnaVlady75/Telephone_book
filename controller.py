import view
import database

def main():
    while  True:
        ask = view.user_input()
        if ask == 1:
            data_person = view.person()
            database.add_data(data_person)
        elif ask == 2:
            name = view.search()
            database.search_name(name)
        elif ask == 3:
            database.sort_name()
        elif ask == 4:
            database.sort_date()
        elif ask == 5:
            database.print_name()
        elif ask == 6:
            database.print_all() 
        elif ask == 7:
            data = view.search()
            new_lst_person = database.select_person(data)
            num = view.select_num()
            new_person = view.person()
            database.change_person(new_lst_person[num-1], new_person)
        elif ask == 8:
             data = view.search()
             new_lst_person = database.select_person(data)
             num = view.select_num()
             database.delete_person(new_lst_person[num-1])
        elif ask == 9:
            break    

main()            
