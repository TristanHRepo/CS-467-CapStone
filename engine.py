import sys
import json
import inventory
import nlp
from Planets.Subaqueanus import Subaqueanus
from Planets.Desertum import Desertum
from Planets.Maia import Maia
from Planets.Alcyone import Alcyone
from Planets.Celaeno import Celaeno
from Planets.Byss import Byss
from Planets.Eridanos import Eridanos
from Planets.Monarch import Monarch
from Planets.Atlas import Atlas
from Planets.Pleione import Pleione
from Planets.final import Asterone


class Engine:
    """This is the game engine that checks for user input and move the player to correct planets"""

    def __init__(self):
        """Asks if you want to load a game or start new, then loads game and starts engine"""

        self.planets = ['Subaqueanus', 'Maia', 'Alcyone', 'Celaeno', 'Byss', 'Eridanos', 'Monarch', 'Atlas', 'Pleione',
                        'Desertum', 'Asterone']
        self.planet = None
        self.game = None

        flag = self.prompts()
        if flag == 1:
            self.game = self.load()
            self.engine()
        elif flag == 0:
            self.game = self.new_game()
            if self.game is not False:
                self.engine()
            else:
                self.close()
        else:
            self.close()

    def prompts(self):
        """Asks the user if you want to load a game and then calls load function if so"""

        load_game = input("Would you like to load a game? (Y/N)\n>>")

        if load_game == 'y' or load_game == 'Y':
            return 1

        new_game = input("Would you like to enter a new game? (Y/N)")

        if new_game == 'y' or new_game == 'Y':
            return 0

        return 2

    def load(self):
        """Loads a game for the user by asking for an entry in save file and returning data for that entry"""

        print("Loading:\n-------------------------------------------\n")

        saved_game = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        try:
            with open('Savedata.txt', 'r') as file:

                save = file.readlines()
                for planet in save:

                    array = planet.rsplit('=')

                    position = self.planets.index(array[0])

                    array[1] = array[1].replace('\n', '')
                    array[1] = int(array[1])

                    if array[1] == 1:
                        saved_game[position] = 1

            file.close()
        except FileNotFoundError:
            print("No saved game file found.")
            return False

        for index in range(len(saved_game)):
            if not saved_game[index]:
                self.planet = self.get_planet(self.planets[index])
                break

        return saved_game

    def new_game(self):
        """Creates a new game for the user"""

        with open("Savedata.txt", 'w') as file:

            for index in range(len(self.planets)):
                file.write(self.planets[index] + "=0\n")

        file.close()

        # Create new inventory: load in base & write it to inventory file to edit
        with open("base_inventory.json") as file1:
            base = json.load(file1)

        with open("inventory.json", "w") as file2:
            json.dump(base, file2, indent=4)

        self.planet = self.get_planet(self.planets[0])

        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def close(self):
        """Closes game"""

        print("Closing game")

        return

    def save_game(self):
        """Saves the game"""

        with open("Savedata.txt", 'w') as file:

            for index in range(len(self.planets)):
                if self.game[index] == 1:
                    file.write(self.planets[index] + "=1\n")
                else:
                    file.write(self.planets[index] + "=0\n")

        file.close()

        print("Game Saved:\n-------------------------------------------")

        return

    def get_planet(self, request):
        """Initiates the requested planet's class based on planet name passed in"""

        planet = getattr(sys.modules[__name__], request)

        planet = planet()

        return planet

    def change_planet(self):
        """Changes planets for the game"""

        pos = self.planets.index(type(self.planet).__name__)
        self.game[pos] = 1

        for index in range(len(self.game)):
            if not self.game[index]:
                self.planet = self.get_planet(self.planets[index])
                break

        self.save_game()

        return

    def engine(self):
        """Game play loop for the game"""
        manually_closed = False
        while True:

            action = input(">>")

            if action == 'help':
                nlp.get_actions()
                continue

            if action == 'quit':
                self.close()
                manually_closed = True
                break

            if action == 'inventory':
                print(inventory.get_inv())
                continue

            if action == 'savegame':
                self.save_game()
                continue

            if action == 'loadgame':
                load_game = input("Would you like to load a game? (Y/N)\n>>")
                if load_game == 'y' or load_game == 'Y':
                    self.load()
                    continue

            room_status = self.planet.action(action)

            if room_status is True:
                self.change_planet()


        if not manually_closed:
            self.close()
        return


if __name__ == "__main__":
    game = Engine()
