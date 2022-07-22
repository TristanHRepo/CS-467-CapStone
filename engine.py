import Subaqueanus

class Engine:
    """This is the game engine that checks for user input and move the player to correct planets"""

    def __init__(self):
        """Asks if you want to load a game, then loads game and starts engine"""

        planet = None
        game = None

        flag = self.prompts()
        if flag == 1:
            game = self.load()
            self.engine()
        elif flag == 0:
            game = self.new_game()
            self.engine()
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
        """Loads a game for the user by asking for a entry in save file and returning data for that entry"""

        with open('saves.txt', 'r') as file:

            saves = file.readlines()

        print("Current Saves: ")
        for save in saves:
            print(save)

        print("\nWhich save should be used?")
        selection = input(">>")

        print("Loading: " + selection + "\n-------------------------------------------\n")

        return

    def new_game(self):
        """Creates a new game for the user"""

        return

    def close(self):
        """Closes game"""

        print("Closing game")

        return

    def save_game(self):
        """Saves the game"""

        planet = self.get_planet()

        return

    def get_planet(self):
        """Gets which planet the player is currently on"""



        return

    def engine(self):
        """Game play loop for the game"""

        # planet = self.get_planet()

        planet = Subaqueanus.Subaqueanus()

        while True:

            action = input(">>")
            if action == 'quit':
                break
            planet.action(action)

        self.close()
        return

game = Engine()

