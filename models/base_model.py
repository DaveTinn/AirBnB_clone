#!/usr/bin/python3
'''Python Interpreter.'''

import models
import uuid
from datetime import datetime

'''Import modules.'''


class BaseModel():
    '''
    Instantiating the class BaseModel.

    It defines all common attributes/methods for other classes.
    '''

    def __init__(self, *args, **kwargs):
        '''Initializes the BaseModel instance.'''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) > 0:
            for key, value in kwargs.items():  # Skips special attr
                if key == '__class__':
                    continue
                # Converts str representation of datetime to datetime objects
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                else:
                    setattr(self, key, value)
            return

        models.storage.new(self)

    def __str__(self):
        '''Returns the string representation of the BaseModel instance.'''
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''
        Updates the public instance attribute updated_at,
        with the current datetime.
        '''
        self.updated_at = datetime.now()

        models.storage.save()

    def to_dict(self):
        '''
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        '''
        my_dict = {**self.__dict__}
        my_dict['__class__'] = type(self).__name__

        if 'created_at' in my_dict:
            my_dict['created_at'] = my_dict['created_at'].isoformat()
        if 'updated_at' in my_dict:
            my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
