import planet


class Monarch(planet.Planet):
    
    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Monarch")
        self.print_welcome()
        self.data = {
            "clearing": self.clearing,
            "tree archway": self.tree_archway,
            "pleasant jungle grove": self.pleasant_jungle_grove

        }
        self.rooms = [0, 1, 2]
        self.placement = 0
        self.accomplished  = False

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

    def clearing(self, action):
        """Interaction with cave"""

        if self.placement != 0:
            print("Invalid action")
            return

        if action.lower() == 'look':
            print("You're in awe of the natural beauty around you. However, you realize that that the forest is too think to traverse,/n other than through the tree archway.")
        elif action.lower() == 'walk':
            print("You walk over to the archway itself. It is truly magnificent to behold. You can't see where the archway leads to,/n but the plant life is thin enough you can cross through it.")
            self.placement += 1

        return

    def tree_archway(self, action):
        """Interaction with mucus"""

        if self.placement != 1:
            print("Invalid action")
            return

        if action.lower() == 'cross':
            print("You cross through the archway. Not too bad going through. You come out into a pleastn jungle grove.")
            self.placement += 1

        return

    def pleasant_jungle_grove(self, action):
        """Interaction with mucus"""

        if self.placement != 2:
            print("Invalid action")
            return

        if action.lower() == 'catch':
            print("You've managed to gently grab the bee-like insect, though that sting in your hand in unpleasant./n And you're actually feeling better now, rather than worse. A rather unexpected outcome. This is worth keeping.")
            self.accomplished = True        

        return