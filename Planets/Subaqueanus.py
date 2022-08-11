import planet
import nlp
import inventory

class Subaqueanus(planet.Planet):
    """The underwater planet"""

    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Subaqueanus")
        self.enter_planet()
        self.data = {
            "cave": self.cave,
            "mucus": self.mucus,
            "sculpture": self.sculpture,
            "sculptures": self.sculpture,
            "pearl": self.pearl,
            "sphere": self.pearl,
            "junk": self.junk,
            "tool": self.tools,
            "part": self.parts,
            "parts": self.parts,
            "tools": self.tools,
            "ship": self.ship
        }

        self.directions = {
            "north": self.north,
            "south": self.south,
            "east": self.east,
            "west": self.west
        }

        self.checkpoints = [False, False, False, False, False, False, False, False]
        self.placement = 0

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

        self.data[object[1]](object[0])

        # Final actions completed, return True to let engine know to move to next planet
        if self.checkpoints[6] is True and self.checkpoints[7] is True:
            print("---------------------------------------------------------\n"
                  "With your ship repaired and an interesting artifact from the planet you board your ship\n"
                  "As you get ready to take off to the next planet, you notice the creature\n"
                  "It is waving to you through the window\n"
                  "Your ship struggles but then quickly gains speed\n"
                  "You notice your new friend helping you gain thrust by pushing your ship!\n"
                  "You finally emerge from the water, and being your ascent into the sky\n"
                  "On to the next planet!\n"
                  "---------------------------------------------------------\n")
            return True

        # Final action not complete, so return False
        return False

    def cave(self, action):
        """Interaction with cave"""

        if (action.lower() == 'move' or action.lower() == 'south') and self.checkpoints[3] is True:
            print("And there is the ship. Still broken.\n"
                  "Hopefully I can repair that soon.")
            self.placement = 0

        elif (action.lower() == 'move' or action.lower() == 'south') and self.checkpoints[1] is True:
            print("You return to the entrance of the cave.\n"
                  "Somehow you feel more exposed than when you were in the cave as you return to the deep\n"
                  "You move your headlamp in the direction of your ship and notice the creature from in the cave.\n"
                  "Your headlamp causes the creature to flee once more, this time into the open ocean.\n"
                  "As you approach your ship, you notice it was taking parts of your ship.\n"
                  "A few panels have been damaged, but this looks repairable...\n"
                  "If only you had some tools and ship parts.")
            self.checkpoints[3] = True
            self.placement = 0
            return

        elif (action.lower() == 'move' or action.lower() == 'south') and self.checkpoints[0] is True:
            print("You return to the entrance of the cave.\n" \
            "Nothing really interesting out here except your ship.")
            self.placement = 0
            return

        if self.placement != 0:
            print("Invalid action")
            return

        if action.lower() == 'move' or action.lower() == 'north':
            print("You move closer to the cave. At it's entrance you notice that the cave is dimly illuminated\n"
                  "by an interesting fungus with small tentacles, and at tip of each tentacle is a small bulb\n"
                  "giving off faint white light.\n"
                  "Further in the cave you notice something much larger giving off a red hue.")
        elif action.lower() == 'examine':
            print("A dark cave. The opening must be at least 15ft in diameter. Maybe something of\n"
                  "interest lies within?")
        elif action.lower() == 'enter':
            if self.checkpoints[1] is False:
                print("You enter the cave.\n"
                      "Your suit's light giving off a narrow cone of light ahead of you, you begin to descend.\n"
                      "As you begin to descend, you notice the tentacles with lights reaching toward you\n"
                      "The red hue begins to increase in size.\n"
                      "You approach carefully, not wanting to disturb whatever lies ahead.\n"
                      "Finally, you begin to see a figure\n"
                      "The red hue is an object, perfectly spherical and the size of bowling ball.\n"
                      "It is housed in a large... Oyster, approximately the size of a car.\n"
                      "This would be fantastic to take as an artifact for the planet!\n"
                      "Soon after you begin to make examine the object you notice something\n"
                      "A large creature grabs the oyster and pulls it deeper into the cave.\n"
                      "It leaves behind a glowing mucus...\n"
                      "What was that?")
                self.placement += 1
                self.checkpoints[0] = True
            elif self.checkpoints[1] is True:
                print("You enter the cave.\n"
                      "You return to the room with the glowing sphere on top of the pile of junk.\n"
                      "Maybe something of use is in the junk pile.\n"
                      "Also, there are the sculptures.")
                self.placement = 2

        return

    def mucus(self, action):
        """Interaction with mucus"""

        if self.placement != 1:
            print("Invalid action")
            return

        if action.lower() == 'examine':
            print("Interesting substance. It appears to be harmless. It seems to give off a some light. This could be "
                  "easily followed...\nPerhaps this is a trap. Or this creature really can't control what it excretes.")
        elif action.lower() == 'touch':
            print("Quiet slimy. Does not seem sticky, as it seems more like an algae. Maybe it tastes like lettuce?")
        elif action.lower() == 'follow':
            print("You travel deeper into the cave, following the mucus...\n"
                  "The trails ends at what appears to be the end of the cave.\n"
                  "As you scan the room, it full of sculptures made from scrap parts.\n"
                  "You also see the red glowing sphere a top a large pile of junk... and the creature\n"
                  "The creature takes notice of you.\n"
                  "Quickly it runs toward you... Is this it?\n"
                  "But as soon it comes upon you, it runs past you.\n"
                  "It seems safe for now.")
            self.placement += 1
            self.checkpoints[1] = True
        elif action.lower() == 'taste':
            print("You pull the slimy, algae like trail goo toward yourself. Why are you doing this? As it pulls closer"
                  " and you open your mouth.\nTHUNK\nOh yeah, your wearing a helmet... There was no way you were "
                  "actually going to try that... Right?")
        elif action.lower() == 'return' or action.lower() == 'south':
            print("You return to the mouth of the cave...")
            self.placement -= 1

        return

    def junk(self, action):
        """Junk actions"""
        
        if self.placement != 2:
            print("Invalid action")
            return

        if action.lower() == 'explore' or action.lower() == 'examine':
            print("You look through the junk pile.\n"
                  "You find many trinkets and... ship parts?\n"
                  "You also find some tools?\n"
                  "Does this creature know how to use tools?? Does it have a ship?")
            self.checkpoints[2] = True

        return

    def sculpture(self, action):
        """sculpture actions"""

        if self.placement != 2:
            print("Invalid action")
            return

        if action.lower() == 'examine':
            print("As you examine the sculptures, you notice the fine details added to each sculpture.\n"
                  "Some sculptures seem to be of other creatures, some just interesting shapes, and some of...\n"
                  "Ships. Interesting.")

        elif actino.lower() == 'break':
            print("I could break some of these sculptures but then what?\n"
                  "I don't want to anger the creature.")

        return

    def pearl(self, action):
        """Pearl actions"""

        if self.placement != 2:
            print("Invalid action")
            return

        if action.lower() == 'examine':
            print("A pearlescent sphere, the size of a bowling ball.\n"
                  "The object itself has a redish pink color to it with a red aura around it.\n"
                  "This would be an awesome item to take with me, but it is way to heavy.\n"
                  "Perhaps I could break piece off?")

        elif action.lower() == 'take':
            print("You attempt to move the sphere...\n"
                  "It does not budge. This thing is HEAVY.\n"
                  "Maybe I could just take a piece with me?")

        elif action.lower() == 'break' and self.checkpoints[4] is False:
            print("You line up your hand with the sphere.\n"
                  "You take a deep breathe and raise your hand above your head.\n"
                  "You swing your hand with all your might.\n"
                  "OUCH\n"
                  "As your hand connects with the sphere, you feel pain in your hand.\n"
                  "Perhaps karate chopping this, or just using your body in general, is not the correct way to do this.")

        elif action.lower() == 'break' and self.checkpoints[4] is True:
            print("You take out the hammer from the tool set and line it up with the sphere\n"
                  "You swing down as hard as you can and manage to chip off a piece of the sphere\n"
                  "As you examine the piece, you notice that it shipped into a perfect prism.\n"
                  "This will be a great artifact for this planet! You store the prism away in your inventory.")
            self.checkpoints[7] = True
            inventory.add("prism")
        return

    def tools(self, action):
        """Tool methods"""

        if action.lower() == 'examine' and self.checkpoints[4] is True:
            print("Some tools that I found in the cave. I wonder how they got on this planet?")
            return

        if self.placement != 2:
            print("Invalid action")
            return

        if action.lower() == 'take' and self.checkpoints[2] is True and self.checkpoints[4] is False:
            print("You grab the tools. Perhaps they could be of use.")
            self.checkpoints[4] = True

        elif action.lower() == 'examine' and self.checkpoints[2] is True:
            print("A hammer, a screwdriver set, and various other tools.")

        return

    def parts(self, action):
        """Ship Parts interactions"""

        if action.lower() == 'examine' and self.checkpoints[5] is True:
            print("Some ship parts I found in the cave. It seems I'm not the first to visit this place.")
            return

        if self.placement != 2:
            print("Invalid action")
            return

        if action.lower() == 'take' and self.checkpoints[2] is True and self.checkpoints[5] is False:
            print("Maybe I could use these spare ship parts in the future? You can never be too safe!")
            self.checkpoints[5] = True

        elif action.lower() == 'examine' and self.checkpoints[2] is True:
            print("Looks like some panels and materials that could be retro fitted on my ship if needed.")

        return

    def ship(self, action):
        """Ship actions"""

        if action.lower() == 'return':
            print("You begin your journey back to the ship..")
            self.action('move cave')

        if self.placement != 0:
            print("Invalid action")
            return

        if action.lower() == 'examine':
            if self.checkpoints[3] is True:
                print("I can't believe that creature dismantled pieces of my ship.\n"
                      "Luckily the damage is minimal, but it does need to be repaired before I can leave\n"
                      "Maybe there is some scrap parts I can find around here?")
            else:
                print("Ah what a beauty. I can't believe this thing works underwater.")
        elif action.lower() == 'repair' and self.checkpoints[3] is True:

            if self.checkpoints[4] is True and self.checkpoints[5] is True:
                print("You use the tools and the ship parts from the cave and work on your ship.\n"
                      "As you are working, you notice the creature curiously observing you from a distance\n"
                      "It is quite terrifying considering this creature is the size of a dump truck\n"
                      "After some time, the creature slowly brings you a piece of the ship. \n"
                      "It seems to be trying to help!\n"
                      "With the creatures help you finish repairing your ship!\n"
                      "As soon as you finish the creature takes the remaining peaces of the ship that were not used "
                      "and swims away\n"
                      "It seems like you made a friend?")
                self.checkpoints[6] = True
            elif self.checkpoints[4] is False and self.checkpoints[5] is True:
                print("Well I have the parts, but no tools to repair this ship with.\n"
                      "Why do these space ship teams never carry tools with them?\n"
                      "Maybe there is something in the cave I could use?")
            elif self.checkpoints[4] is True and self.checkpoints[5] is False:
                print("I have some tools, but I need parts also.\n"
                      "The parts that the creature tore off are too damaged to use again\n"
                      "Maybe there is something else I could use in the cave?")
            else:
                print("Why don't they ever send these ships with repair kits?\n"
                      "Maybe I can find something of use in the cave?")

        elif action.lower() == 'enter' or action.lower() == 'use':
            print("I should find something of interest here before I get back in the ship to leave.")

        return

    def enter_planet(self):
        """Prints the welcome for the planet"""

        print("You step out of the ship.\n"
              "Your senses are immediately dampened as you enter darkness.\n"
              "The environment here feels viscous. Could it be?\n"
              "You turn the head lamp of your suit on and see a bubble floating straight up.\n"
              "You are under water.\n"
              "You observe your surroundings and see you are completely submerged in a large body of water.\n"
              "The ship closes behind you.\n"
              "Under your feet is a sandy floor.\n"
              "No signs of life yet, but the environment leaves you feeling vulnerable.\n"
              "You establish North on this planet using your onboard compass system.\n"
              "To the North you see an opening in the world. A dark abyss. It seems to be some type of cave.\n"
              "To the South, you see your ship.")

        return

    def north(self):
        """Go north options"""

        if self.placement == 0:
            self.action('enter cave')
        elif self.placement == 1:
            self.action('follow mucus')
        else:
            print("Can't go North from here")

        return

    def south(self):
        """Go south options"""

        if self.placement == 2:
            self.action('return ship')
        elif self.placement == 1:
            self.action('return ship')
        else:
            print("Going into the deep blue from here seems scary\n"
                  "I think I should stick to this area")
        return

    def east(self):
        """Go east options"""

        if self.placement == 0:
            print("I could go East, but what about that awesome cave ahead?")
        else:
            print("There is no East in this cave!")

        return

    def west(self):
        """Go west options"""

        if self.placement == 0:
            print("I could go West, but what about that awesome cave ahead?")
        else:
            print("There is no West in this cave!")

        return
