import planet


class Subaqueanus(planet.Planet):
    """The underwater planet"""

    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Subaqueanus")
        self.print_welcome()
        self.data = {
            "cave": self.cave,
            "mucus": self.mucus
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

    def cave(self, action):
        """Interaction with cave"""

        if self.placement != 0:
            print("Invalid action")
            return

        if action.lower() == 'move':
            print("You move closer to the cave. At it's entrance you notice that the cave is dimly illuminated by an interesting fungus with small tenticles, which at the tip of each tentacle is a small bulb which gives off faint white light.\nFurther in the cave you notice something much larger giving off a red hue.")
        elif action.lower() == 'examine':
            print("A dark cave. The opening must be at least 15ft in diameter. Maybe something of interest lies within?")
        elif action.lower() == 'enter':
            print("You enter the cave. Your suit's light giving off a narrow cone of light ahead of you, you begin to descend. \nAs you begin to ascend, you notice the tenticles move toward you, as if they are trying to touch you.\nThe red hue begins to increase in size. You approach carefully, not wanting to disturb whatever lies ahead. Finally, you begin to see a figure\nThe red hue is an object, perfectly spherical and the size of bowling ball. It is housed in a large... Oyster, approzimately the size of a Dumptruck. This would be fantastic for your journal.\nSoon after you begin to make an entry, a large creature grabs the oyster and pulls it deeper into the cave.\nIt leaves behind a glowing mucus... What was that?")
            self.placement += 1

        return

    def mucus(self, action):
        """Interaction with mucus"""

        if self.placement != 1:
            print("Invalid action")
            return

        if action.lower() == 'examine':
            print("Interesting substance. It appears to be harmless. It seems to give off a some light. This could be easily followed...\nPerhaps this is a trap. Or this creature really can't control what it excretes.")
        elif action.lower() == 'touch':
            print("Quiet slimy. Does not seem sticky, as it seems more like an algae. Maybe it tastes like lettuce?")
        elif action.lower() == 'follow':
            print("You travel deeper into the cave, following the mucus...")
        elif action.lower() == 'taste':
            print("You pull the slimy, algae like trail goo toward yourself. Why are you doing this? As it pulls closer and you open your mouth.\nTHUNK\nOh yeah, your wearing a helmet... There was no way you were actually going to try that... Right?")

        return

