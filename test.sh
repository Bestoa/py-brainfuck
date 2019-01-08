#!/bin/bash

pip3 list
python3 setup.py sdist && pip3 install -U dist/*.gz && python3 -m pytest -v
