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

# room is a dict with keys (name of room) and values (Room instance "object")
# print("Room after initialization: ", room['outside'])

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# print("Room after linking: ", room['outside'].n_to)
# print("Room after linking: ", room['outside'].s_to)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

player_name = input(f'What is your name, Adventurer?: ')

player = Player(player_name, room['outside'])

print(f"\nWelcome {player_name}! Embark on a journey with us to new lands!")
print(f"*flashes occur*")
print(f"{player_name} suddenly gets dropped right outside of a cave.")

# player.current_room = player.current_room

# print(player.current_room.s_to)

while True:
    print(f"\n==========================================================================================================")
    print(f"\n{player.name} is currently at the {player.current_room.name}\n")
    print(f"{player.current_room.description}\n")

    user_input = input(f" - Enter a command: ")

    # Player quits game
    if user_input == 'q':
        break
    # If possible, moves to next room
    elif user_input == 'n':
        if player.current_room.n_to:
            player.current_room = player.current_room.n_to
        else:
            print(f"\n - There is no room to the North.")
    elif user_input == 'w':
        if player.current_room.w_to:
            player.current_room = player.current_room.w_to
        else:
            print(f"\n - There is no room to the West.")
    elif user_input == 's':
        if player.current_room.s_to:
            player.current_room = player.current_room.s_to
        else:
            print(f"\n - There is no room to the South.")
    elif user_input == 'e':
        if player.current_room.e_to:
            player.current_room = player.current_room.e_to
        else:
            print(f"\n - There is no room to the East.")

    # Invalid input
    else:
        print(
            f"\n - {user_input} is currently not a valid input.\n - Commands: n, w, s, e, or q \n")
