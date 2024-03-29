'''Brainfuck interpreter'''

VERSION = '0.2.0.20240221'

def __static_vars():
    '''Decorate, add static attr'''
    def decorate(func):
        '''The decorate'''
        setattr(func, 'stdin_buffer', [])
        return func
    return decorate

@__static_vars()
def __getchar() -> int:
    '''Return one char from stdin'''
    buffer_len = len(__getchar.stdin_buffer)
    if buffer_len == 0:
        __getchar.stdin_buffer = list(input().encode('ascii'))
        __getchar.stdin_buffer.append(10) # We need this enter to compact getchar from libc.
    ret_c, __getchar.stdin_buffer = __getchar.stdin_buffer[0], __getchar.stdin_buffer[1:]
    return ret_c

def __count_same_op(code: str, ptr: int, end: int) -> int:
    n = 1
    while code[ptr + n] == code[ptr] and ptr < end:
        n += 1
    return n

def __pre_execute(raw_code: str) -> list:
    '''JIT'''
    iptr = 0
    code = list()
    raw_code_len = len(raw_code)
    while iptr < raw_code_len:
        if (raw_code[iptr] == '>') or (raw_code[iptr] == '<') or (raw_code[iptr] == '+') or (raw_code[iptr] == '-'):
            n = __count_same_op(raw_code, iptr, raw_code_len);
            code.append([raw_code[iptr], n])
            iptr += n
        else:
            code.append([raw_code[iptr], ''])
            iptr += 1

    iptr = 0
    bracket = list()
    code_len = len(code)
    while iptr < code_len:
        if code[iptr][0] == '[':
            bracket.append(iptr)
        elif code[iptr][0] == ']':
            piptr = bracket.pop()
            code[piptr][1], code[iptr][1] = iptr, piptr
        iptr += 1
    bracket_len = len(bracket)
    if bracket_len != 0:
        code = []
    return code

def __execute(code: list, stack_size: int) -> list:
    '''Run bf code'''
    iptr = 0
    sptr = 0
    stack = list(0 for _ in range(stack_size))
    code_len = len(code)
    while iptr < code_len:
        instruction = code[iptr][0]
        if instruction == '>':
            sptr += code[iptr][1]
        elif instruction == '<':
            sptr -= code[iptr][1]
        elif instruction == '+':
            stack[sptr] += code[iptr][1]
            if stack[sptr] > 255:
                stack[sptr] -= 256
        elif instruction == '-':
            stack[sptr] -= code[iptr][1]
            if stack[sptr] < 0:
                stack[sptr] += 256
        elif instruction == '.':
            print(chr(stack[sptr]), end='')
        elif instruction == ',':
            stack[sptr] = __getchar()
        elif instruction == '[' and stack[sptr] == 0:
            iptr = code[iptr][1]
        elif instruction == ']' and stack[sptr] != 0:
            iptr = code[iptr][1]
        iptr += 1
    # Clean the buffer, otherwise it will affect next round result.
    __getchar.stdin_buffer = []
    return stack

def run(raw_code: str = '', stack_size: int = 128) -> list:
    '''Interpreter the raw_code.
    Input:
        - raw_code: the string of brainfuck code.
                    if this is empty, program will wait for user input.
        - stack_size: the size of stack, default is 128Bytes.
    Return value:
        - The whole stack.
    '''
    if raw_code == '':
        raw_code = input('% ')
    code = __pre_execute(raw_code)
    return __execute(code, stack_size)
