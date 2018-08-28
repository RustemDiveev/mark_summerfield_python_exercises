import sys
import unicodedata

def print_unicode_table(words):
    print("decimal   hex   chr   {0:^40}".format("name"))
    print("-------  -----  ---   {0:-<40}".format(""))

    code = ord(" ")
    end = sys.maxunicode

    while code < end: 
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        # тоже так себе конечно, два раза повторяется одно и тоже
        if words is None: 
            printCheck = 1
        else:
            printCheck = 1
            for i in words:
                if i in name.lower():
                    printCheck *= 1
                else:
                    printCheck *= 0
        if printCheck == 1:
            print("{0:7}  {0:5x}  {0:^3c} {1}".format(code, name.title()))   
        code += 1   

words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [word1] [word2] ... [wordn]".format(sys.argv[0]))
        # так себе решение
        words = 0
    else:
        argCount = len(sys.argv)
        i = 1
        while i < argCount: 
            words.append(sys.argv[i].lower())
            i += 1
if words != 0:
    print_unicode_table(words)