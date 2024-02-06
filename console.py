#!/usr/bin/python3
'''Python Interpreter.'''

import cmd
'''The cmd module'''


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()