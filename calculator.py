import re
from pprint import pprint

run = True
previous = 0

def perform_maths():
    global run
    global previous

    equation = ''
    if previous == 0:
        equation = input("Enter your equation:")
    else:
        equation = input(str(previous))

    if equation == "Quit":
        pprint("Goodbye then!")
        run = False
    else:
        equation = re.sub('[^0-9-+*/%.]', '', equation)

        if previous == 0:
            previous = eval(str(equation))
        else:
            previous = eval(str(previous) + equation)

while run:
    perform_maths()
