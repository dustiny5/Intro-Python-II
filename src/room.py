# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    '''Room Class'''

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.room_item = {}

    def add_item(self, room_item):
        if room_item != {}:
            for k,v in room_item.items():
                self.room_item.update({k:v})

    def remove_item(self, r_item_name):
        print(f'Remove {r_item_name} from {self.name}')
        del self.room_item[r_item_name]

    def __str__(self):
        item_list = ''
        for k,v in self.room_item.items():
            item_list += f'{v}\n=====\n'

        return f'Current Position: {self.name}\n-----\nDescription: {self.description}\n-----\nRoom Item:\n-----\n{item_list}'

    def __repr__(self):
        return f'Room({repr(self.name)}, {repr(self.description)})'
