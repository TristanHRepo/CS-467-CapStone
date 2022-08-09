import planet
import nlp

class Desertum(planet.Planet):
    """The underwater planet"""

    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Subaqueanus")
        self.enter_planet()
        self.data = {
            ""
            # "mucus": self.mucus,
            # "sculpture": self.sculpture,
            # "sculptures": self.sculpture,
            # "pearl": self.pearl,
            # "sphere": self.pearl,
            # "junk": self.junk,
            # "tool": self.tools,
            # "part": self.parts,
            # "parts": self.parts,
            # "tools": self.tools,
            # "ship": self.ship
        }
        self.checkpoints = [False, False, False, False, False, False, False, False]
        self.placement = 0

    def action(self, text):
        """Processes an action from the user"""

        object = self.validate_user_command(text)
        if object[0] is None or object[1] is None:
            print("Invalid action")
            return False

        self.data[object[1]](object[0])

        # Final actions completed, return True to let engine know to move to next planet
        if False:
            return True

        # Final action not complete, so return False
        return False

    def upstream(self):
        """The area up stream"""

        if (action.lower() == 'move' or action.lower() == 'north') and self.placement == 0:
            print("")
            self.placement = 2

        if self.placement != 2:
            print("Invalid action")
            return

        return

    def downstream(self):
        """The area down stream"""

        if (action.lower() == 'move' or action.lower() == 'north') and self.placement == 0:
            print("")
            self.placement = 3

        if self.placement != 3:
            print("Invalid action")
            return

        return

    def statue(self, action):
        """The statue to the North"""

        if (action.lower() == 'move' or action.lower() == 'north') and self.placement == 0:
            print("You approach the formation...\n"
                  "The formation turns out to be some kind of carved pillar about 15 feet high.\n"
                  "At the top of the pillar you see three holes one facing North\n"
                  "The other two point South-East and South-West, toward the channel of water\n"
                  "The Pillar also seems to have a carved entry way\n"
                  "To the north you see a contraption.")
            self.placement = 1

        if self.placement != 1:
            print("Invalid action")
            return



        return

    def enter_planet(self):
        """Prints the welcome for the planet"""

        print("You begin to enter the atmosphere of a new planet...\n"
              "As you descend onto the planet, you take notice of the star in the sky\n"
              "This planet has bright light from this solar systems sun, similar to Earth\n"
              "Your ship lands in a rocky compound near a channel of water.\n"
              "The surrounding area is desert like, but with interesting foliage growing from the sand\n"
              "As you step out of the ship, you notice the air is humid. Strange..\n"
              "It feels similar to a beach. However, no large body of water was spotted in your descent.\n"
              "The channel of water is crystal clear, and runs farther than the horizon.\n"
              "With this planets sun established as your North, the water runs to the West\n"
              "South is your ship, and East would be upstream.\n"
              "You notice to the North a large, un-natural formation\n")
        return
