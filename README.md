# DOG VS CATS

## Repository
https://github.com/IsaakDispensa/pfda_final_project.git

## Description
Similar to out last lecture, I want to create a small pixelated "space invaders" game, except with a "dog VS cats" theme! I want the player to control a small dog icon (that's in a field) and throughout the game the player will shoot tennis balls at angry cats to eliminate them.

## Features
- A moveable dog icon (WASD): Use event listeners to detect key presses (W, A, S, D), and update the dog's x and y coordinates accordingly in your game loop. I'll also want to prevent the dog from moving off-screen by checking boundaries.

- Point Tracker for each cat you eliminate (IE: "Points: 12"): I'd create a points variable and increase it each time a tennis ball successfully hits a cat. I'm thinking of displaying the score in the top corner using a text draw function in my main render loop.

- Pressing "space" fires off a tennis ball: Detect when the spacebar is pressed and spawn a tennis ball object at the dog’s current location.

- Any fired balls can then hit a moving cat to eliminate it from the screen: Loop through all active tennis balls and all cats each frame, and check for collisions. If a ball hits a cat, remove both the ball and cat from their respective lists, and increase the score.

- If a cat touches the dog, your player is eliminated ("Game over! Final Score:__"): Check for collisions between the dog and any cats during the game loop. If there’s a collision, end the game and display a game-over message with the final score.

- I want there to be music/sound effects: I'd load audio files using my framework’s sound system (like pygame.mixer), then play background music on a loop and trigger sound effects during events like shooting or cat elimination.


- I want players to be able to restart the game: Add a "restart" state or button that resets all game variables (score, dog/cat/ball positions, etc.) to their starting values and brings the player back to the beginning of the game when triggered.

## Challenges
- I need to research how to add music/sounds to my game.
- I want my game to have a point system, so I need to resarch that mechanic.
- I am also aiming to have the player die/restart in my game, so that will require a few tutorials.

## Outcomes
Ideal Outcome:
-My ideal outcome will be a working "space invaders" style game with a dog VS cat theme. I there to be great visuals with a working "shoot" feature to eliminate cats (the dog will throw/shoot tennis balls at the cats). If I can, I want to add a point system, music, and sound effects. I would also like the cats to move about the screen and advance towards the player's dog.

Minimal Viable Outcome:
-At minimum, I would at least like a working game where cats pop up and the dog moves to shoots tennis balls to "eliminate" them. Sound effects/music/a point system isn't necessary but would be a plus.

## Milestones

- Week 1
  1. Find the dog/cat/tennis ball/backdrop images.
  2. Incorporate a mechanic to allow the dog to move with WASD.
  3. Incorporate a mechanic to have the dog fire off tennis balls when the player hits the "space" bar.
  4. Find WAV files for the sound effects/music, too.

- Week 2
  1. Create mechanic that allows cats to pop up randomly and advance towards the player's dog.
  2. If any of the cats touch the dog, then add function to make the game end. "Sorry! Game Over!"
  3. Incorporate a mechanic to where if any of the tennis balls hit a cat, then the cat vanishes off the screen.

- Week N (Final)
  1. Finally, add in the bonus point system where each time a player "eliminates" a cat, the player gains a point.
  2. Add in the music and sound effects. (EX: when the player fires off a tennis ball, the dog barks.)
  3. Clean up everything, record the video, and submit.

