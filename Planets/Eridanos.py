import planet
import nlp
import inventory

class Eridanos(planet.Planet):
    
    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Eridanos")        
        self.data = {
            "ravine": self.ravine_path,
            "wide path": self.river_path1,            
            "river": self.sulphur_river,
            "narrow path": self.river_path2,
            "termite mound": self.termite_mound,
            "flat cave": self.termite_left_cave,
            "short cave": self.termite_right_cave,
            
        }
        self.rooms = [0, 1, 2, 3, 4, 5, 6]
        self.placement = 0
        self.accomplished = False
        self.tool = False
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
        if object[0] is None or object[1] is None:
            print("Invalid action")
            return False

        self.data[object[1]](object[0])

        # Final actions completed, return True to let engine know to move to next planet
        if self.accomplished == True:
            return True

        # Final action not complete, so return False
        return False

    def print_welcome(self):
        
        if self.visited == False:
            print('Plunging cliffs, strange flora, roaring rapids, and the faint smell of sulphur. Welcome to '
                  'Eridanos. You have arrived on the top of a medium sized cliffside, but in the distance you can '
                  'see something that reminds you of a collosal termite mound. You start down a trail leading down '
                  'into ravine that looks like it will take you to the mound, and there appear to be several caves '
                  'along the path.')
            self.visited = True
        elif self.visited == True:
            print("Welcome back to Eridanos! You see the path to the ravine still in front of you as well as the "
                  "termite mound structure and the ravine caves.")
        return

    def ravine_path(self, action):
        """Interaction with cave"""

        if self.placement != 0:
            print("Invalid action")
            return

        if action.lower() == 'move':
            print("You walk down the ravine to the wide river path. There's a spot you could explore that goes right to the river.")
            self.placement += 1

        return

    def river_path1(self, action):
        """Interaction with mucus"""

        if self.placement != 1:
            print("Invalid action")
            return

        if action.lower() == 'explore':
            print("You go over to the river itself to see what you might be able to find.")
            self.placement += 1
        elif action.lower() == 'move':
            print("You continue on the path. You'd say the path is now a narrow path rather than wide.")
            self.placement += 2
        elif action.lower() == 'return':
            print("You head back toward the ravine path to your ship.")
            self.placement -= 1

        return
   
    def sulphur_river(self, action):
        """Interaction with cave"""

        if self.placement != 2:
            print("Invalid action")
            return

        if action.lower() == 'take':
            self.tool = True
            print("You reach into the river and pull out a tool that looks somewhat like a silver pickaxe. Definitely "
                  "keeping this.")            
        elif action.lower() == 'move':
            print("You have to get back to the river path to continue on.")
        elif action.lower() == 'return':
            print("You head back toward the river path.")
            self.placement -= 1


        return

    def river_path2(self, action):
        """Interaction with cave"""

        if self.placement != 3:
            print("Invalid action")
            return

        if action.lower() == 'follow':
            print("You continue to follow the path until you make it to the termite mound itself.")
            self.placement += 1
        elif action.lower() == 'return':
            print("You head back toward the part of the path with the river access point.")
            self.placement -= 1

        return

    def termite_mound(self, action):
        """Interaction with cave"""

        if self.placement != 4:
            print("Invalid action")
            return

        if action.lower() == 'left':
            print("You enter the left side cave of the mound.")
            self.placement += 1
        elif action.lower() == 'right':
            print("You enter the right side cave of the mound.")
            self.placement += 2
        elif action.lower() == 'return':
            print("You head back toward the river path.")
            self.placement -= 1

        return

    def termite_left_cave(self, action):
        """Interaction with cave"""

        if self.placement != 5:
            print("Invalid action")
            return

        if action.lower() == 'poke' and self.tool is True:
            print("After putting the pickaxe into the opening, a fossilized claw comes out. This is something "
                "worth noting and keeping.")
            self.accomplished = True
            inventory.add("fossilized claw")
        elif action.lower() == 'poke' and self.tool is False:
            print("It looks like you need to put something into the hole. You do see some moisture around it, "
                "as well as some silver flecks.")  
        elif action.lower() == 'return':
            print("You head back toward the clearing with your ship.")
            self.placement -= 1
        return

    def termite_right_cave(self, action):
        """Interaction with cave"""

        if self.placement != 6:
            print("Invalid action")
            return
        elif action.lower() == 'return':
            print("There's clearly nothing here. Better go back to the main entrance.")
            self.placement -= 2

        return
 
