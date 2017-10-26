# coding: utf-8
import sys
import nbfi
from tempfile import TemporaryFile

def test_print_prime():
    result = ''
    with open('demo/print_prime', 'r') as fin:
        with TemporaryFile('w+t') as fout:
            stdin = sys.stdin
            stdout = sys.stdout
            sys.stdin = fin
            sys.stdout = fout
            nbfi.run()
            sys.stdout = stdout
            sys.stdin = stdin
            fout.seek(0)
            result = fout.read()

    with open('tests/except_result', 'r') as f:
        except_result = f.read()
        assert except_result == result

def test_version():
    assert nbfi.VERSION == '0.1.0.1047'
