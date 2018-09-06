#
import os

while True:
    try:
        line = input("Enter file name: ")
        file = open(line, "r")
        for linenum, line in enumerate(file):
            print("[line={0}] {1}".format(linenum, line))
    except FileNotFoundError as err:
        print("No file found. Try again!")
    except Exception:
        print("Shit happened!")