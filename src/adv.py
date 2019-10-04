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



#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Dustin', room['outside'])
continue_game = True
while continue_game:
    current_room = player.current_room
    user_cmd = player.get_input()
    if user_cmd == 'q':
        print('End Game')
        break
    elif user_cmd == 'take':
        if current_room.room_item == {}:
            print('No items to pick-up')
            continue
        else:
            # Add items in room
            player.add_item(current_room.room_item)
            # Delete items in room
            current_room.remove_item(current_room.room_item)
    elif user_cmd == 'drop':
        if player.player_item == {}:
            print('No items to drop')
            continue
        else:
            # Remove items from player
            dropped_item = player.remove_item(player.player_item)
            # Drop to room
            current_room.add_item(dropped_item)
    else:
        player.move_room()
        print(player.current_room)
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
