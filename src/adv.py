from room import Room
from player import Player
from item import Item

# Declare all the rooms
# room is a dict with keys (name of room) and values (Room instance "object")

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

item = {
    'stick':  Item("stick", "a stick! Great for poking people in the eye!"),

    'rock':    Item("rock", """a rock! The rock looks oddly like Chuck Norris..."""),

    'bacon': Item("bacon", """bacon!!!!!!! Oh wait... it doesn't looked cooked. *sad face*"""),

    'sword':   Item("sword", """a sword! You have found the mighty Excalibur!!!!!\nYou notice a marking on the bottom:\nMade in China"""),

    'gold': Item("gold", """gold! The gold is small but it should be worth something..."""),
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

# Adding items to a rooms
room['outside'].contents = []
room['foyer'].contents = [item['rock'], item['stick']]
room['overlook'].contents = [item['sword']]
room['narrow'].contents = [item['stick']]
room['treasure'].contents = [item['bacon'], item['gold']]

x = room['foyer'].contents.index(item['stick'])
print(x)

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

# User input for player's name
player_name = input(f'What is your name, Adventurer?: ')

# Initializes a new player instance
player = Player(player_name, room['outside'])

print(f"\nWelcome {player_name}! Embark on a journey with us to new lands!")
print(f"*flashes occur*")
print(f"{player_name} suddenly gets dropped right outside of a cave.")


def add_item(player, item_name):
    try:
        print('player', player)
        print('current room contents', player.current_room.contents)
        print('type of contents', type(player.current_room.contents))
        index = player.current_room.contents.index(item[item_name])
        print(index)
    # except:
    #     print('something went wrong :(')
    # print(item[item_name], 'testing')
    # print(item.item_name, 'this works')

    # try:
    #     print(item.item_name, 'this works')
    #     player.inventory.append(item[item_name])
    #     player.current_room.contents.remove(item[item_name])
    # except:
    #     print(f"'{item_name}' not found.")


def remove_item(player, item_name):
    try:
        player.current_room.contents.append(item.item_name)
        player.inventory.remove(item.item_name)
    except:
        print(f"'{item_name}' not found.")


    # Starts game loop
while True:
    print(f"\n==========================================================================================================")
    print(f"\n{player.name} is currently at the {player.current_room.name}")
    print(f"{player.current_room.description}\n")

    user_input = input(f" - Enter a command: ")

    command = user_input.split()

    if len(command) <= 1:
        # Player quits game
        if user_input == 'q':
            break
        # Check inventory
        elif user_input == 'i' or user_input == 'inventory':
            print(f"\n{player.name} opens their inventory.")
            if len(player.inventory) == 0:
                print(f'{player.name} has no items yet.')
            else:
                print(f'{player.name} has:\n{player.inventory}')
        elif user_input == 'look':
            print(f"\n{player.name} looks around {player.current_room.name}.")
            if len(player.current_room.contents) == 0:
                print(f"There doesn't seem to be anything here.")
            else:
                print(
                    f"{player.name} found something.\n{player.current_room.name} currently contains {player.current_room.contents}")

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
        elif user_input == 'commands' or user_input == 'help':
            print(f"""
            \n - Help | Commands
            \n --------------------------------------------------------------------
            \n - q = Quit Game
            \n
            \n - Directions
            \n --------------------------------------------------------------------
            \n - n = move North
            \n - w = move West
            \n - s = move South
            \n - e = move East
            \n
            \n - Actions
            \n --------------------------------------------------------------------
            \n - i | inventory = Look at inventory
            \n - get <item> | take <item> = Adds item to inventory
            \n - drop <item> = Drops item from inventory
            \n - look = Looks for items (displays a list of available items)
            """)
        else:
            print(
                f"\n - {user_input} is currently not a valid input.\n - Try typing help or commands \n")

    # Actions
    elif len(command) == 2:
        item = command[1]

        if command[0] == 'get' or command[0] == 'take':
            # Add item to player's inventory
            print(item, 'item')
            add_item(player, item)
            pass
        elif command[0] == 'drop':
            # Remove item from player's inventory
            remove_item(player, item)
            pass
        else:
            print(
                f"\n - {user_input} is currently not a valid input.\n - Try typing help or commands \n")

    # Invalid input
    else:
        print(
            f"\n - {user_input} is currently not a valid input.\n - Try typing help or commands \n")
