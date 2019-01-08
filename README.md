# py-brainfuck
Tiny brainfuck interpreter with pure Python3

[![Build Status](https://travis-ci.org/Bestoa/py-brainfuck.svg?branch=master)](https://travis-ci.org/Bestoa/py-brainfuck)

1. Core code just has ~40 lines.
2. Stack size is flexible, default is 128 Bytes.

## Usage

### cli mode
```shell
python3 -m nbfi
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<++.>+++++++++++++++.>.+++.------.--------.<<+.<.
Hello World!
RET(stack[0]) = 0
```
### import as a module
```python
In [1]: import nbfi

In [2]: nbfi.run('++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<++.>+++++++++++++++.>.+++.------.--------.<<+.<.')
   Hello World!
   RET(stack[0]) = 0
```

## TODO
1. Extend the brainfuck syntax, make it useful.
