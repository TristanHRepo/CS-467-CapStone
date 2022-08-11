import planet
import nlp
import inventory

class Byss(planet.Planet):

    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Byss")
        self.data = {
            "shelf": self.overhanging_shelf,
            "wall": self.colossal_wall,
            "sinkhole": self.sinkhole,
            "staircase": self.broken_staircase,
            "well": self.deep_well

        }
        self.rooms = [0, 1, 2, 3, 4]
        self.placement = 0
        self.accomplished = False
        self.visited = False
        self.print_welcome()

    """def query_NLP(self, text):
        ""Placeholder function to query natural language parser.""

        # value = self.validate_user_command(text)

        action = text.rsplit()

        return action"""

    def action(self, text):
        """Processes an action from the user"""

        object = self.validate_user_command(text)
        if object[0] is None:
            print("Invalid action")
            return False

        if object[1] is None:
            if object[0] in self.directions:
                self.directions[object[0]]()
                return False

        if object[1] not in self.data:
            print("Invalid action")
            return False

        # Final actions completed, return True to let engine know to move to next planet
        if self.accomplished == True:
            return True

        # Final action not complete, so return False
        return False

    def print_welcome(self):

        if self.visited == False:
            print('Welcome to Byss. A world wracked with constanst storms. Nothing but rain wherever you any attempt '
                  'to  land, nor do there really appear to be any reliable places of shelter. Your suit can handle '
                  'it, and thus it will have to do.')
            self.visited = True
        elif self.visited == True:
            print("Welcome back to Byss, where the rain has not, and likely never will abate. Back to where you left "
                  "off.")
        return

    def overhanging_shelf(self, action):
        """Interaction with cave"""

        if self.placement != 0:
            print("Invalid action")
            return

        if action.lower() == 'examine':
            print("Not much under this shelf other than your ship. And rain. But to the east you do see that huge "
                  "wall you noticed from the air. Maybe there's something there?")
        elif action.lower() == 'east':
            print("You make your way from under the shelf towards to wall. The very, very big wall...")
            self.placement += 1

        return

    def colossal_wall(self, action):
        """Interaction with cave"""

        if self.placement != 1:
            print("Invalid action")
            return

        if action.lower() == 'examine':
            print("The wall is spectacularly impressive. AN unbroken sheet of rock. But there's nothing here to find "
                  "at all. But to the south, you see an interesting sinkhole.")
        elif action.lower() == 'south':
            print(
                "With nothing to actually inspect at the wall, you head towards the sinkhole, to see if something's "
                "there.")
            self.placement += 1

        return

    def sinkhole(self, action):

        if self.placement != 2:
            print("Invalid action")
            return

        if action.lower() == 'examine':
            print(
                "Another dead end. The sinkhole holds nothing. That the torrential rain hasn't filled it up at all is "
                "a testament to it's danger. But you must journey on. Looks like some sort of broken staircase to "
                "the east.")
        elif action.lower() == 'east':
            print(
                "Time to move on form this spot as well. The rains continue to make taveling more difficult, "
                "but it's time to try the pillar with the broken staircase.")
            self.placement += 1

        return

    def broken_staircase(self, action):

        if self.placement != 3:
            print("Invalid action")
            return

        if action.lower() == 'examine':
            print(
                "Yet another dud. You're starting to wonder if there's absolutely anything interesting on this "
                "planet other than rain and boring rock. But there's a well to the southwest. Gonna give it one "
                "last try.")
        elif action.lower() == 'southwest':
            print(
                "You're really getting tired of all this rain. But hopefully this well is more promosing than the "
                "last few spots you tried.")
            self.placement += 1

        return

    def deep_well(self, action):
        """Interaction with mucus"""

        if self.placement != 4:
            print("Invalid action")
            return

        if action.lower() == 'take':
            print(
                "You reached into the well, just to see what was there, and you came away with a beautiful geode. "
                "This is exactly the sort of thing you were looking for. Time to move on to a new planet.")
            self.accomplished = True
            inventory.add("geode")

        return
