#!/usr/bin/python3
'''Python Interpreter.'''

from models.base_model import BaseModel
'''Import module.'''


class City(BaseModel):
    '''
    The class represents a city in the application.

    It inherits from the BaseModel class.
    '''
    state_id = ""
    name = ""
