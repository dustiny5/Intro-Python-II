# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    '''Room Class'''

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'Current Position: {self.name}\nDescription: {self.description}'

    def __repr__(self):
        return f'Room({repr(self.name)}, {repr(self.description)})'
