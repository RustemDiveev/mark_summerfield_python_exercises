#
import os 
import sys

""" Файл, над которым проводятся работы"""
FILE_NAME = "mngmt.txt"

""" Список с вставляемыми строками """
inserted_list = []

""" Список с номерами удаляемых строк """
deleted_list = []

def main():
    while True:
        Print_Header()
        Print_Content()
        prompt_input()         

def Print_Content():
    try:
        file = open(FILE_NAME, 'r')
        i = 0
        for linenum, line in enumerate(inserted_list):
            if linenum + 1 in deleted_list:
                pass 
            else:
                i += 1
                print("{0}:  {1}".format(i, line))
        for linenum, line in enumerate(file):
            if linenum + 1 + i in deleted_list:
                pass
            else:
                i += 1
                print("{0}:  {1}".format(i, line), end="")
        print("")
    except FileNotFoundError as err:
        print(err)
    finally:
        file.close()

def Print_Menu():
    save = "" if not inserted_list and not deleted_list else "[S]ave  "
    output = "{0}{1}{2}{3}:".format("[A]dd  ", save, "[D]elete  ", "[Q]uit")
    return output

def Print_Header():
    print("Programm Heading")

def add_line():
    global deleted_list
    global inserted_list
    line = input("Enter new item:")
    if line:
        inserted_list.insert(0, line)
        deleted_list = [num + 1 for num in deleted_list]  

def delete_line():
    global deleted_list 
    line = input("Enter line number to delete:")
    if line:
        if deleted_list:
            deleted_list = [item + 1 for item in deleted_list]
        deleted_list.append(int(line))

def insert_items():
    file = open(FILE_NAME, "r+")
    readcontent = file.read()
    file.seek(0, 0)
    for item in inserted_list:
        file.write(str(item) + "\n")
    file.write(readcontent)
    file.close()
        
def delete_items():
    file = open(FILE_NAME, "r")
    lines = file.readlines()
    file.close()
    file = open(FILE_NAME, "w")
    for num, line in enumerate(lines):
        if num + 1 in deleted_list:
            pass
        else:
            file.write(line)
    file.close()

def save():
    global inserted_list
    global deleted_list
    key = input("Save changes? [y/n]:")
    if key:
        if len(key) == 1:
            if key in "yY":
                insert_items()
                delete_items()
                inserted_list = []
                deleted_list = []
                print("Changes saved!", end="")
            elif key in "nN":
                pass
        
def prompt_input():
    key = input(Print_Menu())
    if len(key) == 1:
        if key in "Qq":
            sys.exit()
        elif key in "Aa":
            add_line()
        elif key in "Dd":
            delete_line()
        elif key in "Ss" and inserted_list and deleted_list:
            save()
    else:
        input("Wrong output!")
    
main()

