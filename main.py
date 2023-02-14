from map import MapBuilder
from player import Player
from console import *

##### GLOBAL VARIABLES ########

MAP_FILE = "./text_map.xlsx"
WORLD_MAP = MapBuilder(MAP_FILE)
BOUNDARIES = WORLD_MAP.get_boundaries()
PLAYER = Player(100, 100, BOUNDARIES)

COMMANDS = {"help": print_help, "move": PLAYER.move, "observe": PLAYER.observe}


def init_game():
    player_name = input(f"What is your name? ")
    PLAYER.set_name(player_name)
    print("Hello " + PLAYER.get_name())


if __name__ == "__main__":
    init_game()
    while True:
        print_to_console(
            "You are standing on {}.".format(
                WORLD_MAP.return_tile(
                    PLAYER.get_coordinates()[0], PLAYER.get_coordinates()[1]
                ).name
            )
        )
        command = input("> ").lower().split(" ")
        if command[0] in COMMANDS:
            COMMANDS[command[0]](
                *command[1:]
            )  # puts everything after the first command as an argument, but unpacks it first, so no empty list is delivered
        else:
            print("Befehl nicht erkannt.")
