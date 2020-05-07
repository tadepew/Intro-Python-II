from room import Room
from player import Player

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
while True:
    print(
        f"Current room: {player.location}")
    print(f"Room description: {player.location.description}")
    selection = input("Move rooms by typing 'N', 'E', 'W', or 'S': ")

    if selection == "e":
        print("Thanks for playing")
        break
    try:
        if selection == "N":
            player.location = player.location.n_to
            print(f"Moved to room '{player.location}'")

        elif selection == "E" and player.location.e_to == True:
            player.location = player.location.e_to
            print(f"Moved to room '{player.location}")

        elif selection == "S" and player.location.s_to == True:
            player.location = player.location.s_to
            print(f"Moved to room '{player.location}'")

        elif selection == "W" and player.location.w_to == True:
            player.location = player.location.w_to
            print(f"Moved to room '{player.location}'")

        else:
            print(f"Can't move that way from {player.location}")
    except ValueError:
        print("Please enter valid direction")
