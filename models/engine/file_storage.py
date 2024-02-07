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

    def save(self):
        '''
        Serializes __objects to the JSON file (path: __file_path.
        '''
        p_data = {}
        for key, obj in FileStorage.__objects.items():
            p_data[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as my_file:
            json.dump(p_data, my_file)

    def reload(self):
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as my_json_file:
            data_deserialized = None

            try:
                data_deserialized = json.load(my_json_file)
            except json.JSONDecodeError:
                pass

            mapped_class = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "Amenity": Amenity,
                    "City": City,
                    "State": State,
                    "Place": Place,
                    "Review": Review
            }

            if data_deserialized is None:
                return

            for obj_key, obj_data in data_deserialized.items():
                name_of_class = obj_key.split(',')[0]
                if name_of_class in mapped_class:
                    obj_class = mapped_class[name_of_class]
                    obj_inst = obj_class(**obj_data)
                    FileStorage.__objects[obj_key] = obj_inst
                else:
                    pass
