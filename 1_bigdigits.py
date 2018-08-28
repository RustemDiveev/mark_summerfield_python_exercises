import sys

#Lists which graphically represent numbers
#Zero, One and etc
Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]

One =  ["   *   ",
        "  **   ",
        "   *   ",
        "   *   ",
        "   *   ",
        "   *   ",
        "  ***  "]

Two =  ["  ***  ",
        " *   * ",
        " *  *  ",
        "   *   ",
        "  *    ",
        " *     ",
        " ***** "]

Three = ["  ***  ",
         " *   * ",
         "     * ",
         "    *  ",
         "     * ",
         " *   * ",
         "  ***  "]

Four =  ["   *   ",
         "  **   ",
         " * *   ",
         "*  *   ",
         "****** ",
         "   *   ",
         "   *   "]

Five =  [" ***** ",
         " *     ",
         " *     ",
         " ***** ",
         "     * ",
         "     * ",
         " ***** "]

Six =   [" ***** ",
         " *     ",
         " *     ",
         " ***** ",
         " *   * ",
         " *   * ",
         " ***** "]

Seven = [" ***** ",
         "     * ",
         "    *  ",
         "   *   ",
         "  *    ",
         " *     ",
         " *     "]

Eight = ["  ***  ",
         " *   * ",
         " *   * ",
         "  ***  ",
         " *   * ",
         " *   * ",
         "  ***  "]

Nine =  ["  **** ",
         " *   * ",
         " *   * ",
         "  **** ",
         "     * ",
         "     * ",
         "     * "]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try: 
    # Return input param to digits (should be a number)
    digits = sys.argv[1]
    # Row counter, each number consists of 7 rows
    row = 0
    while row < 7: 
        # Declare an empty line
        line = ""
        column = 0
        # We print line by line traversing digits 7 times
        while column < len(digits):
            # get a number by traversing digits (input parameter)
            number = int(digits[column])
            # get a digit
            digit = Digits[number]
            # build a line and add delimiter (double space)
            line += digit[row] + "  "
            # increment column
            column += 1
        print(line)
        row += 1
# No input param
except IndexError:
        print("usage: 1_bigdigits.py <number>")
# Number not found in input parameter
except ValueError as err:
        print(err, "in", digits)        

