#!/usr/bin/python3
'''Python Interpreter.'''

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
'''
Import modules.
'''


class FileStorage():
    '''
    Instantiating a class FileStorage.

    Serializes instances to a JSON file.
    Deserializes JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects.'''
        return FileStorage.__objects

    def new(self, obj):
        '''Sets in __objects the obj with key <obj class name>.id.'''
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Serializes __objects to the JSON file (path: __file_path).
        '''

        with open(FileStorage.__file_path, "w") as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        '''
        Deserializes the JSON file to __objects.
        '''
        mapped_class = {
            "BaseModel": BaseModel,
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "State": State,
            "Place": Place,
            "Review": Review
        }

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as my_json_file:
            data_deserialized = None

            try:
                data_deserialized = json.load(my_json_file)
            except json.JSONDecodeError:
                pass

            if data_deserialized is None:
                return

            FileStorage.__objects = {
                obj_key: mapped_class[obj_key.split('.')[0]](**obj_value)
                for obj_key, obj_value in data_deserialized.items()}
