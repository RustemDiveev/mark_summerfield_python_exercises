#
import os
import sys

""" Может принимать два значения: 
    FILELIST - меню списка файлов 
    FILE     - меню файла 
"""
current_mode = "FILELIST" 

""" Флаг старта программы """
start_flg = 0

""" Список файлов с расширением lst в текущей директории """
filelist = []

""" Клавиша по умолчанию (возможно не константа) """
DEFAULT_KEY = "a"

""" Список не сохраненных значений, 
    каждый элемент - кортеж вида ("INSERT", "BLABLABLA") или ("DELETE", "1") 
    - описывает действия с файлом при его сохранении 
"""
nonsaved_values = []

""" Индекс открытого файла из filelist, -1, если ни один файл не открыт """
fileopened = -1

""" Является ли файл пустым, -1 нет информации, 0 - пустой, 1 - не пустой """
fileempty = -1

def main():
    global start_flg
    global filelist
    while True:
        if start_flg == 0 and current_mode == "FILELIST":
            print_line("List Keeper")
            filelist = print_filelist()
            print_filelist_menu()
            start_flg = 1
        user_input_prompt()
        
def print_line(heading):
    print("{0:-^70}".format(heading))

def print_filelist(extension="lst"):
    filelist = os.listdir()
    filelist = [file for file in filelist if len(file.split(".")) > 1 and file.split(".")[1] == extension]
    if len(filelist) == 0:
        print_line("No files found")
    else:
        for num, file in enumerate(filelist):
            print("[{0}]   {1}".format(num, file))
    return filelist

def print_filelist_menu(default_key="a"):
    print("[A]dd  [Q]uit  [{0}]:".format(default_key), end="")

def print_file_menu():
    save = "" if len(nonsaved_values) == 0 else "[S]ave  "
    delete = "" if fileempty == 0 else "  [D]elete" 
    print("[A]dd{0}  {1}[Q]uit  [{2}]:".format(delete, save, DEFAULT_KEY), end="")

def add_file(extension="lst"):
    print("Enter new file name: ", end="")
    filename = str(input()).strip().lower()
    if len(filename.split(".")) > 1 and filename.split(".")[-1] == extension:
        pass
    else: 
        filename += "." + extension        
    
    new_file = open(filename, "w")
    new_file.close()

def check_is_file_empty(fileopened):
    try:
        file = open(filelist[fileopened], "r")
        i = 0
        for line in file:
            if i == 0:
                pass
            else:
                break
            i += 1
    except FileExistsError as err:
        print(err)
    finally:
        file.close()
    return i 

def print_file(fileopened):
    global fileempty
    print_line("List Keeper")
    if check_is_file_empty(fileopened) > 0:
        fileempty = 1
        try:
            file = open(filelist[fileopened], "r")
            for linenum, line in enumerate(file):
                print("{0}:  {1}".format(linenum + 1, line), end="")
        except FileNotFoundError as err:
            print(err)
        finally:
            file.close()
    else: 
        fileempty = 0
        print_line("No items found")
    print("")
    print_file_menu()

def add_line():
    global nonsaved_values
    line = input("Add item:")
    if len(line) > 0:
        t = "INSERT", line
        nonsaved_values.append(t)
        return 1
    else:
        return 0

def delete_line():
    global nonsaved_values
    line = input("Delete item number (or 0 to cancel):")
    try:
        line = int(line)
        if line == 0:
            # Пользователь отменил удаление
            return 0    
        else:
            t = "DELETE", line - 1
            nonsaved_values.append(t)
            # Пользователь выполнил удаление
            return 1
    except ValueError as err:
        print("ERROR: Wrong input. Enter item number or 0 to cancel")

def prompt_save():
    pass

def user_input_prompt():    
    global current_mode
    global fileopened
    global filelist
    line = input()
    line = DEFAULT_KEY if len(line) == 0 else line
    line = str(line).strip()
    # Меню файлов
    if current_mode == "FILELIST":
        if len(line) == 1 and line in "Qq":
            sys.exit()
        elif len(line) == 1 and line in "Aa":
            add_file()
        elif len(filelist) > 0:
            try:
                line = int(line)
                if line in range(0, len(filelist)):
                    current_mode = 'FILE'
                    fileopened = int(line)
                    print_file(fileopened)
            except ValueError:
                print("ERROR: invalid choice--enter one of 'AaQq' or select file by its number")
    elif current_mode == "FILE":
        if len(line) == 1 and line in 'Qq':
            current_mode = "FILELIST"
            print_line("List Keeper")
            filelist = print_filelist()
            print_filelist_menu()
        elif len(line) == 1 and line in 'Aa':
            status = add_line()
        elif len(line) == 1 and line in 'Dd':
            delete_line()
        elif len(line) == 1 and line in 'Ss':
            prompt_save()
        else:
            print("ERROR: invalid choice--enter one of 'AaDdSs' or enter 'Qq' to quit to file menu")

main()
