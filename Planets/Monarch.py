import planet
import nlp
import inventory

class Monarch(planet.Planet):
    
    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Monarch")        
        self.data = {
            "clearing": self.clearing,
            "archway": self.tree_archway,
            "tunnel": self.tree_tunnel,
            "upper path": self.north_path,
            "lower path": self.southeast_path,
            "plain": self.desolate_plain,
            "grove": self.pleasant_jungle_grove

        }
        self.rooms = [0, 1, 2, 3, 4, 5, 6]
        self.placement = 0
        self.accomplished  = False
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
            print('As you made you way to land on Monarch, you noticed it was tidally locked toward its sun, '
                  'but at the terminator line had a lush jungle, so that is where you find yourself now. From up '
                  'high, the trees were unlike anything you have ever seen, but still comfortably familiar at the '
                  'same time.')
            self.visited = True
        elif self.visited == True:
            print("You have returned to the terminator line jungle on Monarch, still full of those fascinating "
                  "flowers and bees.")
        return

    def clearing(self, action):
        """Interaction with clearing"""

        if self.placement != 0:
            print("Invalid action")
            return

        if action.lower() == 'look':
            print("You're in awe of the natural beauty around you. However, you realize that that the forest is too "
                  "think to traverse, other than through the tree archway.")
        elif action.lower() == 'move':
            print("You walk over to the archway itself. It is truly magnificent to behold. You can't see where the "
                  "archway leads to, but the plant life is thin enough you can cross through it.")
            self.placement += 1

        return

    def tree_archway(self, action):
        """Interaction with archway"""

        if self.placement != 1:
            print("Invalid action")
            return

        if action.lower() == 'enter':
            print("You find yourself now walking through a tunnel of trees. The shafts of light coming throgh the "
                  "upper canopy are beautiful. Despite only being on a terminal ring, this might be the most "
                  "beautiful planet you've been to. After a while, you come across a fork in the tunnel. One leads "
                  "north and the other southeast.")
            self.placement += 1
        elif action.lower() == 'return':
            print("You head back toward the clearing with your ship.")
            self.placement -= 1

        return

    def tree_tunnel(self, action):
        
        if self.placement != 2:
            print("Invalid action")
            return

        if action.lower() == 'north':
            print("You head off in the northern tunnel.")
            self.placement += 1
        elif action.lower() == 'southeast':
            print("You head off southeast. The air seems to be getting more dry, and the plants a little less healthy "
                  "and sparse.")
            self.placement = 4
        elif action.lower() == 'return':
            print("You head back toward the tree archway entry.")
            self.placement -= 1

        return

    def north_path(self, action):
        
        if self.placement != 3:
            print("Invalid action")
            return

        if action.lower() == "north":
            print("You continue north along to path. As you get closer to the end, you start to hear a faint buzzing "
                  "noise. As you you reach the end of the path, you come out into a pleasant jungle grove, "
                  "filled with a number of bee-like insects. You certainly didn't expect this!")
            self.placement += 3
        elif action.lower() == 'return':
            print("You head back toward the tunnel split.")
            self.placement -= 1
            
        return

    def southeast_path(self, action):
        
        if self.placement != 4:
            print("Invalid action")
            return

        if action.lower() == 'southeast':
            print("And then you reach the end. Of course. You just had to forget you were on a narrow ring. Before "
                  "you is the desolate daylight side of the planet you should probably head back. Quickly.")
            self.placement += 1
        elif action.lower() == 'return':
            print("You head back toward the tunnel split.")
            self.placement = 2

        return

    def desolate_plain(self, action):
        
        if self.placement != 5:
            print("Invalid action")
            return

        if action.lower() == 'return':
            print("You immediately head back toward the split in the tunnel. You do not want to stick around here for "
                  "very long.")
            self.placement -= 1
        elif action.lower() == 'examine':
            print("This is not an area you want to be in for long. It is hot, desolate, and that sun in going "
                  "nowhere. Time to head back.")
        

        return

    def pleasant_jungle_grove(self, action):
        """Interaction with grove"""

        if self.placement != 6:
            print("Invalid action")
            return

        if action.lower() == 'take':
            print("You've managed to gently grab the bee-like insect, though that sting in your hand in unpleasant. "
                  "And you're actually feeling better now, rather than worse. A rather unexpected outcome. This is "
                  "worth keeping.")
            self.accomplished = True  
            inventory.add("insect")      

        return
