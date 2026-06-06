from playsound import playsound
import os
import random
names = ['creep', 'shapeofyou', 'smellsliketeenspirit', 'somewhereibelong']

print('''
    DJ TrashNoise Command Line Player
      Select an Option:
      1. Radiohead - Creep (Techno Remix)
      2. Shape Of You - Ed Sheeran (Techno Remix)
      3. Nirvana - Smells Like Teen Spirit (Techno Remix)
      4. Linkin Park - Somewhere I Belong (Techno Remix)
      5. Random Song
      ''')

choice = input()

if not choice.isdigit():
    print('Invalid Choice')
    exit()
elif int(choice) < 1:
    print('Invalid Choice')
    exit()
else:
    if int(choice) < 5:
        playsound(os.getcwd() + '/songs/' + names[int(choice)-1] + '.mp3')
    else:
        playsound(os.getcwd() + '/songs/' + names[random.randint(0,3)] + '.mp3')