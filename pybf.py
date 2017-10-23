#!/usr/bin/env python3
def pre_execute(code: list):
    cp = 0
    bracket = list()
    while (cp < len(code)):
        if (code[cp] == '['):
            bracket.append(cp)
        elif (code[cp] == ']'):
            previous = bracket.pop()
            code[previous] = cp
            code[cp] = -previous
        cp += 1
    if (len(bracket) != 0):
        raise

def execute(code: list):
    cp = 0
    sp = 0
    stack = list(0 for _ in range(512))
    while (cp < len(code)):
        if (code[cp] == '>'):
            sp += 1
        elif (code[cp] == '<'):
            sp -= 1
        elif (code[cp] == '+'):
            stack[sp] += 1
        elif (code[cp] == '-'):
            stack[sp] -= 1
        elif (code[cp] == '.'):
            print(chr(stack[sp]), end='')
        elif (code[cp] == ','):
            stack[sp] = input().encode('ascii')[0]
        elif (code[cp] > 0 and stack[sp] == 0):
            cp = code[cp]
        elif (code[cp] < 0 and stack[sp] != 0):
            cp = -(code[cp])
        cp += 1
    print("RET(stack[0]) = %d" % stack[0])

if __name__ == '__main__':
    code = input()
    code = list(code)
    pre_execute(code)
    execute(code)
