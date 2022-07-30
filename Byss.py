import planet


class Byss(planet.Planet):
    
    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Byss")
        self.print_welcome()
        self.data = {
            "oerhanging shelf": self.overhanging_shelf,
            "colossal wall": self.colossal_wall,
            "deep well": self.deep_well

        }
        self.rooms = [0, 1, 2]
        self.placement = 0
        self.accomplished = False

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

    def overhanging_shelf(self, action):
        """Interaction with cave"""

        if self.placement != 0:
            print("Invalid action")
            return

        if action.lower() == 'walk':
            print("You make your way from under the shelf towards to wall. The very,/n very big wall...")
            self.placement += 1

        return

    def colossal_wall(self, action):
        """Interaction with cave"""

        if self.placement != 1:
            print("Invalid action")
            return

        if action.lower() == 'move':
            print("With nothing to actually inspect at the wall, you move to the well nearby.")
            self.placement += 1

        return

    def deep_well(self, action):
        """Interaction with mucus"""

        if self.placement != 2:
            print("Invalid action")
            return

        if action.lower() == 'grab':
            print("You reached into the well, just to see what whas there, and you came away with a beautiful geode.")
            self.accomplished = True        

        return