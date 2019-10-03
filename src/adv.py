from room import Room
from player import Player
from item import Item

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

# Add items to room
items_ = {
    'foyer': {'Sword':Item('Sword', 'Atk +3'), 
        'Shield':Item('Shield', 'Def +3, Block +2')},
    'overlook': {'Cloak':Item('Cloak', 'Def +2')},
    'narrow': {'Ring':Item('Ring', 'Def +1')},
    'treasure': {'Dagger':Item('Dagger', 'Atk +1 Dex +2')}
}

room['foyer'].add_item(items_['foyer'])
room['overlook'].add_item(items_['overlook'])
room['narrow'].add_item(items_['narrow'])
room['treasure'].add_item(items_['treasure'])

# print(room['foyer'].add_item({'Cloak':Item('Cloak', 'Def +2')}))
# print(room['foyer'].room_item)

# room['foyer'].remove_item('Sword')
# print(room['foyer'])
# player = Player('Dust', room['foyer'])
# player.add_item({'Dagger':Item('Dagger', 'Atk +1 Dex +2')})
# print(player.player_item)
# player.add_item({'Ring':Item('Ring', 'Def +1')})
# print(player.player_item)


# Input player name
input_player_name = input('What is your name traveler? ')

# Continue game - Game continues to play until False or break
continue_game = True

# Set the first room
current_loc = room['outside']

# Instantiate Player
player = Player(input_player_name, current_loc)

while continue_game == True:

    print(f'\n{current_loc}\n==========\n')

    if current_loc.room_item == {}:
        print('No Items\n-----\n')
    else:
        print('Yes Items\n-----\n')
        # Ask user if they want to pick up an item
        item_pick_up = input('Pick up item? Please type item name or enter to continue: ')

        # Loop until we get the right answer
        while (item_pick_up not in current_loc.room_item) and (item_pick_up != ''):
            item_pick_up = input('Wrong item name. Please type item name or enter to continue: ')

        if item_pick_up != '':
            # Add to player inventory
            print(f'Picked-up: {item_pick_up}')

            for k,v in current_loc.room_item.items():
                if item_pick_up == k:
                    print({k:v})
                    player.add_item({k:v})

            # Remove from room
            current_loc.remove_item(item_pick_up)
            print(player.player_item)

        
    # Ask user for the direction
    input_direction = input('Where to traveler? Enter n, s, e, w, i(inventory), or q(quit): ')

    # Re-enter input until we get 'n' 's' 'e' 'w' 'i'or 'q'
    commands = ['n', 's', 'e', 'w', 'i', 'q']

    while input_direction not in commands:
        input_direction = input('Incorrect. Please enter: n, s, e, w, i(inventory), or q(quit): ')
    while input_direction == 'i':
        if player.player_item == {}:
            print('No Inventory')
            input_direction = input('Please enter: n, s, e, w, i(inventory), or q(quit): ')
        elif player.player_item != {}:
            print(player.player_item)
            drop_item = input('Do you want to drop an item? Enter Item name or press enter to continue: ')
            while (drop_item not in player.player_item) and (drop_item != ''):
                drop_item = input('Enter the correct item name or press enter to continue: ')
            if drop_item != '':
                # Add item to room
                for k,v in player.player_item.items():
                    if drop_item == k:
                        print({k:v})
                        current_loc.add_item({k:v})

                print(f'Room has {drop_item}')
                player.remove_item(drop_item)
                        
            else:
                input_direction = input('Please enter: n, s, e, w, i(inventory), or q(quit): ')
        

    # If q then quit and end the game
    if input_direction == 'q':
        print('End Game')
        break

    # Set key to the inputs and values to the attributes
    cardinal_attr = {'n':'n_to', 's':'s_to', 'w':'w_to', 'e':'e_to'}

    # Check if room instance has the attribute
    while hasattr(current_loc, cardinal_attr[input_direction]) == False:
        print('A wall is in your way. Please try again.')
        input_direction = input('Please enter: n, s, e, w, i(inventory), or q(quit): \n')
        while input_direction not in commands:
            input_direction = input('Incorrect. Please enter: n, s, e, w, i(inventory), or q(quit) ')
        while input_direction == 'i':
            if player.player_item == {}:
                print('No Inventory')
                input_direction = input('Please enter: n, s, e, w, i(inventory), or q(quit): ')
            elif player.player_item != {}:
                print(player.player_item)
                input_direction = input('Please enter: n, s, e, w, i(inventory), or q(quit): ')
    
        # If input is 'q' then we quit the game
        if input_direction == 'q':
            print('End Game')
            continue_game = False
            break

    # Update current location by getting the attribute of the previous current location
    else:
        current_loc = getattr(current_loc, cardinal_attr[input_direction])
