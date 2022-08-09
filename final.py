import planet
import inventory


class Asterone(planet.Planet):
    """The final planet"""

    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Asterone")
        self.print_welcome()
        self.data = {
            "path": self.path,
            "tower": self.tower,
            "stairs": self.tower,
            "door": self.door,
            "room": self.room,
            "button": self.button,
            "journal": self.log,
            "log": self.log,
            "datalog": self.log
        }
        self.visited = True
        self.rooms = [0, 1, 2]
        self.door_locked = True
        self.placement = 0

    def query_NLP(self, text):
        """Placeholder function to query natural language parser."""

        value = self.validate_user_command(text)
        action = text.rsplit()
        return action

    def action(self, text):
        """Processes an action from the user"""
        object = self.query_NLP(text)
        if object is False:
            print("Invalid action")

        self.data[object[1]](object[0])
        if object == "look":
            self.print_welcome()

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
            print("Finally nearing the end of your journey, you navigate your ship towards the furthest mass in the "
                  "cluster. At a distance, the planet appears to be blue. But as you get closer, you realize that it "
                  "is burning in every color you can imagine, possessing the brightest glow you've seen so far. The "
                  "spectrum is mesmerizing. All over the planet, you can see glowing pools that pulse with various "
                  "colors. Reaching into the sky is a tower of strange, multicolored crystal, consisting of "
                  "square-like shapes and hues like an oil slick. You recognize the mineral as bismuth -- or "
                  "something similar to it. The land itself is aetherial, glassy, smooth, with glows of all colors "
                  "mingling and flowing together. There is a large flat area that is perfect for landing your ship, "
                  "as though it were made for this purpose. As you exit your ship, you notice the landing zone is "
                  "surrounded by liquid, like a moat, on all sides, but there is a path to the north that stretches "
                  "over the liquid, leading towards the tower. /n/nFar in the distant southern sky, in the direction "
                  "from which you just came, you can see the golden-hued planet glimmering softly, though it would be "
                  "impossible to see its flowers if you didn't know they were there.")
        else:
            print("You land on a bright, primarily blue planet, far away from the others. Up close, you can see the "
                  "planet is multicolored. There are pools of glowing colorful liquids. There is a tall tower to the "
                  "north that looks to be made of bismuth. Your ship is on a large, flat area surrounded by glowing "
                  "liquid. /n/nThere is a path to the north that reaches over the liquid. Far to the south is the "
                  "golden planet. ")

    def path(self, action):
        """Interaction with path"""

        if self.placement != 0:
            print("Invalid action")
            return

        act = action.lower()
        if act == 'north' or act == 'go north' or act == 'path' or act == 'go path':
            print("You walk northward, making your way onto the path that stretches over the strange liquid. Like the "
                  "rest of the solid surface of this planet, the path is glassy and smooth, almost translucent. Around "
                  "you, you can see the glowing, colorful liquid, but something tells you not to touch it. Do you "
                  "keep following the path to the tower? ")

        elif act == 'examine':
            print("A smooth, glassy, semi-translucent path that stretches across the strange liquid. ")

        elif act == 'move' or act == 'follow':
            print("You follow the strange, glossy path, heading towards the tower you saw when you landed. As you "
                  "approach, you see that there are stairs that wind around the tower. Will you climb them? ")
            self.placement += 1

    def tower(self, action):
        """ Interaction with tower """
        if self.placement != 1:
            print("You cannot do that now!")
            return

        act = action.lower()
        if act == 'climb':
            print("You climb the stairs of the crystal tower. \n\n At the top of the tower, you find a door with a "
                  "rather conspicuous keyhole.")

        elif act == 'examine':
            print("You are looking at a very tall tower comprised of squareish, prismatic crystals. You recognize the "
                  "crystal to be bismuth, or at least soemthing that looks quite similar. It glimmers with many colors,"
                  " like an oil slick. There are stairs that spiral around to the top of the tower. At the top of the "
                  "tower, there is a plain door with a conspicuous keyhole visible. ")

    def door(self, action):
        """ Interaction with door """
        if self.placement != 1:
            print("You can't do that here. ")
            return

        act = action.lower()
        if act == 'open':
            if self.door_locked:
                print("The door does not budge. It is locked. ")
            else:
                print("The door easily swings open, revealing a room. It appears to be akin to a control room. ")

        elif act == 'unlock':
            if inventory.check("silver key"):
                print("The key unlocks the door without a hitch. ")
                inventory.remove("silver key")
            else:
                print("You have no key!")

        elif act == 'examine':
            print("The door at the top of the bismuth tower's stairs is surprisingly plain and nondescript, aside from "
                  "the conspicuous keyhole by its handle. ")

        elif act == 'touch':
            print("You touch the door. It does not react. ")

    def key(self, action):
        """ Interaction with key """
        if self.placement != 1:
            print("You can't use that here.")
            return

        # Check if we have the key
        if not inventory.check("silver key"):
            print("You don't have a key!")
            return

        act = action.lower()
        if act == 'use':
            print("The key unlocks the door without a hitch. ")

    def room(self, action):
        """ Interaction with room """
        if self.placement != 1:
            print("You can't do that here. ")
            return

        act = action.lower()
        if act == 'enter':
            if self.placement != 2:
                print("Behind the door you just opened, you find what you can only identify as a control room. There is"
                      " a station with a simple terminal with a flat glassy area, similar to a scanner. There is a red "
                      "button beside the scanner. ")
                self.placement = 2
            else:
                print("You're already in the room!")

        elif act == 'examine':
            print("Behind the door you just opened, you find what you can only identify as a control room. There is "
                  "a station with a simple terminal with a flat glassy area, similar to a scanner. There is a red "
                  "button beside the scanner. ")

    def button(self, action):
        """ Interaction with button """
        if self.placement != 2:
            print("You can't do that here. ")
            return

        act = action.lower()
        if act == 'examine':
            print("At the simple terminal station, beside the scanner-like device, there is a conspicuous red button.")

        elif act == 'push':
            print('You push the button. A holographic interface appears in front of you. It reads, "Connecting to '
                  'Home..." After a moment, the display changes. It now reads, "Please scan datalog."')

        elif act == 'touch':
            print("You touch the button. Since you didn't push it down, nothing happens. ")

    def log(self, action):
        """ Interaction with log """
        if self.placement != 2:
            print("You can't do that here. ")
            return

        act = action.lower()
        if act == 'examine':
            print("You look at your log, in which you have been collecting data about every planet you have seen. "
                  "This book holds a lot of information to send home...")

        elif act == 'scan' or act == 'use':
            print('You place your log onto the flat scanning surface. The interface reads, "Input accepted. Now '
                  'transmitting to Home..." \n\n'
                  'Subaqueanus: \n\n'
                  'Maia \n\n'
                  'Alcyone \n\n'
                  'Celaeno \n\n'
                  'Byss \n\n'
                  'Eridanos \n\n'
                  'Monarch \n\n'
                  'Atlas \n\n'
                  'Pleione \n\n'
                  'Desertum \n\n'
                  'Asterope: You Are Here\n\n')
            print('At the end of it all, the display reads simply, "Transmission received!"')

