import planet
import inventory


class Atlas(planet.Planet):
    """The crystal planet"""

    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Atlas")
        self.visited = False
        self.print_welcome()
        self.data = {
            "jagged red peak": self.peak,
            "peak": self.peak,
            "red peak": self.peak,
            "white sigil": self.sigil,
            "sigil": self.sigil,
            "red crystal": self.crystal,
            "crystal": self.crystal,
            "silver key": self.key,
            "key": self.key
        }
        self.directions = [
            "north",
            "south",
            "east",
            "west"
        ]
        self.crystal_obtained = False
        self.rooms = [0, 1]
        self.placement = 0

    def query_NLP(self, text):
        """Placeholder function to query natural language parser."""

        value = self.validate_user_command(text)
        action = text.rsplit()
        return action

    def action(self, text):
        """Processes an action from the user"""
        obj = self.query_NLP(text)
        if obj is False:
            print("Invalid action")

        if len(obj) < 2:
            if obj[0] == "look":
                self.visited = False
                self.print_welcome()
            # if obj[0] in self.directions:
            #     self.directions[obj[0]]()
            #     return False

        else:
            self.data[obj[1]](obj[0])

        # Final Action:
        return True

        # DEFAULT:
        # return False

    def print_welcome(self):
        """
        Prints the room's long description if it hasn't been visited before, or if 'look' is input.
        Otherwise prints the room's short description.
        """
        if not self.visited:
            print("You fly down onto the blue planet covered in swirling mists. As your ship descends, "
                  "it is difficult to see due to the density of the mysterious fog, but you start to make out "
                  "crystalline structures all over the surface of the planet. The majority of them are blue, "
                  "but there are tones of white and purple as well, as though the planet itself is the inside of a "
                  "geode. You land on a flat, smooth blue area that is elevated out of the mist, and look around. The "
                  "ground is nearly entirely solid crystal, which rises and falls into hills and valleys. \n\nTo the "
                  "south of your landing point, you notice a jagged red peak rising through the fog. It does not appear"
                  " to be too steep to climb. In the sky to the west, you notice a golden planet looming close by, "
                  "easily within a short flying distance. ")
            self.visited = True
        else:
            print("You are on a blue, mist-covered planet that is covered in crystal. You are standing on a smooth, "
                  "flat area. There is a jagged red peak to the south. There is a golden planet in the sky to the "
                  "west. ")

    def peak(self, action):
        """Interaction with peak"""

        if self.placement != 0:
            print("Invalid action")
            return

        act = action.lower()
        if act == 'south' or act == 'go south' or act == 'jagged red peak' or act == 'go jagged red peak':
            print("You make your way towards the jagged red peak rising over the mist to the south. You have to descend"
                  " down into the mist to reach it. As you walk, you notice the ground below the surface of the mist is"
                  " much more rugged, not smooth and flat like the area where your ship landed. It's easy to lose your "
                  "footing, so you walk very slowly and carefully.\n\n"
                  "When you get to the peak, you find that there is a seemingly natural path built into it, spiraling "
                  "up to the top. You sense heat pulsing from inside the red crystalline structure.")

        elif act == 'examine':
            print("A jagged red peak that rises over the mist covering the planet. It seems to be made of red crystal.")

        elif act == 'climb' or act == 'follow':
            print("You climb the winding path out of the mist with relative ease, though you have to proceed with "
                  "caution. As you reach the top of the peak, you notice that suspended in the air at eye level is a "
                  "small, glittering, round red crystal.")
            self.placement += 1

    def crystal(self, action):
        """ Interaction with crystal """
        if self.placement != 1:
            print("You cannot do that now!")
            return

        act = action.lower()
        if act == 'touch':
            print("You press a gloved finger to the crystal. You can sense great heat emanating from it.")

        elif act == 'examine':
            print("The crystal floating in front of you is small and round, with a crimson hue. It glitters in the "
                  "faint starlight. ")

        elif act == 'take':
            print("You grab the crystal and add it to your inventory. On the ground to below, to the east, you notice "
                  "a white sigil in the shame of a flame begin to glow.")
            inventory.add("red crystal")  # Add to inventory file
            self.crystal_obtained = True

        elif act == 'go':
            self.placement += 1

    def sigil(self, action):
        """Interaction with sigil"""

        if self.placement != 1:
            print("Invalid action; please try again")
            return

        act = action.lower()
        if act == 'examine':
            print("You examine the white sigil. It appears to be a natural feature of the ground beneath your feet, "
                  "rather than something that has been painted there. It makes a pointed shape that appears to "
                  "resemble a flame. In the center, there is a raised circle marking. ")
        # Action varies based on whether crystal is in inventory
        elif act == 'touch':
            # Check if the crystal is in inventory before interaction
            if inventory.check("red crystal"):
                print("You reach out and touch the sigil. The glow brightens and a silver, gem-encrusted key rises from"
                      " the circle marking in the center, floating there. ")
            else:
                print("There is no response from the sigil. There is no abnormal sensation.")

        elif act == 'talk':
            print("The sigil is silent.")

        elif act == 'taste':
            print("What are you doing? The sigil is not edible.")

    def key(self, action):
        """ Interaction with key """
        if self.placement != 0:
            print("You can't do that here. ")
            return

        act = action.lower()
        if act == 'take':
            inventory.add("silver key")
            print("You pick up the key and add it to your inventory.")

        elif act == 'examine':
            print("The key is silver and encrusted with gems. It is of standard size and shape otherwise.")

        elif act == 'touch':
            print("You touch the key. It continues to float there.")
