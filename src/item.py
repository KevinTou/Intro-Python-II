# Write an Item class which will be the base class for specialized item types to be declared later

# Attributes
# name
# Names should be one word for ease of parsing

# description


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"item: {self.name}, description: {self.description}"

    def __repr__(self):
        return f"{repr(self.name)}"

    def on_take(self):
        return f"You have picked up {self.name}"

    def on_drop(self):
        return f"You have dropped {self.name}"
