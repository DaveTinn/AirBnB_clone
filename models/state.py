#!/usr/bin/python3
'''Python Interpreter.'''

from models.base_model import BaseModel
'''Import module.'''


class State(BaseModel):
    '''
    Represents a state in the application.

    The class inherits from the BaseModel class.
    '''
    name = ""
