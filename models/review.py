#!/usr/bin/python3
'''Python Interpreter.'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''
    The class represents a review in the program.
    It inherits from the BaseModel class.
    '''
    place_id = ""
    user_id = ""
    text = ""
