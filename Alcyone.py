import planet
import nlp


class Alcyone(planet.Planet):
    """The Alcyone planet"""

    def __init__(self):
        """Call inheritance from parent class"""

        super().__init__("Alcyone")
        self.enter_planet()
        self.data = {
            "trident": self.trident,
            "seal": self.seal,
            "bubble": self.bubble,
            "rock": self.rock,
            "paper": self.paper,
            "scissors": self.scissors,
            "wall": self.wall,
            "poseidon": self.poseidon

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
        print('You look around.  You get the sense that gravity does not exist, but you know that it must.')
        print('You are surrounded by a light violet mist, and apparently are suspended in a giant bubble.')
        print('The bubble material is transparent, and in the distance you see the star Alcyone of the Pleiades system.')
        print('It seems strange to just KNOW that, but it is as if something else is *involved* with your thoughts.')
        print('It feels like you are hooked up to some wireless version of a virtual reality machine, and images')
        print('are being beamed into your head.  You get the sense that you can *will* yourself in any direction.')
        print('You scan the inner surface of your bubble, and their appears to be large seals to your left and right.')

        
        return

    
    def bubble(self, action):
        """Interaction with bubble"""

        if action.lower() == 'examine':
            print("It is a bubble...nothing interesting here.  Maybe you should LOOK SEAL :)")
        self.placement += 1

        return

    def seal(self, action):
        """Interaction with seal"""

        if action.lower() == 'examine':
            print('There is some writing on the seal.  It references Mount Cyllene.')
            print('There is a small trident floating near the seal.')
            self.placement += 1
        return

    def trident(self, action):
        """Interaction with trident"""

        if action.lower() == 'examine':
            print('The trident resembles, well, a TRIDENT.  It reminds you a bit of Thors hammer, but it is')
            print('most certainly shaped like a trident.  You are suddenly craving chocolate milk, you hear a')
            print('voice that says <there is no Dana, only Zuul>, and you feel COMPELLED to take that trident.')

        if action.lower() == 'take':
            print('You now hold the trident')
            self.placement += 1
            print('A shimmering head descends from above you.  Your brain flashes an image of Poseidon, and you know')
            print('That it is him.  "I loved her.  I truly did", the giant gaseous image of Poseidon exclaims.')
            print('Will you play rock-paper-scissors with me?')
            ans4 = input(">>")
            print('Poseidon throws down a ROCK.  You get the sense that he does not know how to play this game.')
            print('What is your choice?  (enter ROCK, PAPER, or SCISSORS')
            ans5 = input(">>")
            print('You are slightly amused.  Poseidon concedes, and apparently he was prepared to concede')
            print('independent of your choice.  He disappears, and the trident appears to vibrate.')
            print('Suddenly, the sphere vanishes.  All Newtonian laws of physics return.  You are in a room.')
            print('All you can see in the room is a wall.')

        return

    def wall(self, action):
        """Interaction with wall"""

        if action.lower() == 'examine':
            print('The wall has an indentation.  It is remarkably the same size and shape of the pentagonal tablet.')
            print('You see Greek letters that spell the name ALCYONE.  This is odd, because you are convinced that')
            print('you have never been able to read Greek.  Something clearly is messing with your head!')
            ans55 = input(">>")
            print('Before we consider that choice, your trident is vibrating.  Again.')
            print('It appears that this is not a weapon, however, as it suddenly projects a hologram')
            print('of a younger, more charming version of Poseidon.')
            print('Poseidon speaks.  Help me!  I must retain my past glory!')

            print('What is the name of my true love?')
            ans9 = input(">>")
            if ('Alcyone' in ans9) or ('alcyone' in ans9):
                print('Success!')
                print('Poseidon says:  Yes, or, at least I hope so!  I am quite the narcissist, but I believe')
                print('I was capable of love.  But hey, mythology can be confusing, especially when you are forever')
                print('stuck as a hologram thousands of years in the future in a star system named after your favorite')
                print('girl and her other sisters!')
                print('The room begins to vibrate.  A very large set of rock, paper, and scissors appear.')
            else:
                print('Try typing: answer poseidon')
                self.placement = 5

        return

    def poseidon(self, action):
        """Interaction with poseidon"""

        if action.lower() == 'answer':
            print("Poseidon speaks again:  What is the name of my true love?")
            ans8 = input(">>")
            print('You typed' + ans9 + 'but I hear what I want to hear!')
            print('Poseidon says:  I think I heard ALCYONE from you!  Yes, or, at least I hope so!')
            print('I am quite the narcissist, but I believe')
            print('I was capable of love.  But hey, mythology can be confusing, especially when you are forever')
            print('stuck as a hologram thousands of years in the future in a star system named after your favorite')
            print('girl and her other sisters!')
            print('The room begins to vibrate.  A very large set of rock, paper, and scissors appear.')

            self.placement += 1

        return

    def rock(self, action):
        """Interaction with rock"""

        if action.lower() == 'take':
            print('WRONG CHOICE')
        return

    def paper(self, action):
        """Interaction with paper"""

        if action.lower() == 'take':
            print('Success!')
            print('You have defeated Poseidon and earned the undying respect of Alcyone!')
            self.checkpoints[5] = True
        return

    def scissors(self, action):
        """Interaction with scissors"""

        if action.lower() == 'take':
            print('WRONG CHOICE')
        return
