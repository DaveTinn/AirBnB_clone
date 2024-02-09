#!/usr/bin/python3
'''
Python Interpreter
'''

from models.engine import file_storage
'''
Import module.
'''


storage = file_storage.FileStorage()
storage.reload()
