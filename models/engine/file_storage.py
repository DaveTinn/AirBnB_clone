#!/usr/bin/python3
'''Python Interpreter.'''

import json
import os
from models.base_model import BaseModel
'''
Import modules.
'''

class FileStorage:
    '''
    Instantiating a class FileStorage.
    
    Serializes instances to a JSON file.
    Deserializes JSON file to instances'
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects.'''
        return FileStorage.__objects
    
    def new(self, obj):
        '''Sets in __objects the obj with key <obj class name>.id.'''
        key = '{}.{}'.format(type(obj).__name, obj.id)
        FileStorage.__objects[key] = obj
