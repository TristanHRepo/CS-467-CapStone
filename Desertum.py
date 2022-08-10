import planet
import nlp

class Desertum(planet.Planet):
    """The underwater planet"""

    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Subaqueanus")
        self.enter_planet()
        self.data = {
            "statue": self.statue,
            "pillar": self.statue,
            "upstream": self.upstream,
            "downstream": self.downstream,
            "contraption": self.mirror,
            "building": self.building,
            "inside": self.inside,
            "crystal": self.crystal,
            "mirror": self.mirror,
            "sundial": self.sundial,
            "picture": self.picture,
            "stone": self.stone,
            "ship": self.ship
        }

        self.directions = {
            "north": self.north,
            "south": self.south,
            "east": self.east,
            "west": self.west
        }

        self.checkpoints = [False, False, False, False, False, False]
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

        self.data[object[1]](object[0])

        # Final actions completed, return True to let engine know to move to next planet
        if self.checkpoints[5] is True:
            print("---------------------------------------------------------\n"
                  "You return to your ship!\n"
                  "10 planets done, what a journey\n"
                  "You begin to board your ship as you notice a moon pass in front of the sun\n"
                  "A beautiful solar eclipse covers the area and the desert planet turns dark and cool\n"
                  "It is amazing to behold\n"
                  "You turn on your ship and take off\n"
                  "Space really is beautiful....")
            return True

        # Final action not complete, so return False
        return False

    def upstream(self, action):
        """The area up stream"""

        if action == 'move' and self.placement == 0:
            print("You move upstream...\n"
                  "You find an area with a small building that has a window toward the North-West\n"
                  "There is no glass for the window.\n"
                  "The building has a place where a door would be also")
            self.placement = 2

        if self.placement != 2:
            print("Invalid action")
            return

        return

    def building(self, action):
        """Building actions"""

        if action == 'move' and self.placement == 0:
            self.action('move upstream')
            return

        if self.placement != 2 and self.placement != 5:
            print("Invalid action")
            return

        if action == 'examine':
            if self.placement == 5:
                self.action('examine inside')
            else:
                print("This seems to have been here for a while\n"
                      "The climate has definitely taken it's toll on the building\n"
                      "There seems to be some drawings of a man on the sun dropping a ball\n"
                      "The ball seems to land on another man who is bearing it on his shoulders\n"
                      "He seems to be trapped within a tall building with three beams pointing at the top...")

        elif action == 'enter':
            print("You enter the building and notice immediately there is a hole\n"
                  "From the hole you see a ray of light shining down onto a pedestal\n"
                  "It seems like something is missing")
            self.placement = 5

        return

    def inside(self, action):
        """Inside the building actions"""

        if self.placement != 5:
            print("Invalid action")
            return

        if action == 'examine' or action == 'explore':
            print("You survey the room and see something...\n"
                  "You notice an orange sized crystal laying on the ground")

        return

    def crystal(self, action):
        """Crystal actions"""

        if action == 'examine' and self.checkpoints[6] is True:
            print("A perfectly spherical crystal that is cloudy inside\n"
                  "it's quiet beautiful actually\n"
                  "I wonder if the crystal could be used from something")

        if self.placement != 5:
            print("Invalid action")
            return

        if action == 'examine':
            print("A perfectly spherical crystal that is cloudy inside\n"
                  "it's quiet beautiful actually\n"
                  "I wonder if the crystal could be used from something")

        elif action == 'take' and self.checkpoints[6] is False:
            print("You pick up the crystal")
            self.checkpoints[6] = True

        elif (action == "drop" or action == "use") and self.placement == 5:
            print("You place the cystal on the pedestal\n"
                  "The ray of light shines into the crystal and a light beam projects from the window\n"
                  "It seems to be shining directly at the pillar to the North")
            self.checkpoints[2] = True
            self.checkpoints[6] = False

        return

    def downstream(self, action):
        """The area down stream"""

        if action == 'move' and self.placement == 0:
            print("You move downstream...\n"
                  "You enter an area where the water curves around a tall object\n"
                  "The object stands at about four feet tall and has a large concave mirror\n"
                  "You notice that the mirror projects a beam of light from the sun")
            self.placement = 3
            return

        if self.placement != 3:
            print("Invalid action")
            return

        return

    def mirror(self, action):
        """Actions for the mirror"""

        if action == 'move' and self.placement == 0:
            self.action('move downstream')
            return

        if self.placement != 3:
            print("Invalid action")

        if action == 'examine':
            print("An interesting contraption that seems to be used for projecting the sun's light\n"
                  "It appears to be attached to a swivel on the base\n"
                  "The contraption has two handles that look to be for positioning purposes")

        elif (action == 'turn' or action == 'use') and self.checkpoints[0] is True:
            print("You begin to turn the mirror toward the pillar you found from earlier\n"
                  "As you turn the mirror, you notice the light beam and get an idea of how to work this thing\n"
                  "Finally you position the mirror to shine the beam of light at the pillar\n"
                  "The pillar seems to accept the light")
            self.checkpoints[3] = True

        return

    def sundial(self, action):
        """sundial actions"""

        if action == 'move' and self.placement == 1:
            print("You go past the statue to the North\n"
                  "As you make you way up the hill, you see a a large stone platform with a sundial in the middle\n"
                  "The platform has a picture of a sun around the sundial\n"
                  "You see that the picture color around the edge of the sun\n"
                  "The North side of the sun picture has a light yellow color\n"
                  "This color gradually turns into an intense red color at the South\n"
                  "The red side of the sun also seems to be reaching toward the South")
            self.placement = 4

        if self.placement != 4:
            print("Invalid action")
            return

        if action == 'examine':
            print("You see a beautiful sundial with color on top\n"
                  "The sundial has the same picture as the platform that you are standing on\n"
                  "However, the red side of the sun and the Gnomon of the sundial face North\n"
                  "You also notice that the face of the sundial can be turned")

        if action == 'turn':
            print("You turn the sundial..\n"
                  "As you make your revolution you notice the sundial lock in place\n"
                  "This happens when the picture on the sundial matches the picture on the platform\n"
                  "You then see a ray of light project from the tip of the Gnomon into the pillar to the South\n")
            self.checkpoints[1] = True

        return

    def picture(self, action):
        """Picture actinos"""

        if self.placement != 4:
            print("Invalid action")
            return

        if action == 'examine':
            print("You see the picture of the sun around the sundial\n"
                  "You see that the picture color around the edge of the sun\n"
                  "The North side of the sun picture has a light yellow color\n"
                  "This color gradually turns into an intense red color at the South\n"
                  "The red side of the sun also seems to be reaching toward the South")

        return

    def statue(self, action):
        """The statue to the North"""

        if action == 'move' and (self.placement == 0 or self.placement == 2):
            print("You approach the formation...\n"
                  "The formation turns out to be some kind of carved pillar about 15 feet high.\n"
                  "At the top of the pillar you see three holes one facing North\n"
                  "The other two point South-East and South-West, toward the channel of water\n"
                  "The Pillar also seems to have a carved entry way\n"
                  "To the north you see a small hill with what looks like a sundial.")
            self.placement = 1

        if self.placement != 1:
            print("Invalid action")
            return

        if self.checkpoints[1] is True and self.checkpoints[2] is True and self.checkpoints[3] is True:
            print("You see three beams of light entering the top of the pillar\n"
                  "As you approach the statue, you realize that the carved entry way has opened\n"
                  "Inside you see a pair of hands holding an apple sized rock\n"
                  "There is a picture on the floor of a large man crushing a boulder\n"
                  "The pictures show the man finally compressing the boulder into a small stone...")
            self.checkpoints[4] = True
            return

        if action == 'examine':

            print("An interesting pillar with calligraphy all over it.\n"
                  "The entry way is closed but seems like it could be opened\n"
                  "You look up and see..")

            if self.checkpoints[1] is False and self.checkpoints[2] is False and self.checkpoints[3] is False:
                print("Three holes, one facing North, one South-East, and one South-West")
                return

            if self.checkpoints[1] is True:
                print("You see a beam of light entering the pillar from the South-West")
            if self.checkpoints[2] is True:
                print("You see a beam of light entering the pillar from the South-East")
            if self.checkpoints[3] is True:
                print("You see a beam of light entering the pillar form the North")

            print("Maybe if I fill all three holes with beams of light...")

        return

    def stone(self, action):
        """Stone actions"""

        if self.placement != 1:
            print("Invalid action")
            return

        if self.checkpoints[1] is False or self.checkpoints[2] is False or self.checkpoints[3] is False:
            print("Invalid action")
            return

        if action == 'examine':
            print("A spherical stone the is perfectly smooth\n"
                  "It glows with a faint orange hue\n"
                  "Maybe it is the stone depicted in the picture???\n"
                  "This seems like a perfect artifact to keep from this planet for the journal")

        elif action == 'take':
            print("You pick up the sphere...\n"
                  "It is surprisingly heavy!\n"
                  "I think that is all for this planet!")
            self.checkpoints[5] = True

        return

    def ship(self, action):
        """Ship actions"""

        if action == 'move' or action == 'return':
            print("You return to your ship..."
                  "With this planets sun established as your North, the water runs to the West\n"
                  "To the West is where you see some kind of contraption\n"
                  "Behind you is your ship, and East would be upstream where a small building is.\n"
                  "You notice to the North a large, un-natural formation")
            self.placement = 0

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
              "To the West is where you see some kind of contraption\n"
              "Behind you is your ship, and East would be upstream where a small building is.\n"
              "You notice to the North a large, un-natural formation")

        return

    def north(self):
        """Go north options"""

        if self.placement == 0:
            self.action('move statue')
        elif self.placement == 1:
            self.action('move sundial')
        else:
            print("Can't go North from here")

        return

    def south(self):
        """Go south options"""

        if self.placement == 4:
            self.action('move statue')
        elif self.placement == 1:
            self.action('move ship')
        else:
            print("Can't go South from here")

        return

    def east(self):
        """Go east options"""

        if self.placement == 0:
            self.action('move upstream')
        else:
            print("Can't go East from here")

        return

    def west(self):
        """Go west options"""

        if self.placement == 0:
            self.action('move downstream')
        else:
            print("Can't go West from here")

        return
