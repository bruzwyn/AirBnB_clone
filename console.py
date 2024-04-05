#!/usr/bin/env python3
"""
Module that contains the entry of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """class defination of the consol
    """

    prompt = '(hbnb) '

    model_classes = ['BaseModel', 'User', 'State', 'Amenity',
                     'City', 'Place', 'Review']

    cmds = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def do_quit(self, line):
        """ quits the program
        """

        return True

    def do_EOF(self, line):
        """exits the program when end of file is reached
        """
        print('')

        return True

    def help_help(self):
        """ used to show description of command called"""

        print("Describes a given command")

    def emptyline(self):
        """doesn't execute anything when empty line is entered
        """

        pass

    def precmd(self, arg):
        """
        used to process the command before they are executed
        """

        if '.' in arg and '(' in arg and ')' in arg:
            model_class = arg.split('.')
            cm1 = model_class[1].split('(')
            cm2 = cm1[1].split(')')
            if model_class[0] in HBNBCommand.model_classes and \
                    HBNBCommand.cmds:
                arg = cm1[0] + ' ' + model_class[0] + ' ' + cm2[0]
        return arg

    def do_create(self, arg):
        """ creates a new instance of BaseModel
        """

        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.model_classes:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'Amenity': Amenity, 'City': City, 'Place': Place,
                   'Review': Review}
            myModel = dct[arg]()
            print(myModel.id)
            myModel.save()

    def do_count(self, arg):
        """
        Used to count the number of instances
        """

        count = 0
        objs = storage.all()
        for key, value in objs.items():
            model_class = key.split('.')
            if model_class[0] == arg:
                count = count + 1
        print(count)

    def do_show(self, arg):
        """
        print string representation of instance based on class name
        """

        if not arg:
            print("** class name missing **")
            return
        line = arg.split(' ')
        if line[0] not in HBNBCommand.model_classes:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for key, value in objs.items():
                name = value.__class__.__name__
                obj_id = value.id
                if name == line[0] and obj_id == line[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id
        """

        if not arg:
            print("** class name missing **")
            return
        line = arg.split(' ')
        if line[0] not in HBNBCommand.model_classes:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("**  instance id missing **")
        else:
            objs = storage.all()
            for key, value in objs.items():
                name = value.__class__.__name__
                obj_id = value.id
                if name == line[0] and obj_id == line[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """
        prints all string representation of all instances based on
        or not on the class name
        """
        if not arg:
            print("** class name missing **")
            return

        line = arg.split(' ')
        if line[0] not in HBNBCommand.model_classes:
            print("** class doesn't exist **")
        else:
            objs = storage.all()
            inst_list = [str(obj) for obj in objs.values() if
                         obj.__class__.__name__ == line[0]]
            if len(inst_list) != 0:
                print(inst_list)

    def do_update(self, arg):
        """
        updates instance based on classname and id
        """

        if not arg:
            print("** class name missing **")
            return
        b = ""
        for args in arg.split(','):
            b = b + args
        line = shlex.split(b)
        if line[0] not in HBNBCommand.model_classes:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            for key, value in obj.items():
                name = value.__class__.__name__
                obj_id = value.id
                if name == line[0] and obj_id == line[1].strip('"'):
                    if len(line) == 2:
                        print("** attribute name missing **")
                    elif len(line) == 3:
                        print("** value missing **")
                    else:
                        setattr(value, line[2], line[3])
                        storage.save()
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
