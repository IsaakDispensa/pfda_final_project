import pygame
import random
import time

DOG_STEP = 5.5
BALL_SPEED = 4.0
CAT_SPAWN_INTERVAL = 2
CAT_SPEED = 2.0


pygame.init()

# Get fullscreen dimensions
infoObject = pygame.display.Info()
GAME_WIDTH, GAME_HEIGHT = infoObject.current_w, infoObject.current_h

# Create fullscreen game screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Dog VS Cats")
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("jazz.wav")
pygame.mixer.music.play(-1)


defeat_sound = pygame.mixer.Sound("defeat.flac")
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

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FLOOR_LEVEL = GAME_HEIGHT - 40

dog_x = GAME_WIDTH // 2
dog_y = FLOOR_LEVEL - dog_image.get_height()
dog_movement = 0

score = 0
score_font = pygame.font.SysFont("Courier", 30, bold=True)
game_over_font = pygame.font.SysFont("Courier", 60, bold=True)

balls = []
cats = []

def move_left():
    global dog_movement
    dog_movement = -1

def move_right():
    global dog_movement
    dog_movement = 1

def stop_dog():
    global dog_movement
    dog_movement = 0

def create_ball():
    ball_x = dog_x + 80
    ball_y = dog_y - 40
    balls.append([ball_x, ball_y])

def create_cat():
    cat_x = random.randint(0, GAME_WIDTH - 160)
    cat_image = random.choice(cat_images)
    cats.append({"x": cat_x, "y": 0, "image": cat_image})

def remove_sprite(sprite_list, index):
    del sprite_list[index]

cat_timer = 0
game_running = True

while game_running:
    screen.blit(grass_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_RIGHT:
                move_right()
            elif event.key == pygame.K_SPACE:
                create_ball()
            elif event.key == pygame.K_q:
                game_running = False
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                stop_dog()

    dog_x += DOG_STEP * dog_movement
    dog_x = max(0, min(dog_x, GAME_WIDTH - dog_image.get_width()))

    for ball in balls.copy():
        ball[1] -= BALL_SPEED
        if ball[1] < 0:
            balls.remove(ball)
        for i, cat in enumerate(cats.copy()):
            if int(ball[0]) in range(int(cat["x"]) - 100, int(cat["x"]) + 100) and int(ball[1]) in range(int(cat["y"]) - 100, int(cat["y"]) + 100):
                remove_sprite(balls, balls.index(ball))
                remove_sprite(cats, i)
                defeat_sound.play()
                score += 1
                break

    if time.time() - cat_timer > CAT_SPAWN_INTERVAL:
        create_cat()
        cat_timer = time.time()

    for cat in cats.copy():
        cat["y"] += CAT_SPEED
        if cat["y"] > FLOOR_LEVEL:
            game_running = False

    screen.blit(dog_image, (dog_x, dog_y))

    for ball in balls:
        screen.blit(ball_image, (ball[0], ball[1]))

    for cat in cats:
        screen.blit(cat["image"], (cat["x"], cat["y"]))

    padding = 50
    score_label = f"Score: {score}"

    for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, -2), (-2, 2), (2, 2)]:
        outline = score_font.render(score_label, True, WHITE)
        screen.blit(outline, (GAME_WIDTH - outline.get_width() - padding + dx, padding + dy))

    text_surface = score_font.render(score_label, True, BLACK)
    screen.blit(text_surface, (GAME_WIDTH - text_surface.get_width() - padding, padding))

    pygame.display.flip()
    clock.tick(60)

pygame.mixer.music.stop()

screen.fill((0, 0, 0))

game_over_label = "GAME OVER"
for dx, dy in [(-3, 0), (3, 0), (0, -3), (0, 3), (-3, -3), (3, -3), (-3, 3), (3, 3)]:
    outline = game_over_font.render(game_over_label, True, WHITE)
    text_rect = outline.get_rect(center=(GAME_WIDTH // 2 + dx, GAME_HEIGHT // 2 + dy))
    screen.blit(outline, text_rect)

text_surface = game_over_font.render(game_over_label, True, BLACK)
text_rect = text_surface.get_rect(center=(GAME_WIDTH // 2, GAME_HEIGHT // 2))
screen.blit(text_surface, text_rect)


score_label = f"Final Score: {score}"
for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, -2), (-2, 2), (2, 2)]:
    outline = score_font.render(score_label, True, WHITE)
    screen.blit(outline, (GAME_WIDTH // 2 - outline.get_width() // 2 + dx, GAME_HEIGHT // 2 + 80 + dy))

text_surface = score_font.render(score_label, True, BLACK)
screen.blit(text_surface, (GAME_WIDTH // 2 - text_surface.get_width() // 2, GAME_HEIGHT // 2 + 80))

pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()   