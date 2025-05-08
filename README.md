# DOG VS CATS

## Demo
Demo Video: https://youtu.be/p-shbLIOEls

## GitHub Repository
GitHub Repo: https://github.com/IsaakDispensa/pfda_final_project.git

## Description
Summary: 
-Dog VS Cats is a 2D arcade-style game created using Pygame. Players take control of a dog who fends off cats by launching bones at them. Cats fall from the top of the screen at regular intervals, and the player must move the dog left or right to aim and shoot accurately. Each cat defeated earns the player a point, but if even one cat reaches the ground, the game ends.


File Descriptions:
-The main script, project.py, contains the full logic for the game. It includes everything from initializing Pygame and managing the game loop to handling player inputs, spawning enemies, detecting collisions, and rendering visuals on the screen. Key functions such as create_ball, create_cat, and move_left help keep the game’s logic modular and organized for easier maintenance and expansion.
-Image assets such as dog.png, bone.png, and various cat.png files provide the characters and interactive elements of the game. The background, grass.png, sets the visual stage for gameplay, while multiple cat images are used to randomly vary the enemies' appearance. I used familiar cat meme icons to make the game more fun and relevant. The dog is also from “Undertale”, a 2d pixel game, because I wanted to add in a cute little reference. 
-Sound assets include a looping background music track (jazz.wav) that creates a playful, upbeat mood. A separate sound effect (defeat.flac) plays each time the player successfully defeats a cat.


Features:
-One of the standout features is the fullscreen mode, which allows the game to occupy the entire display. 
-The game also features randomized cat appearances using multiple cat images. Each time a cat is spawned, a different sprite is selected at random, which adds variety and keeps the visuals from feeling repetitive.
-The projectile system allows players to press the spacebar to fire bones upward from the dog’s position. 
-Score tracking utilizes the “Courier” font with a white outline for visibility against the background. The current score is always displayed during gameplay, and a final score is shown on a “game over” screen once the player loses.
-Finally, music and sound effects give the game a more dynamic and professional feel. The background track runs continuously during gameplay, and the cat defeat sound plays once a bone collides with their “hitbox”


Future Improvements:
-There are several areas where the game could be expanded or improved. One idea is to add power-ups, such as special bones that do more damage or shields that protect the dog from cats reaching the ground.
-Another improvement would be a menu system, including a start screen, a pause/resume function, and the ability to restart the game without relaunching it. Keeping track of a high score would also add a layer of replayability and competition.


Reference I Used For Help:
https://realpython.com/build-python-turtle-game-space-invaders-clone/