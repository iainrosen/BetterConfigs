#!/bin/bash
rm -rf dist/*
#/usr/bin/python3 -m pip install --upgrade build
/usr/bin/python3 -m build
#/usr/bin/python3 -m pip install --upgrade twine
#/usr/bin/python3 -m twine upload dist/*