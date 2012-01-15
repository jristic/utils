import re

print('Hello World')


class State:
    NoFound=0
    BeforeDot=1
    AfterDot=2


state = State.NoFound
val = ""
totalVal = 0

f = open('purchases.txt', 'r')
line = f.readline()

while line != '':
    for i in range(len(line)):
        if state == State.NoFound:
            if line[i] == '$':
                state = State.BeforeDot
        elif state == State.BeforeDot:
            if line[i] == '.':
                val = val + '.'
                state = State.AfterDot
            else:
                val = val + line[i]
        elif state == State.AfterDot:
            if re.match("[0-9]", line[i]):
                val = val + line[i]
            else:
                fVal = float(val)
                print("Purchase of: " + val + " dollars. " + str(fVal))
                totalVal += fVal
                print("Running total: " + str(totalVal))
                val = ""
                state = State.NoFound
    
    

    state = State.NoFound
    val = ""
    line = f.readline()

print("Total purchases of: " + str(totalVal) + " dollars.")
