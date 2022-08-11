import planet
import inventory


class Pleione(planet.Planet):
    """The crystal planet"""

    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Pleione")
        self.visited = False
        self.print_welcome()
        self.data = {
            "golden flower": self.flower,
            "flower": self.flower,
            "grey patch": self.patch,
            "dull grey patch": self.patch,
            "patch": self.patch,
            "flowers": self.flowers,
            "crystal shard": self.shard,
            "shard": self.shard,
            "sparkle": self.sparkle,
            "crystal": self.crystal,
            "red crystal": self.crystal,
            "small red crystal": self.crystal
        }
        self.directions = {
            "north": self.north,
            "south": self.south,
            "east": self.east,
            "west": self.west
        }
        self.cured = False
        self.rooms = [0, 1, 2, 3]
        self.placement = 0

    def query_NLP(self, text):
        """Placeholder function to query natural language parser."""

        value = self.validate_user_command(text)
        action = text.rsplit()
        return action

    def action(self, text):
        """Processes an action from the user"""
        obj = self.validate_user_command(text)
        if obj[0] is None:
            print("Invalid action")
            return False

        if obj[1] is None:
            if obj[0] in self.directions:
                self.directions[obj[0]]()
                return False

        self.data[obj[1]](obj[0])

        # Final Action:
        if self.placement == 3:
            print("---------------------------------------------------------\n"
                  "You board your ship and make way for the sandy-colored star to the east. \n"
                  "You have a feeling that you are nearing the end of your journey... \n"
                  "---------------------------------------------------------\n")
            return True

        return False

        # DEFAULT:
        # return False

    def print_welcome(self):
        """
        Prints the room's long description if it hasn't been visited before, or if 'look' is input.
        Otherwise prints the room's short description.
        """
        if not self.visited:
            print("Your ship lands on a yellow-hued planet. As you exit your ship, you see that the surface of the "
                  "planet is virtually covered in golden flowers, bobbing gently in the apparent breeze. Each flower "
                  "has four petals and a round, ruffled shape. The field of flowers nearly reaches your knees. The "
                  "ground is thickly coated with flowers, but they easily yield to your touch, should you wish to "
                  "push them aside. \n\nTo the north, you can make out a dull grey patch on the surface. The ground "
                  "seems patchy, as though the flowers are not so dense there. Towards the east, you can see a blue "
                  "planet looming close in the sky.\n")
            print("Push the flowers aside?")
            self.visited = True
        else:
            if self.cured:
                print("You land on a planet lush with golden flowers.\n"
                      "All the flowers are uniformly healthy.\n"
                      "There is a blue planet in the near east. ")
            else:
                print("You land on a planet lush with golden flowers. \n"
                      "There is a dull grey patch to the north. \n"
                      "There is a blue planet in the near east. ")

    def flowers(self, action):
        """Interaction with flowers"""

        if self.placement != 0:
            print("There are no living flowers here!")
            return

        act = action.lower()
        if act == 'push':
            print("You part the flowers where you stand. Beneath the petals, you find a tiny fragment of a red "
                  "crystal. It's a shard. You sense that it is warm to the touch. This seems familiar... ")
            if inventory.check("red crystal"):
                print("It looks identical in makeup to the red crystals you saw on Atlas. The only difference is that "
                      "this one is even smaller, a tiny crystal shard.\n"
                      "Together with the whole crystal you picked up earlier, you could produce a significant amount of"
                      " heat. ")
            self.placement += 1

        elif act == 'examine':
            print("A dense field of golden flowers that have a magical quality to them. Nearly the whole planet is "
                  "covered in these flowers, such that it's hard to see the ground beneath.")

    def shard(self, action):
        """ Interaction with crystal shard """
        if self.placement != 1:
            print("You cannot do that now!")
            return

        act = action.lower()
        if act == 'touch':
            print("You gingerly touch the crystal shard on the ground. It's tiny, but you can sense great heat "
                  "emanating from it.")

        elif act == 'examine':
            print("The crystal shard on the ground is tiny, with jagged edges and a slight sparkle. It glitters in the "
                  "faint starlight. It has a faint heat coming from it. Haven't you seen something like this somewhere "
                  "before?")

        elif act == 'take':
            print("You grab the tiny crystal and add it to your inventory. ")
            inventory.add("crystal shard")

    def patch(self, action):
        """Interaction with grey patch"""

        act = action.lower()
        if act == 'move':
            print("You make your way northward, and find that the flower petals here have turned grey. The flowers "
                  "appear to be wilting and dying, and as a result it is easier to see the earth beneath. You sense "
                  "that the temperature in this area has sharply dropped. On the surface, you can see a sparkle. ")
            self.placement += 1

        elif act == 'examine':
            print("A patch of land on the planet Pleione where all of the flowers covering the surface have turned "
                  "dull, grey, and lifeless. They wilt in death. You think you can detect a hint of frost on their "
                  "petals.\n"
                  "Because the flowers are not so thick here, you can see the earth beneath. Your eyes catch on a "
                  "sparkle on the surface. ")

        elif act == 'talk':
            print("The dull grey patch doesn't respond to you. ")

        elif act == 'taste':
            print("You really shouldn't eat these dead flowers. You don't know what's happened to them! ")

        elif act == 'touch':
            print("You reach out and grab one of the flowers. Its wilted petals crumble to dust between your fingers. ")

    def sparkle(self, action):
        """ Interaction with sparkle """
        if self.placement != 2:
            print("You're not in the right place for that. You're: ", self.placement)
            return

        act = action.lower()
        if act == 'take':
            print("Try as you might, you cannot pick up the sparkle. What is it, anyway? You should get a "
                  "closer look. ")

        elif act == 'examine':
            print("On closer examination, the sparkle appears to be a crystalline receptacle. There is an indentation "
                  "in the middle of the receptacle. It seems like something small and round would perfectly fit into "
                  "the indentation. A shard is too small, but maybe a whole crystal will do... ")

    def crystal(self, action):
        """ Interaction with crystal in inventory """
        act = action.lower()
        if act == 'drop' or act == 'use':
            if self.placement == 2:
                print("You fit the small red crystal into the indentation. It's a perfect fit! \nAs the red crystal is "
                      "placed into the receptacle, it sparkles, and the surrounding flowers seem to glow as they are "
                      "flooded with life.\nYou sense that the temperature has risen. The flowers have been restored to "
                      "their full colors.\nYou brought them back to life!")
                self.cured = True
                self.placement += 1
            else:
                print("You can't use that here. ")

        elif act == "examine":
            print("You have a small, round, red crystal in your inventory. You remember that you picked it up when "
                  "you found it floating on Atlas. It has a faint shimmer to it, and you can sense that it gives off "
                  "considerable heat.\n"
                  "It seems that this crystal is attuned to fire magic.")

    def flower(self, action):
        """ Interaction with individual flower """
        act = action.lower()
        if act == 'take' or act == 'pull':
            print("You pick a golden flower from the surface, and add it to your inventory. ")
            inventory.add("golden flower")

        elif act == 'examine':
            print("A pretty golden flower that has a magical property to it. It glows with life. ")

    def north(self):
        """ Go north """
        if self.placement == 0 or self.placement == 1:
            self.action("go dull grey patch")
        else:
            print("You can't go north right now. ")

    def south(self):
        """ Go south """
        print("You can't go south right now. ")

    def east(self):
        """ Go east """
        if self.placement < 3:
            print("You really ought to investigate the dull grey patch before you leave...")

    def west(self):
        """ Go west """
        print("You've already been west! You should explore elsewhere for now. ")
