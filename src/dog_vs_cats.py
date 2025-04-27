import pygame
import random
import time

#Constants
GAME_WIDTH, GAME_HEIGHT = 1400, 900
DOG_STEP = 5.0
BALL_SPEED = 4.0
CAT_SPAWN_INTERVAL = 2
CAT_SPEED = 2.0

# Initialize Pygame
pygame.init()

# Load and play background music
pygame.mixer.init()
pygame.mixer.music.load("jazz.wav")
pygame.mixer.music.play(-1)  # Loop forever

# Load sound effects
defeat_sound = pygame.mixer.Sound("defeat.flac")

# Create game screen
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Dog VS Cats")
clock = pygame.time.Clock()

# Load images
grass_image = pygame.image.load("grass.png")
grass_image = pygame.transform.scale(grass_image, (GAME_WIDTH, GAME_HEIGHT))
   
dog_image = pygame.image.load("dog.png")
dog_image = pygame.transform.scale(dog_image, (200, 200))
   
ball_image = pygame.image.load("bone.png")
ball_image = pygame.transform.scale(ball_image, (80, 60))
   
cat_images = [
    pygame.transform.scale(pygame.image.load("cat.png"), (160, 160)),
    pygame.transform.scale(pygame.image.load("cat1.png"), (160, 160)),
    pygame.transform.scale(pygame.image.load("cat2.png"), (160, 160)),
    pygame.transform.scale(pygame.image.load("cat3.png"), (160, 130)),
    pygame.transform.scale(pygame.image.load("cat4.png"), (160, 160)),
    pygame.transform.scale(pygame.image.load("cat5.png"), (160, 160)),
    ]