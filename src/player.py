# Write a class to hold player information, e.g. what room they are in
# currently.

# Attributes
# name
# current_room


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f"{self.name} is in {self.current_room.name}"

    def __repr__(self):
        return f"Player({repr(self.name), repr(self.current_room)})"
