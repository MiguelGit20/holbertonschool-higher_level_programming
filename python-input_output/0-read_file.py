#!/usr/bin/python3
""" 
Module that contains a function
that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read())