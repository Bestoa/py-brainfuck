#!/usr/bin/env python3
'''Brainfuck interpreter'''

def static_vars():
    '''Decorate, add static attr'''
    def decorate(func):
        '''The decorate'''
        setattr(func, 'stdin_buffer', [])
        return func
    return decorate

@static_vars()
def getchar():
    '''Return one char from stdin'''
    if len(getchar.stdin_buffer) == 0:
        getchar.stdin_buffer = list(input().encode('ascii'))
        getchar.stdin_buffer.append(10) # We need this enter to compact getchar from libc.
    ret_c, getchar.stdin_buffer = getchar.stdin_buffer[0], getchar.stdin_buffer[1:]
    return ret_c

def pre_execute(code: list):
    '''Replace the [] with paired code pointer'''
    code_pointer = 0
    bracket = list()
    while code_pointer < len(code):
        if code[code_pointer] == '[':
            bracket.append(code_pointer)
        elif code[code_pointer] == ']':
            previous = bracket.pop()
            code[previous] = code_pointer
            code[code_pointer] = -previous
        code_pointer += 1
    if len(bracket) != 0:
        return True
    return False

def execute(code: list):
    '''Run bf code'''
    code_pointer = 0
    stack_pointer = 0
    stack = list(0 for _ in range(512))
    while code_pointer < len(code):
        if code[code_pointer] == '>':
            stack_pointer += 1
        elif code[code_pointer] == '<':
            stack_pointer -= 1
        elif code[code_pointer] == '+':
            stack[stack_pointer] += 1
            if stack[stack_pointer] == 256:
                stack[stack_pointer] = 0
        elif code[code_pointer] == '-':
            stack[stack_pointer] -= 1
            if stack[stack_pointer] == -1:
                stack[stack_pointer] = 255
        elif code[code_pointer] == '.':
            print(chr(stack[stack_pointer]), end='')
        elif code[code_pointer] == ',':
            stack[stack_pointer] = getchar()
        elif code[code_pointer] > 0 and stack[stack_pointer] == 0:
            code_pointer = code[code_pointer]
        elif code[code_pointer] < 0 and stack[stack_pointer] != 0:
            code_pointer = -(code[code_pointer])
        code_pointer += 1
        #print(code_pointer)
    print("RET(stack[0]) = %d" % stack[0])

def brainfuck_main():
    '''Main function'''
    code = input()
    code = list(code)
    if pre_execute(code):
        print('Stynax error')
        return
    execute(code)

if __name__ == '__main__':
    brainfuck_main()
