# importing random package for library
import random

# function reads input and checks if it is number
# msg - input, minimum - min possible value, default - default value
def get_int(msg, minimum, default):
    # try to read till good input value
    while True:
        try:
            # read input into line
            line = input(msg)
            # if line is empty and default is not return default
            if not line and default is not None:
                return default
            # try to convert to int
            i = int(line)
            # if i is lesser then print
            if i < minimum: 
                print("must be >=", minimum)
            else:
                return i
        # not convertable int
        except ValueError as err:
            print(err)

# read input params
rows = get_int("rows: ", 1, None)
columns = get_int("columns: ", 1, None)
minimum = get_int("minimum: (or Enter for 0): ", -1000000, 0)

default = 1000
if default < minimum:
    default = 2 * minimum
maximum = get_int("maximum (or Enter for " + str(default) + "): ", minimum, default)

# print output
row = 0 
while row < rows:
    line = ""
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)
        s = str(i)
        while len(s) < 10:
            s = " " + s
        line += s
        column += 1
    print(line)
    row += 1



