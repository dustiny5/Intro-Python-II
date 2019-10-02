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
input_player_name = input('What is your name traveler? ')
continue_game = True
desc = 'outside'

while continue_game == True:
    
    current_loc = room[desc]

    player = Player(input_player_name, current_loc)

    # Write a loop that:
    #
    # * Prints the current room name
    print(f'\n{current_loc}\n==========\n')
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    #
    input_direction = input('Where to traveler? Enter n, s, e or w: ')
    while input_direction not in ['n', 's', 'e', 'w']:
        input_direction = input('Incorrect. Please enter: n, s, e or w ')
    # If the user enters a cardinal direction, attempt to move to the room there.

    # Dictionary of cardinal direction k,v and v,k
    cardinal_attr = {'n':'n_to', 's':'s_to', 'w':'w_to', 'e':'e_to'}
    cardinal_attr_2 = {'n_to':'n', 's_to':'s', 'w_to':'w', 'e_to':'e'}

    def check_room(input_direction, begin_location=current_loc):
        # Return a list of empty rooms
        no_room = []
        for el in cardinal_attr.values():
            if el not in begin_location.__dict__.keys():
                no_room.append(cardinal_attr_2[el])
        return no_room
            
    no_room = check_room(input_direction)


    # Print an error message if the movement isn't allowed.
    while input_direction in no_room:
        print('A wall is in your way. Please try again. \n')
        input_direction = input('Where to traveler? Enter n, s, e or w: \n')
    else:

        # Get value from the cardinal_attr dictionary and retrieves the attribute from the current room
        cur_room= room[desc].__dict__[cardinal_attr[input_direction]]

        # Update desc from the key in the room dictionary
        desc = [k for k, v in room.items() if v == cur_room][0]
        print(f'\n{cur_room}\n==========\n')

    # Input y to continue the game or q to quit
    input_continue = input('Continue further, enter y or quit, enter q: ')

    # Loop till we get a y or a q
    while (input_continue != 'y') and (input_continue != 'q'):
        input_continue = input('Incorrect. Please enter y to continue or q to quit: ')
    else:
        # If y then goes back to the while loop, line 47
        if input_continue == 'y':
            continue
        # If the user enters "q", quit the game.
        else:
            print('\nEnd of Game\n==========\n')
            continue_game = False
    
