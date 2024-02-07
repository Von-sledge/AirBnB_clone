#!/usr/bin/python3
"""This contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """cli - command line interface class"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """to exit the program"""
        return True

    def do_EOF(self, line):
        "Exit command at End of File"
        print("")
        return True

    def do_emptyline(self):
        """Custom empty line + Enter does not execute anything"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
