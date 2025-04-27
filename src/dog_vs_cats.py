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