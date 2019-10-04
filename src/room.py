# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
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
        keys = [key for key in r_item_name]
        for k in keys:
            self.room_item.pop(k)
        
    
    def __str__(self):
        if self.room_item == {}:
            no_item = 'No Items'
            return f'Name: {self.name}\nDescription: {self.description}\nRoom Items: {no_item}'
        else:
            return f'Name: {self.name}\nDescription: {self.description}\nRoom Items: {self.room_item}'

    def __repr__(self):
        return f'Room({repr(self.name)}, {repr(self.description)})'