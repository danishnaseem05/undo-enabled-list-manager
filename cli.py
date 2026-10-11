from cmd import Cmd

from list_manager import ListManager


class ListManagerCLI(Cmd):
    intro = "Undo-Enabled List Manager. Type 'help' for commands."
    prompt = "\nEnter a Command: "

    def __init__(self):
        super().__init__()
        self.manager = ListManager()

    def emptyline(self):
        """Do nothing when the user enters an empty line"""
        pass

    def print_state(self):
        """Display the current state of the linked list"""

        print("Current list:\n")
        self.do_list("")

    def do_help(self, command):
        """Show command syntax"""
        print("Available commands:\n")
        print("  add <INDEX> <DESCRIPTION>       Insert a task at INDEX.")
        print("  remove <INDEX>                Remove the task at INDEX.")
        print("  edit <INDEX> <DESCRIPTION>      Replace a task's description.")
        print("  move <FROM_INDEX> <TO_INDEX>    Move a task to another index.")
        print("  list                        Display all tasks and indexes.")
        print("  undo                        Undo the most recent operation.")
        print("  help                        Show general or command-specific help.")
        print("  quit                        Exit the program.")


    def do_add(self, arguments):
        """Usage: add <INDEX> <DESCRIPTION>"""

        try:
            index_text, description = arguments.split(maxsplit=1)
            index = int(index_text)
        except ValueError:
            print("\n[ERROR]\nUsage: add <INDEX> <DESCRIPTION>")
            return

        if self.manager.add(description, index):
            print(f"Added task at index {index}.")
            self.print_state()
        else:
            print("\n[ERROR]\nInvalid index.")

    def do_remove(self, arguments):
        """Usage: remove <INDEX>"""

        try:
            index = int(arguments)
        except ValueError:
            print("\n[ERROR]\nUsage: remove <INDEX>")
            return

        if self.manager.remove(index):
            print(f"Removed task at index {index}.")
            self.print_state()
        else:
            print("\n[ERROR]\nInvalid index.")

    def do_edit(self, arguments):
        """Usage: edit <INDEX> <DESCRIPTION>"""

        try:
            index_text, description = arguments.split(maxsplit=1)
            index = int(index_text)
        except ValueError:
            print("\n[ERROR]\nUsage: edit <INDEX> <DESCRIPTION>")
            return

        if self.manager.edit(index, description):
            print(f"Edited task at index {index}.")
            self.print_state()
        else:
            print("\n[ERROR]\nInvalid index.")

    def do_move(self, arguments):
        """Usage: move <FROM_INDEX> <TO_INDEX>"""

        try:
            from_text, to_text = arguments.split()
            from_index = int(from_text)
            to_index = int(to_text)
        except ValueError:
            print("\n[ERROR]\nUsage: move <FROM_INDEX> <TO_INDEX>")
            return

        if self.manager.move(from_index, to_index):
            print(f"Moved task from index {from_index} to {to_index}.")
            self.print_state()
        else:
            print("\n[ERROR]\nInvalid index.")

    def do_list(self, arguments):
        """Usage: list"""

        tasks = self.manager.get_items()

        if not tasks:
            print("The task list is empty.")
            return

        for index, task in enumerate(tasks):
            print(f"{index}: {task}")

    def do_undo(self, arguments):
        """Usage: undo

        Reverse the most recent add, remove, edit, or move operation.
        """

        if self.manager.undo():
            print("Undid the most recent operation.")
            self.print_state()
        else:
            print("There is nothing to undo.")

    def do_quit(self, arguments):
        """Usage: quit

        Exit the program.
        """
        return True


def main():
    ListManagerCLI().cmdloop()


if __name__ == "__main__":
    main()
