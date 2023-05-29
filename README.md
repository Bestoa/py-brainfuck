# py-brainfuck
Tiny brainfuck interpreter with pure Python3

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/5c06098a2ab540a5979b8d743f5d97c9)](https://app.codacy.com/gh/Bestoa/py-brainfuck/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

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
