import planet
import nlp


class Celaeno(planet.Planet):
    """The Celaeno planet"""

    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Celaeno")
        self.enter_planet()
        self.data = {
            "car": self.car,
            "well": self.well,
            "coin": self.coin,
            "door": self.door,
            "sapphire": self.sapphire
        }
        self.rooms = [0, 1, 2, 3, 4, 5]
        self.placement = 0
        self.checkpoints = [False, False, False, False, False, False, False, False]


    def action(self, text):
        """Processes an action from the user"""

        object = self.validate_user_command(text)
        if object[0] is None or object[1] is None:
            print("Invalid action")
            return False

        self.data[object[1]](object[0])

        # Final actions completed, return True to let engine know to move to next planet
        if self.checkpoints[5] is True:
            print("A portal appears...beckoning...")
            return True

        return False

    def enter_planet(self):
        print('You look around.  You feel like you are 430 light years from Earth.')
        print('You see the star of Celaeno off to the left.')
        print('There is quite the dichotomy around you:  gurgling lava to your right,')
        print('and a bubbling swamp to your left.  You get the sense that the swamp is alive, or at least')
        print('the home to VERY MANY living things of suspicious origin.')
        print('the lava (well, you THINK it is lava) shimmers between normal lava colors, as well as an odd')
        print('shade of cyan.  That is strange...color-shifting lava.')
        print('There is a very wide marble path that bifurcates the two different environments, and there appears to ')
        print('be a DeLorean directly in front of you.  The car seems strangely out of place in this world, but it')
        print('beckons to you.  You have never seen a Celaeno DeLorean before...')
        
        return
    
    def car(self, action):
        """Interaction with car"""

        if action.lower() == 'examine':
            print("It is a Delorean.  It ironically has a flux capacitor and a fusion generator,")
            print("and a copy of Grays Sports Almanac in the front seat.")
        if action.lower() == 'drive':
            print("You are now driving the car.  You accelerate to 88 miles per hour.")
            print("The time circuits explode.  You don't know where you are, but you emerge in a world where")
            print("you see frozen lava on one side, a frozen swamp on the other, and yet the climate feels")
            print("shockingly tropical.  This world is bizarre.")
            print("Thankfully, you still see the Celaeno star, although its relative position in the sky has changed.")
            print("You see a giant well and a stack of coins in front of you.")
        self.placement += 1

        return

    def well(self, action):
        """Interaction with well"""

        if action.lower() == 'examine':
            print("The well is deep.  You can see a handful of coins at the bottom.")
            self.placement += 1

        return

    def coin(self, action):
        """Interaction with coin"""

        if action.lower() == 'examine':
            print("The coin has an image of Atlas on it. You vaguely remember that Atlas was the father of Celaeno.")
            self.placement += 1

        if action.lower() == 'throw':
            print("The coin enters the well.  Nothing happens.")
            print("Minutes later, Atlas appears.  He appears to be lifting this planet on his shoulders,")
            print("which is a true mine-bender for you.  How can you simultaneously see Atlas in front of you,")
            print("HOLDING the very planet that both of you are standing on?  This world is BIZARRE.")
            print("Atlas speaks:  If the Kessel run were from here to Earth, and Earth is 430 light years away,")
            print("How many parsecs is that?")
            ans5 = input(">>")
            print("You are correct!  It absolutely would be 130 parsecs.")
            print("Atlas disappears.  A brick wall appears.  The brick wall has a brick door.")
            print("You also see a large, random sapphire on the ground.  This is odd, because the sapphire seems")
            print("to have no relevance here.  Yet, you also feel like YOU MUST TAKE IT.")

        return

    def door(self, action):
        """Interaction with door"""

        if action.lower() == 'examine':
            print("It is a brick door.  All in all, it is just another brick door in the wall.")
        elif action.lower() == 'open':
            print("After you open the brick door that is surrounded by the brick wall, you see a brick road.")
            print("The brick road is yellow.  There are three forks to the road.")
            print("One leads to an emerald city in the distance.  One leads to a chocolate factory. ")
            print("The third one leads toward what looks like a giant moon.  You think to yourself:")
            print("THAT IS NO MOON.")
            self.checkpoints[5] = True
            self.placement += 1

        return

    def sapphire(self, action):
        """Interaction with sapphire"""

        if action.lower() == 'examine':
            print("It is a beautiful sapphire.  You get the sense that it has magical powers,")
            print("but given how crazy today has been, it could be JUST ABOUT ANYTHING.  Take it!")
        elif action.lower() == 'take':
            print("You now own your very own quasi-magical sapphire!")
            self.placement += 1

        return










