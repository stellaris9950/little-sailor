
# # Import External Librarys
# import pygame
# import jsonProcess
# # import ui


"""

jsonProcess.add_ui("start_button", "StartUI", (0,0), (10, 10))


def mouseDetect(obstacle_list, circle_list):
    mouse_pos = pygame.mouse.get_pos()

    for obstacle in obstacles_list:
        if obstacle.rect.collidepoint(mouse_pos):
            return obstacle

    for circle in circle_list:
        if circle.pos.distance_to(mouse_pos) < circle.radius:
            return circle


ui_list = jsonProcess.read_ui()
def drawSpecificUI(containerWindowType):
    for ui in ui_list:
        if ui["containerWindowType"] == containerWindowType:

            pygame.draw.rect(screen, "white", [ui["position"], ui["size"]])


# pygame Run
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Little Sailor")
clock = pygame.time.Clock()
running = True
dt = 0



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    drawSpecificUI('StartUI')

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60


    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
"""

import pygame
import json

import ui

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Little Sailor")

# Load cookie image
cookie_img = pygame.image.load('cookie.png')
cookie_rect = cookie_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Game variables
score = 0
font = pygame.font.Font(None, 36)

# Save and load functions
def save_game(score):
    with open('savegame.json', 'w') as file:
        json.dump({'score': score}, file)

def load_game():
    try:
        with open('savegame.json', 'r') as file:
            data = json.load(file)
            return data['score']
    except FileNotFoundError:
        return 0

# Front page functions

# Main game loop
game_state = 'front_page'  # Initial game state
start_button_rects = (None, None)
save_button_rect = pygame.Rect(WIDTH - 150, 10, 140, 40)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == 'front_page':
                start_button_rect, load_button_rect = start_button_rects
                if ui.buttonClickDetect(start_button_rect):
                    game_state = 'main_game'
                elif ui.buttonClickDetect(load_button_rect):
                    score = load_game()

            elif game_state == 'main_game':
                if cookie_rect.collidepoint(event.pos):
                    score += 1
                elif save_button_rect.collidepoint(event.pos):
                    save_game(score)


    # __________________________________________________________________

    if game_state == 'front_page':
        start_button_rects = ui.show_front_page(screen)
    elif game_state == 'main_game':


        ui.drawPort(screen)



    pygame.display.flip()

pygame.quit()

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game Interface with Button UI')

# Define some colors
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 139)
BROWN = (165, 42, 42)
GOLD = (255, 215, 0)
GREY = (192, 192, 192)

# Button positions and sizes
buttons = {
    "port": pygame.Rect(50, 500, 80, 80),
    "market": pygame.Rect(150, 500, 80, 80),
    "ship": pygame.Rect(250, 500, 80, 80),
    "save_game": pygame.Rect(350, 500, 80, 80)
}

# Current page
current_page = None


def draw_interface(screen, page):
    # Fill the background
    screen.fill(LIGHT_BLUE)

    # Draw the top bar
    pygame.draw.rect(screen, DARK_BLUE, (0, 0, SCREEN_WIDTH, 50))

    # Draw the main area depending on the page
    if page:
        message = page.upper()
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        pygame.draw.rect(screen, GREY, (50, 100, 700, 200))
        screen.blit(text, text_rect)
    else:
        pygame.draw.rect(screen, GREY, (50, 100, 700, 200))

    # Draw the buttons
    for name, rect in buttons.items():
        pygame.draw.rect(screen, BROWN, rect)
        # Optionally add text to the buttons here


def check_button_click(pos):
    global current_page
    for name, rect in buttons.items():
        if rect.collidepoint(pos):
            current_page = name
            return


# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a button was clicked
            if event.button == 1:  # Left mouse button
                check_button_click(event.pos)

    # Draw the interface
    draw_interface(screen, current_page)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
