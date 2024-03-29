#!/usr/bin/python3
"""This contains the entry point of the command interpreter"""
import cmd
import models
from models.user import User
from models.base_model import BaseModel
import re
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """cli - command line interface class"""
    prompt = "(hbnb) "
    hbnb_class = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        "Exit command at End of File"
        return True

    def do_emptyline(self):
        """Custom empty line + Enter does not execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance and saves to JSON file"""
        new_comm = self.parseline(line)[0]
        if new_comm is None:
            print("** class name missing **")
        elif new_comm[0] not in self.hbnb_class:
            print("** class doesn't exist **")
        else:
            update = eval(new_comm)()
            update.save()
            print(update.id)

    def do_show(self, line):
        """Prints string representation based on class name"""
        new_comm = self.parseline(line)[0]
        obj_id = self.parseline(line)[1]
        if new_comm is None:
            print("** class name missing **")
        elif new_comm[0] not in self.hbnb_class:
            print("** class doesn't exist **")
        elif obj_id == "":
            print("** instance id missing **")
        else:
            cls_id = models.storage.all().get(new_comm + "." + obj_id)
            if cls_id is None:
                print("** no instance found **")
            else:
                print(cls_id)

    def do_destroy(self, line):
        """Deletes an instance based on class name and id"""
        cls_name = self.parseline(line)[0]
        obj_id = self.parseline(line)[1]
        if cls_name is None:
            print("** class name missing **")
        elif cls_name not in self.hbnb_class:
            print("** class doesn't exist **")
        elif obj_id == "":
            print("** instance id missing **")
        else:
            cls_id = models.storage.all().get(new_comm + "." + obj_id)
            if cls_id is None:
                print("** no instance found **")
            else:
                del models.storage.all()[new_comm + "." + obj_id]
                models.storage.save()

    def do_all(self, line):
        """Prints all string representation based on class name/otherwise"""
        cls_name = self.parseline(line)[0]
        save = models.storage.all()
        if cls_name is None:
            print([str(save[obj]) for obj in save])
        elif cls_name in self.hbnb_class:
            keys = save.keys()
            print([str(save[key]) for key in keys if key.startswith(command)])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id\
           by adding or updating attribute\
           (save the change into the JSON file)
        """
        args = self.parseline(line)
        args_size = len(args)
        objdict = storage.all()

        if args_size == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.hbnb_class:
            print("** class doesn't exist **")
            return False
        if args_size == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if args_size == 2:
            print("** attribute name missing **")
            return False
        if args_size == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if args_size == 4:
            obj = objdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                value = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = value(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            obj_type = obj.__class__.__dict__.keys()
            for key, value in eval(argl[2]).items():
                if (key in obj_type and type(obj.__class__.__dict__[key])
                        in {str, int, float}):
                    value_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = value_type(value)
                else:
                    obj.__dict__[key] = value
        storage.save()

    def do_count(self, line):
        """Retrieve the number of instances of a given class"""
        command = self.parseline(line)[0]
        count = 0
        for obj in storage.all().values():
            if command == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
