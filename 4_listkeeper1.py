#
import os 
import sys

class CurrentModeError(Exception):
    """Вызывается, если current_mode пустой, или принимает значение отличное от FILELIST, FILE"""
    pass

class UserKeyError(Exception):
    """Вызываем, если введеные пользователем данные являются валидными, но не вызывают ни одну из команд"""
    pass

def main():
    """Тип меню - FILELIST, FILE"""
    current_mode = "FILELIST"

    """ Список с вставленными значениями """
    inserted_list = []

    """ Список с удаленными значениями """
    deleted_list = []

    """ Список файлов с расширением lst"""
    filelist = []

    """ Печатать файл и строку начиная с нуля (0) или с единицы (1) """
    START_WITH_ZERO = 0

    """ Индекс выбранного файла """
    selected_file_num = -1

    default_key = "a"

    """ 
        1. Обновляем список файлов с нужным расширением
        2. Печатаем содержимое в зависимости от типа меню
        3. Ожидаем пользовательских действий
    """
    while True:
        filelist = refresh_filelist()
        print_content(current_mode, inserted_list, deleted_list, filelist, START_WITH_ZERO, selected_file_num)
        current_mode, selected_file_num, inserted_list, deleted_list = prompt_input(current_mode, filelist, START_WITH_ZERO, selected_file_num, inserted_list, deleted_list, default_key)
        #print(current_mode)

""" Возвращаем список файлов с нужным расширением """
def refresh_filelist(extension="lst"):
    filelist = os.listdir()
    filelist = [file for file in filelist if len(file.split(".")) > 1 and file.split(".")[1] == extension]
    return filelist

def print_content(current_mode, inserted_list, deleted_list, filelist, START_WITH_ZERO, selected_file_num):
    try:
        if current_mode == "FILELIST":
            print_header()
            print_filelist(filelist, START_WITH_ZERO)
        elif current_mode == "FILE":
            print_header()
            print_file_content(filelist, selected_file_num, inserted_list, deleted_list, START_WITH_ZERO)
        else:
            raise CurrentModeError
    except CurrentModeError:
        msg = "Variable current_mode is empty" if not current_mode else "Variable current_mode has value: " + current_mode
        print("Error:", msg)

def print_header(heading="List Keeper", width=75):
    print("{0:-^{1}}".format(heading, width))

def print_filelist(filelist, START_WITH_ZERO):
    if filelist:
        for num, filename in enumerate(filelist):
            print("{0}:  {1}".format(num + START_WITH_ZERO, filename))
    else:
        print("No files found!")

def add_file(filelist, extension="lst"):
    filename = ""
    while not(filename):
        filename = str(input("Enter new file name:")).strip().lower()
        if not(filename):
            print("No name was specified!")  
            continue
        else:
            filename = filename if len(filename.split(".")) > 1 and filename.split(".")[-1] == extension else filename + "." + extension
        try:
            if filename in filelist:
                raise FileExistsError
            else:
                file = open(filename, "w")
                file.close()
        except FileExistsError:
            print("File already exists!")
            filename = ""
            continue

def check_is_file_empty(filelist, selected_file_num):
    try:
        file = open(filelist[selected_file_num], "r")
        i = 0
        for line in file:
            if i == 0:
                pass
            else:
                break
            i += 1
    except FileNotFoundError as err:
        print(err)
    finally:
        file.close()
    return i

def print_file_content(filelist, selected_file_num, inserted_list, deleted_list, START_WITH_ZERO):
    #print("inserted_list = ", inserted_list)
    #print("deleted_list = ", deleted_list)
    #TODO: не обработана ситуация, если удалены все строки в файле и в листе с новыми значениями
    if check_is_file_empty(filelist, selected_file_num) == 0 and not(inserted_list):
        print("No items found!")
    else:
        try:
            file = open(filelist[selected_file_num], "r")
            i = 0
            for linenum, line in enumerate(inserted_list):
                if linenum + START_WITH_ZERO in deleted_list:
                    i += 1
                else: 
                    print("{0}:  {1}".format(linenum - i, line))
            for linenum, line in enumerate(file):
                if linenum + START_WITH_ZERO + i in deleted_list:
                    i += 1
                else:
                    print("{0}:  {1}".format(linenum - i, line), end="")
            print("")
        except FileNotFoundError as err:
            print(err)
        finally: 
            file.close()

def add_line(inserted_list, deleted_list):
    line = input("Add item:")
    if line:
        inserted_list.insert(0, line)
        deleted_list = [num + 1 for num in deleted_list]
    return inserted_list, deleted_list

def delete_line(deleted_list, START_WITH_ZERO):
    print("Start delete_line", deleted_list)
    line = int(input("Delete item number (or " + str(START_WITH_ZERO - 1) + " to cancel):"))
    if str(line) and line != START_WITH_ZERO - 1:
        #TODO: Валидация существования данной строки
        if not deleted_list:
            print("deleted_list is empty, added one element")
            deleted_list.append(int(line))
        else:
            """ Алгоритм:
                1. Проверяем меньше или равен ли номер выбранного элемента, любому элементу в массиве
                2. Если таких элементов нет, то вставляем элемент как есть
                3. Если да, то увеличиваем все элементы в списке на 1, и убираем из списка элемент, на котором остановились в п.1
                4. Повторяем пункт 1
            """
            print("deleted list is not empty")
            dummy_list = deleted_list.copy()
            print("DUMMY_LIST:", dummy_list)
            i = 0
            while 0 <= i <= (len(dummy_list) - 1):
                if line >= dummy_list[i]:
                    del dummy_list[i]
                    line += 1
                    i = 0
                else:
                    i += 1
            print("line to append: ", line)
            print("deleted_list before append: ", deleted_list)
            deleted_list.append(int(line))
    else:
        print("check not passed")
    print(deleted_list)
    return deleted_list

def insert_items(filelist, selected_file_num, inserted_list):
    try:
        file = open(filelist[selected_file_num], "r+")
        readcontent = file.read()
        file.seek(0, 0)
        for item in inserted_list:
            file.write(str(item) + "\n")
        file.write(readcontent)
        file.close()
    except FileNotFoundError as err:
        print(err)
    finally:
        file.close()

def delete_items(filelist, selected_file_num, inserted_list, deleted_list):
    try:
        file = open(filelist[selected_file_num], "r+")
        lines = file.readlines()
        file.close()
        file = open(filelist[selected_file_num], "w")
        for num, line in enumerate(lines):
            if num + 1 in deleted_list:
                pass
            else:
                file.write(line)
    except FileNotFoundError as err:
        print(err)
    finally:
        file.close()

def save(filelist, selected_file_num, inserted_list, deleted_list):
    key = ""
    while not(key):
        key = input("Save changes? [y/n]:")
        if key:
            if len(key) == 1:
                if key in "yY":
                    insert_items(filelist, selected_file_num, inserted_list)
                    delete_items(filelist, selected_file_num, inserted_list, deleted_list)
                    inserted_list = []
                    deleted_list = []
                    print("Changes successfully saved!")
                elif key in "nN":
                    inserted_list = []
                    deleted_list = []
                    print("Changes not saved!")
            else:
                key = ""
        return inserted_list, deleted_list            
            

def prompt_input(current_mode, filelist, START_WITH_ZERO, selected_file_num, inserted_list, deleted_list, default_key):
    FILELIST_MENU = "[A]dd  [Q]uit  [{default_key}]:"
    FILE_MENU = "[A]dd{DELETE}{SAVE}  [Q]uit  [{default_key}]:"
    if current_mode == "FILELIST":
        default_key = "a"
        menu_string = FILELIST_MENU.format(**locals())
        user_key = input(menu_string)
        user_key = default_key if not user_key else user_key
        if len(user_key) == 1 and user_key in 'Qq':
            sys.exit()
        elif len(user_key) == 1 and user_key in 'Aa':
            add_file(filelist)
        else:
            try:
                user_key = int(user_key)
                if filelist and user_key in range(START_WITH_ZERO, len(filelist) - 1 + START_WITH_ZERO):
                    current_mode = "FILE"
                    selected_file_num = user_key - START_WITH_ZERO
                else:
                    raise UserKeyError            
            except ValueError:
                print("ERROR: invalid choice--enter one of 'AaQq' or file number to edit content")
                while user_key:
                    user_key = input("Press Enter to continue:")
            except UserKeyError:
                print("ERROR: invalid choice--enter one of 'AaQq' or file number to edit content")
                while user_key:
                    user_key = input("Press Enter to continue:")
    elif current_mode == "FILE":
        DELETE = "" if check_is_file_empty(filelist, selected_file_num) == 0 else "  [D]elete"
        SAVE = "" if not inserted_list and not deleted_list else "  [S]ave"
        default_key = "a" if not default_key else default_key
        menu_string = FILE_MENU.format(**locals())
        user_key = input(menu_string)
        user_key = default_key if not user_key else user_key
        try:
            if len(user_key) == 1 and user_key in 'Qq':
                inserted_list, deleted_list = save(filelist, selected_file_num, inserted_list, deleted_list)
                selected_file_num = -1
                current_mode = "FILELIST"
            elif len(user_key) == 1 and user_key in 'Aa':
                inserted_list, deleted_list = add_line(inserted_list, deleted_list)
            elif len(user_key) == 1 and user_key in 'Dd' and DELETE:
                print("DELETED_LIST before:", deleted_list)
                deleted_list = delete_line(deleted_list, START_WITH_ZERO)
                print("DELETED_LIST after:", deleted_list)
            elif len(user_key) == 1 and user_key in 'Ss' and SAVE:
                inserted_list, deleted_list = save(filelist, selected_file_num, inserted_list, deleted_list)
            else:
                raise UserKeyError
        except UserKeyError:
            print("ERROR: invalid choice--enter one of 'Aa{0}{1}Qq'".format("Dd" if DELETE else "", "Ss" if SAVE else ""))
            while user_key:
                user_key = input("Press Enter to continue:")
    return current_mode, selected_file_num, inserted_list, deleted_list



main()