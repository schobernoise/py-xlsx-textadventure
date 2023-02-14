from console import *


class Player:
    def __init__(self, hp, mana, boundaries, name="", coordinates=(0, 0)):
        self.set_name(name)
        self.set_coordinates(coordinates)
        self.set_hp(hp)
        self.set_mana(mana)
        self.__boundaries = boundaries
        self.inventory = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_coordinates(self):
        return self.__coordinates

    def set_coordinates(self, coordinates):
        self.__coordinates = coordinates

    def get_hp(self):
        return self.__hp

    def set_hp(self, hp):
        self.__hp = hp

    def get_mana(self):
        return self.__mana

    def set_mana(self, mana):
        self.__mana = mana

    ############################

    def move(self, direction):
        print("BOUNDARIES", self.__boundaries)
        if direction == "north" and self.get_coordinates()[0] > 0:
            self.set_coordinates(
                (self.get_coordinates()[0] - 1, self.get_coordinates()[1])
            )
        elif direction == "south" and self.get_coordinates()[0] < self.__boundaries[0]:
            self.set_coordinates(
                (self.get_coordinates()[0] + 1, self.get_coordinates()[1])
            )
            # print("You are going", direction)
        elif direction == "east" and self.get_coordinates()[1] < self.__boundaries[1]:
            self.set_coordinates(
                (self.get_coordinates()[0], self.get_coordinates()[1] + 1)
            )
        elif direction == "west" and self.get_coordinates()[1] > 0:
            self.set_coordinates(
                (self.get_coordinates()[0], self.get_coordinates()[1] - 1)
            )
        else:
            print_to_console("I can't go there")
        print_to_console(self.get_coordinates())

    def observe(self):
        print_to_console("You are observing your surroundings.")
        print_to_console("You see ...") # TODO: Here it would be possible to fetch data from the current tile, displaying descriptive information.
    
    def get_inventory(self):
        raise NotImplementedError
    
    def add_to_inventory(self, items):
        raise NotImplementedError
    
    def del_from_inventory(self,items):
        raise NotImplementedError
