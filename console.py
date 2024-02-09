#!/usr/bin/python3
'''Python Interpreter.'''
import shlex
import re
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models import storage
'''The cmd module'''

my_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
              'Amenity': Amenity, 'City': City,
              'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    '''
    Instantiating a command line interface class.

    The class inherits from cmd.Cmd class in the cmd module.
    '''
    my_intro = "Welcome to my command line for an AirBnB."
    prompt = "(hbnb) "

    def do_help(self, args):
        '''Displays the help command and the documented commands.

        For more info, type help <topic>.
        '''
        print()
        return super().do_help(args)

    def do_quit(self, args):
        '''Quits the program.'''
        return True

    def do_EOF(self, args):
        '''Handling EOF to exit the command line.'''
        print()
        return True

    def emptyline(self):
        '''Function to override emptyline to prevent default activity.'''
        pass

    def do_create(self, args):
        '''Creates a new instance of BaseModel.'''
        args_list = args.split()

        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in my_classes:
            print("** class doesn't exist **")
            return

        new_instance = my_classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        '''Displays the string representation of an instance.'''
        args_list = args.split()

        if not args_list:
            print("** class name missing **")
            return
        class_name = args_list[0]

        if class_name not in my_classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            # Checks if the class name or id is missing
            print("** instance id missing **")
            return

        inst_id = args_list[1]
        key = '{}.{}'.format(class_name, inst_id)
        instance = storage.all().get(key)

        if instance is None:
            print("** no instance found **")
            return
        else:
            print(instance)

    def do_destroy(self, args):
        '''Deletes an instance based on class name and id.'''
        args_list = args.split()

        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in my_classes:
            print("** class doesn't exist **")
            return

        print(count)

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        inst_id = args_list[1]
        key = "{}.{}".format(class_name, inst_id)
        instance = storage.all().get(key)

        if instance is None:
            print("** no instance found **")
            return

        # Deletes the instance and saves the changes
        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        '''
        Prints all str representation of all instances,
        based on or not on the classs name.
        '''
        args_list = args.split()
        objs = storage.all()

        if not args_list:
            print(json.dumps([str(i) for idx, i in objs.items()]))
            return

        class_name = args_list[0]

        if class_name not in my_classes:
            print("** class doesn't exist **")
            return

        print(json.dumps([str(i) for idx, i in objs.items()]))

    def do_update(self, args):
        '''
        Updates an instance based on the class name and id,
        by adding or updating attribute
        '''
        args_list = args.split()

        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in my_classes:
            print("** class doesn't exist **")
            return

        inst_id = args_list[1]
        key = "{}.{}".format(class_name, inst_id)
        new_instance = storage.all().get(key)

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        if new_instance is None:
            print("** no instance found **")
            return

        if len(args_list) < 3:
            print("** attribute name missing **")
            return

        if len(args_list) < 4:
            print("** value missing **")
            return

        a_name = args_list[2]
        a_value = args_list[3]
        setattr(new_instance, a_name, a_value)

    def do_count(self, args):
        '''Retrieves the number of instances of a class.'''
        args_list = args.split()

        class_name = args_list[0]
        if class_name not in my_classes:
            return

        count = storage.count(my_classes[class_name])
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
