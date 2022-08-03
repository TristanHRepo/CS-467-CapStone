import planet
import nlp
from random import seed
from random import randint

seed(1)


class Maia(planet.Planet):
    """The Maia planet"""

    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Maia")
        self.enter_planet()
        self.data = {
            "pool": self.pool,
            "man": self.man,
            "cylinder": self.cylinder,
            "die": self.die,
            "hermes": self.hermes,
            "tablet": self.tablet,
            "chest": self.chest,
            "wall": self.wall,
            "button": self.wall
        }
        self.rooms = [0, 1, 2, 3, 4, 5]
        self.placement = 0

    def query_NLP(self, text):
        """Placeholder function to query natural language parser."""

        # value = self.validate_user_command(text)

        action = text.rsplit()

        return action

    def action(self, text):
        """Processes an action from the user"""

        object = self.query_NLP(text)
        if object is False:
            print("Invalid action")

        self.data[object[1]](object[0])

        return

    def enter_planet(self):
        print('You feel groggy.  You slowly sit up and look around.  You are in what appears to be an antique spaceship.')
        print('The ground is metallic with a hint of rust, and through a window you can see what looks like')
        print('the star Maia of the Pleiades system.  It reminds you of pictures you saw in an old textbook from')
        print('the James Webb telescope from back in the 21st century.')
        print('There appears to be two pools of crystal-clear water on either side of you')
        print('which seems odd for an antique spaceship floating through this star system.')
        print('A big pool is to your right, and the small pool is to your left.')
        print('There appears to be something on the cave wall, and a man encased in carbonite is between you')
        print('and the window.  The man reminds you of a legendary archaeologist from 20th century cinema.')
        print('You get the sense that someone is playing an elaborate practical joke on you')
        print('by conflating a few different things that do not quite belong together.')
        
        return
    
    
    def pool(self, action):
        """Interaction with pool"""

        if self.placement != 0:
            print("Invalid action")
            return

        if action.lower() == 'look':
            print("The pool has a treasure chest submerged in the water.")
        self.placement += 1

        return

    def chest(self, action):
        """Interaction with pool"""

        if self.placement < 1:
            print("Invalid action")
            return

        if action.lower() == 'look':
            print("The chest appears to have a keyhole.  The size of the keyhole appears to match the size of the key.")
            self.placement += 1

        if action.lower() == 'open':
            print("The chest has a stone tablet")
            self.placement += 10

        return

    def wall(self, action):
        """Interaction with pool"""

        if self.placement != 0:
            print("Invalid action")
            return

        if action.lower() == 'look':
            print("The wall has an indentation.  It is remarkably the same size and shape of the pentagonal tablet.")
            print("There is also a winged foot engraved on the wall of the ship.")
            self.placement += 1

        return

    def man(self, action):
        """Interaction with carbonite man"""

        if self.placement != 0:
            print("Invalid action")
            return

        if action.lower() == 'look':
            print("There is a vibranium key next to the carbonite man, and a cylindrical object with a button.")
        elif action.lower() == 'examine':
            print("There is a vibranium key next to the carbonite man, and a cylindrical object with a button")
        elif action.lower() == 'take':
            print("There is a vibranium key next to the carbonite man, and a cylindrical object with a button")
            self.placement += 1

        return

    def tablet(self, action):
        """Interaction with tablet"""

        if self.placement != 0:
            print("Invalid action")
            return

        if action.lower() == 'take':
            print("You now have the tablet.")
        elif action.lower() == 'examine':
            print("The tablet is shaped like a pentagon.  There is a winged foot on the tablet.")
            self.placement += 1

        return

    def cylinder(self, action):
        """Interaction with cylinder"""

        if self.placement != 1:
            print("Invalid action")
            return
        if action.lower() == 'look':
            print("The cylindrical object with a very pushable button starts vibrating.")
        
        return
        
    def button(self, action):
        """Interaction with button"""

        if self.placement != 1:
            print("Invalid action")
            return
        if action.lower() == 'look':
            print("The button wants to be pushed.")
        if action.lower() == 'push button':
            print("A powerful blue beam emerges from what looks like a lightsaber.")
            print("It appears that this is not a weapon, however, as the beam projects a hologram")
            print("of a woman that looks eerily like Princess Leia, but she calls herself Princess Maia of Pleiades.")
            print("Maia speaks.  Help me (player name)-wan Kenobi!  What is the name of my son?")
            self.placement += 100
        return

    def hermes(self, action):
        """responding to Maia with Hermes as an answer...this part needs adjusting"""

        if self.placement < 100:
            print("You should not know that yet!")
            return
        if self.placement > 100:
            print("You are correct!  Hermes is the son of Maia!")
            print("The room begins to vibrate.  A very large 20-sided die appears.")
            self.placement += 1000
        return

    def die(self, action):
        """rolling the die"""

        if self.placement < 1000:
            print("You cannot roll it until it appears!")
            return
        if self.placement > 1000:
            dice = randint(0, 20)
            print("SUCCESS!  You rolled a ", dice)
            print("A portal appears...beckoning...")
        return
