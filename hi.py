class Person:
    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name

    def full_name(self):
        return self.name + " " + self.family_name