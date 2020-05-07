# Implement a class to hold room information. This should have name and
# description attributes.

from item import Items


class Room:
    def __init__(self, name, description, *args):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        return f"{self.name}"

    # def print_items(self):

    #     if len(self.items) > 0:

    #         print("Room items: ")

    #         item_names = [item for item in self.items]
    #         print(", " .join(item_names))

    # def

    def get_next_room(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to

    def remove_item(self, item):
        if item:
            self.items.remove(item)

    def print_items(self):
        if len(self.items) > 0:
            item_name = [item.name for item in self.items]
            # for items in self.items:
            print("Room item(s):", end=" ")
            print(*item_name, sep=', ', end='\n')
