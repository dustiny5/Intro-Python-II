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


# Input player name
input_player_name = input('What is your name traveler? ')

# Continue game - Game continues to play until False or break
continue_game = True

# Set the first room
current_loc = room['outside']

while continue_game == True:
    
    # Instantiate Player and print current location
    player = Player(input_player_name, current_loc)
    print(f'\n{current_loc}\n==========\n')

    # Ask user for the direction
    input_direction = input('Where to traveler? Enter n, s, e, w or q(quit): ')

    # Re-enter input until we get 'n' 's' 'e' 'w' or 'q'
    while input_direction not in ['n', 's', 'e', 'w', 'q']:
        input_direction = input('Incorrect. Please enter: n, s, e, w, or q(quit) ')

    # If q then quit and end the game
    if input_direction == 'q':
        print('End Game')
        break

    # Set key to the inputs and values to the attributes
    cardinal_attr = {'n':'n_to', 's':'s_to', 'w':'w_to', 'e':'e_to'}

    # Check if room instance has the attribute
    while hasattr(current_loc, cardinal_attr[input_direction]) == False:
        print('A wall is in your way. Please try again.')
        input_direction = input('Please enter: n, s, e or w or q(quit): \n')

        # If input is 'q' then we quit the game
        if input_direction == 'q':
            print('End Game')
            continue_game = False
            break

    # Update current location by getting the attribute of the previous current location
    else:
        current_loc = getattr(current_loc, cardinal_attr[input_direction])
    