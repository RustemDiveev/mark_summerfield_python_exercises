#
import cmath
import math
import sys

# Function loops until user enters valid floating-point number
# and accepts 0 if allow_zero is True
def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
    return x

print("ax^2 + bx + c = 0")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)

x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = -(b / (2 * a))
else: 
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else: #discriminant < 0
        root = cmath.sqrt(discriminant)
    #x1 = (-b + root) / (2 * a)
    #x2 = (-b - root) / (2 * a)
    x1 = (root - b) / (2 * a)
    x2 = (-root - b) / (2 * a)

equation = ("{a}x^2 + {b}x + {c} = 0"
            " -> x = {x1}").format(**locals())
if x2 is not None:
    equation += " or x = {x2}".format(**locals())
print(equation)