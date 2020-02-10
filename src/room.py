# Implement a class to hold room information. This should have name and
# description attributes.

# Attributes
# name
# description

# n_to, s_to, e_to, and w_to
# which point to the room in that respective direction.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.contents = []

    def __str__(self):
        return f"\nname: {self.name}\ndescription: {self.description}\n"

    def __repr__(self):
        return f"Room({repr(self.name), repr(self.description)})"
