#!/usr/bin/python3
'''Python Interpreter.'''

from models.base_model import BaseModel
'''
Import module.
'''


class User(BaseModel):
    '''Instantiating a class User that inherits from BaseModel.'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
