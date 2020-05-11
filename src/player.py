# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Items


class Player:
    def __init__(self, name, location, *args):
        self.name = name
        self.location = location
        self.inventory = []

    def __str__(self):
        return f"{self.name} is currently in room {self.location}"

    def move_to_room(self, next_room):
        self.location = next_room

    def get_item(self, item_name):
        self.inventory.append(item_name)
        self.location.remove_item(item_name)
        print(f"Nice work, {item_name.name} added!")

    def drop_item(self, item_name):
        self.inventory.remove(item_name)
        self.location.items.append(item_name)
        print("Item dropped.")

    def print_items(self):

        if len(self.inventory) > 0:
            item_names = [item.item_name() for item in self.inventory]
            print("Your items:", end=" ")
            print(*item_names, sep=', ', end='\n')

        else:
            print("No items yet.")
