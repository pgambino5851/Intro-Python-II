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

player = Player('outside')
# print(player.room)

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

pInput = ''
currentRoom = player.room
# print(room['outside'].description)
# test = getattr(room[player.room], 'n_to').name
# print(test)
directionSet = set("neswq")
# testInput = input("Choose a direction")
# print(set(testInput).issubset(directionSet))
switchedRooms = False

while not pInput == 'q':
    switchedRooms = False
    if player.room == 'outside':
        print("You are outside.")
    else:
        print(f"You are in the {currentRoom}\n")
        print(f'{room[player.room].description}\n')
    # print(room[player.room].description+'.')
    pInput = input("Which direction would you like to move in? N, E, S, W? Press q to quit.\n")

    while set(pInput).issubset(directionSet) == False:
        pInput = input("Your input is not a valid cardinal direction. Which direction would you like to move in? N, E, S, W? Press q to quit.\n")

    if pInput == 'q':
        break
    else:
        pInput += '_to'
    while switchedRooms == False:
        try:
            currentRoom = getattr(room[player.room], pInput).name
            switchedRooms = True
        except AttributeError:
            print(switchedRooms)
            pInput = input("You cannot move that way, please choose a different cardinal direction.\n")
            pInput += '_to'

    if currentRoom == "Outside Cave entrance":
        player.room = 'outside'

    elif currentRoom == 'Foyer':
        player.room = 'foyer'

    elif currentRoom == "Grand Overlook":
        player.room = 'overlook'

    elif currentRoom == "Narrow Passage":
        player.room = 'narrow'

    elif currentRoom == "Treasure Chamber":
        player.room = 'treasure'
    # print(player.room)
    
    
