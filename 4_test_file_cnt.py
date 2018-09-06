#
import os 
import sys

def main():
    while True:
        line = input()
        try:
            if line in "qQ":
                sys.exit()
            file = open(line, "r")
            print("{0} contains {1} rows".format(line, file_row_count(file)))
        except FileNotFoundError as err:
            print(err)
        finally:
            file.close()

def file_row_count(file):
    i = 0
    for line in file:
        if i == 0:
            pass
        else:
            break
        i += 1
    return i 

main()