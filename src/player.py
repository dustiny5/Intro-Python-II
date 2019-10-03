# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    '''Player Class'''
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.player_item = {}

    def add_item(self, player_item):
        if player_item != {}:
            for k,v in player_item.items():
                self.player_item.update({k:v})

    def remove_item(self, r_item_name):
        del self.player_item[r_item_name]
        print(f'Player dropped: {r_item_name}')


    def __str__(self):
        item_list = ''
        for k,v in self.player_item.items():
            item_list += f'     {v}\n'

        return f'Player Name: {self.name}\n{self.current_room}\nItems:\n {item_list}'
    
    def __repr__(self):
        return f'Player({repr(self.name)}, {repr(self.current_room)})'
