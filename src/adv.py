from room import Room
from player import Player
from item import Items
import os
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#
# items = {
#     'key':          Items("Mysterious Key", "What will it unlock?"),
#     'map':          Items("map", "Where does it go?"),
#     # 'vase':         Items("vase", "A treasure?"),
#     'birdhouse':    Items("Wooden Birdhouse", "Nice"),
#     'lantern':      Items("Gaslight Lantern", "To help you see"),
#     'chest':        Items("Locked Chest", "What's inside?")
# }

# typeOf to find out what kind of object
# best way to add multiple items to rooms?


# room['outside'].items = [items[k] for k in ('key', 'map')]
room['outside'].items.append(Items('map', 'Where does it go?'))
room['outside'].items.append(Items('key', 'What does it unlock?'))
room['foyer'].items.append(Items('vase', 'A treasure?'))
room['overlook'].items.append(Items('birdhouse', 'Nice'))
room['narrow'].items.append(Items('lantern', 'To help you see'))
room['treasure'].items.append(Items('chest', 'What is inside?'))

# Make a new player object that is currently in the 'outside' room.
player = Player("Tristan", room['outside'])


# print(player)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def print_instructions():
    print("--------------")
    print("*To move, type 'n', 's', 'e', or 'w'")
    print("*To quit, type 'q'")
    print("*To pick up an item, type 'get + item name'")
    print("*To drop an item, type 'drop + item name'")
    print("*To check your inventory, type 'i' or 'inventory'")
    print("*To view these instructions, type '?'")
    print("--------------\n")


print("")
print("Welcome to the Adventure Game!\n")
print_instructions()
print("****Good luck!****\n")

print(f"Current room: {player.location}")
print(f"Room description: {player.location.description}\n")


while True:
    if len(room['outside'].items) == 0 and len(room['foyer'].items) == 0 and len(room['overlook'].items) == 0 and len(room['narrow'].items) == 0 and len(room['treasure'].items) == 0:
        print("")
        print("****You won the game!****\n")
        print("Press 'r' to restart")

    selection = input("Type here: ").lower()
    sep_selection = selection.strip().split(" ")

    if selection == "q":
        print("Thanks for playing")
        break

    try:
        if len(sep_selection) == 1:

            if selection == "?":
                print_instructions()

            elif selection in ["n", "s", "e", "w"]:
                next_room = player.location.get_next_room(selection)

                if next_room:
                    player.move_to_room(next_room)
                    print(
                        f"You are now in {next_room} ... {next_room.description}")
                    player.location.print_items()

                else:
                    print("Can't go that way!")

            elif selection in ["i", "inventory"]:
                player.print_items()

            elif selection == 'r':
                os.execl(sys.executable, sys.executable, *sys.argv)

            else:
                print("Please give a valid input.")

        elif len(sep_selection) == 2:
            verb = sep_selection[0]
            obj = sep_selection[1]

            if verb == "get":
                for item in next_room.items:
                    if obj == item.name:
                        obj = item
                        player.get_item(obj)

                    # error handling prints if there are items that != obj before correct item

            elif verb == 'drop':
                for item in player.inventory:
                    if obj == item.name:
                        obj = item
                        player.drop_item(obj)

            else:
                print("Hmm... try again.")

        else:
            print("Please give valid input")

    except ValueError:
        print("Please enter valid direction")


# below is old way I compared directions to see if true, study this and new way
        # if selection == "n":
        #     if player.location.n_to != None:
        #         player.location = player.location.n_to
        #         print(
        #             f"Moved to room '{player.location}' Description: {player.location.description}")
        #         print(f"Items in room: {player.location.items}")
        #     else:
        #         print("Can't go that way")

        # elif selection == "e":
        #     if player.location.e_to != None:
        #         player.location = player.location.e_to
        #         print(
        #             f"Moved to room '{player.location} Description: {player.location.description}")
        #         print(f"Items in room: {player.location.items}")
        #     else:
        #         print("Can't go that way")

        # elif selection == "s":
        #     if player.location.s_to != None:
        #         player.location = player.location.s_to
        #         print(
        #             f"Moved to room '{player.location}' Description: {player.location.description}")
        #         print(f"Items in room: {player.location.items}")
        #     else:
        #         print("Can't go that way")

        # elif selection == "w":
        #     if player.location.w_to != None:
        #         player.location = player.location.w_to
        #         print(
        #             f"Moved to room '{player.location}' Description: {player.location.description}")
        #         print(f"Items in room: {player.location.items}")
        #     else:
        #         print("Can't go that way")

# to learn more about an item, simply type the item name
