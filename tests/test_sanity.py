# coding: utf-8
import sys
import nbfi
import pytest
from tempfile import TemporaryFile

def __run(raw_code: str = '') -> tuple:
    with TemporaryFile('w+t') as fout:
        stdout = sys.stdout
        sys.stdout = fout
        stack = nbfi.run(raw_code)
        sys.stdout = stdout
        fout.seek(0)
        return fout.read(), stack

def test_print_prime():
    result = ''
    with open('demo/print_prime', 'r') as fin:
       stdin = sys.stdin
       sys.stdin = fin
       result, _ = __run()
       sys.stdin = stdin

    with open('tests/except_result', 'r') as f:
        except_result = f.read()
        assert except_result == result

@pytest.mark.timeout(5)
def test_overflow():
    _, stack = __run('+[+]')
    assert stack[0] == 0

def test_version():
    assert nbfi.VERSION == '0.2.0.20240221'
