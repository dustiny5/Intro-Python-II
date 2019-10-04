# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.user_input = None
        self.player_item = {}

    def get_input(self):
        self.user_input = input('Please enter: n, s, e, w, q, take, drop: \n')
        while self.user_input not in ['n', 's', 'e', 'w', 'q', 'take', 'drop']:
            self.user_input = input('Incorrect! Please enter: n, s, e, w, q, take, or drop: \n')
        return self.user_input
    
    def add_item(self, player_item):
        if player_item != {}:
            for k,v in player_item.items():
                self.player_item.update({k:v})
        print(f'Picked-up: {player_item}')

    def remove_item(self, r_item_name):
        print(f'Player dropped: {r_item_name}')
        dropped_item = {}
        keys = [key for key in r_item_name]
        for k in keys:
            dropped_item.update({k:self.player_item.pop(k)})
        return dropped_item

    def move_room(self):
        cardinal_attr = {'n':'n_to', 's':'s_to', 'w':'w_to', 'e':'e_to'}
        input_ = cardinal_attr[self.user_input]
        while hasattr(self.current_room, input_) == False:
            self.get_input()
            input_ = cardinal_attr[self.user_input]
        else:
            self.current_room = getattr(self.current_room, input_)

    def __str__(self):
        return f'Name: {self.name}\nExploring: {self.current_room}'

    def __repr__(self):
        return f'Player({repr(self.name)}, {repr(self.current_room)})'