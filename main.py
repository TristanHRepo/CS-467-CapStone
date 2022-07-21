#Gary Lutwen
#CS 467
#Maia Room
#Updated 21 July 2022


import time
from random import seed
from random import randint

seed(1)


def print_intro(room):
    # Placeholder to draw on specific room intro
    print('You feel groggy.  You slowly sit up and look around.  You are in what appears to be an antique spaceship.')
    print('The ground is metallic with a hint of rust, and through a window you can see what looks like')
    print('the star Maia of the Pleiades system.  It reminds you of pictures you saw in an old textbook from')
    print('the James Webb telescope from back in the 21st century.')
    print('There appears to be two pools of crystal-clear water on either side of you')
    print('which seems odd for an antique spaceship floating through this star system.')
    print('A big pool is to your right, and the small pool is to your left.')
    print('There appears to be something on the cave wall, and a man encased in carbonite is between you')
    print('and the window.  The man reminds you of a legendary archaeologist from 20th century cinema.')
    print('You get the sense that someone is playing an elaborate practical joke on you')
    print('by conflating a few different things that do not quite belong together.')

print_intro(1)

player = "Gary"
key = 0
die = 0

print('What is your name?')
player = input(">>")


print(player + '!  There is a vibranium key next to the carbonite man, and a cylindrical object with a button.')

# take or get key

ans2 = input(">>")
# if take/get exists, and also key...

if (('get' in ans2) or ('take' in ans2)) and ('key' in ans2):
    print('Success!')
    print('You now hold the key')
    key = 1

if (('get' in ans2) or ('take' in ans2)) and (key == 0):
    print('You cannot seize that item!')


ans3 = input(">>")
print('The small pool has a treasure chest submerged in the water.')

ans4 = input(">>")
print('The chest appears to have a keyhole.  The size of the keyhole appears to match the size of the key.')

ans5 = input(">>")
print('The chest has a stone tablet.  It is shaped like a pentagon.  There is a winged foot on the tablet')

ans44 = input(">>")
print('You now have the tablet.')

ans6 = input(">>")
print('I do not understand that command.')

ans33 = input(">>")
print('You have: key, tablet')

time.sleep(4)

ans7 = input(">>")
print('The wall has an indentation.  It is remarkably the same size and shape of the pentagonal tablet.')
print('There is also a winged foot engraved on the wall of the ship.')

print('The cylindrical object with a very pushable button starts vibrating.')
ans55 = input(">>")
print('A powerful blue beam emerges from what looks like a lightsaber.')
print('It appears that this is not a weapon, however, as the beam projects a hologram')
print('of a woman that looks eerily like Princess Leia, but she calls herself Princess Maia of Pleiades.')

time.sleep(2)

print('Maia speaks.  Help me,' + player + '-wan Kenobi!  What is the name of my son?')


ans9 = input(">>")
if ('Hermes' in ans9) or ('hermes' in ans9):
    print('Success!')
    print('Hermes is the son of Maia!')

time.sleep(2)

print('The room begins to vibrate.  A very large 20-sided die appears.')
ans18 = input(">>")

if (('roll' in ans18) or ('take' in ans18)) and ('die' in ans18):
    die = randint(0, 20)
    print('Success!')
    print('You rolled a ', die)

time.sleep(2)

print('A portal appears...beckoning...')

time.sleep(5)
print('Game has been saved.')




