#!/usr/bin/python3
"""This contains the entry point of the command interpreter"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """cli - command line interface class"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        "Exit command at End of File"
        print("")
        return True

    def do_emptyline(self):
        """Custom empty line + Enter does not execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance and saves to JSON file"""
        new_comm = self.parseline(line)
        if new_comm is None:
            print("** class name missing **")
        elif new_comm[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(new_comm[0])().id)
            storage.save()

    def do_show(self, line):
        """Prints string representation based on class name"""
        new_comm = self.parseline(line)[0]
        obj_id = self.parseline(line)[1]
        if new_comm is None:
            print("** class name missing **")
        elif new_comm[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif obj_id == "":
            print ("** instance id missing **")
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
        elif cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif obj_id == "":
            print ("** instance id missing **")
        else:
            cls_id = models.storage.all().get(new_comm + "." + obj_id)
            if cls_id is None:
                print("** no instance found **")
            else:
                del cls_id
            models.storage.save()

    def do_all(self, line):
        """Prints all string representation based on class name/otherwise"""
        cls_name = self.parseline(line)[0]
        if cls_name is None:
            print("** class name missing **")
        else:
            print(cls_name)

    def do_update(self, line):
        """Updates an instance based on the class name and id\
           by adding or updating attribute\
           (save the change into the JSON file)
        """


if __name__ == "__main__":
    HBNBCommand().cmdloop()
