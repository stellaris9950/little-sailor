import pygame
import json

import ui
from color import *




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



# Button positions and sizes
buttons = {
    "dock": pygame.Rect(50, 500, 80, 80),
    "market": pygame.Rect(150, 500, 80, 80),
    "ship": pygame.Rect(250, 500, 80, 80),
    "save_game": pygame.Rect(350, 500, 80, 80)
}


# Dock UI sail button
sail_button = pygame.Rect(350, 250, 100, 50)
# Market UI buttons
buy_button = pygame.Rect(300, 200, 100, 50)
sell_button = pygame.Rect(300, 300, 100, 50)


return_button = pygame.Rect(50, HEIGHT - 100, 100, 50)
upgrade_button = pygame.Rect(300, 250, 150, 50)
save_button = pygame.Rect(300, 250, 150, 50)

# Current page

# Player square for sailing
player_square = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)
player_speed = 5


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


# Function to draw the sailing canvas
def sailing_canvas(screen, player_square):
    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, GREY, player_square)  # Player square

# Function to check button clicks and call appropriate functions


def move_player_square(keys, player_square):
    if keys[pygame.K_w]:
        player_square.y -= player_speed
    if keys[pygame.K_s]:
        player_square.y += player_speed
    if keys[pygame.K_a]:
        player_square.x -= player_speed
    if keys[pygame.K_d]:
        player_square.x += player_speed

    # Keep the square within the screen bounds
    player_square.clamp_ip(screen.get_rect())


# Main game loop -------------------------------------------

game_state = 'front_page'  # Initial game state
start_button_rects = (None, None)
save_button_rect = pygame.Rect(WIDTH - 150, 10, 140, 40)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # when the game is at the start page --------------------------
            if game_state == 'front_page':
                start_button_rect, load_button_rect = start_button_rects
                if ui.buttonClickDetect(start_button_rect):
                    game_state = 'main_game'
                elif ui.buttonClickDetect(load_button_rect):
                    score = load_game()

            # when the game is at the port page --------------------------
            elif game_state == 'main_game':
                ui.check_button_click(event.pos)

                # if cookie_rect.collidepoint(event.pos):
                #     score += 1
                # elif save_button_rect.collidepoint(event.pos):
                #     save_game(score)


    # __________________________________________________________________

    if game_state == 'front_page':
        start_button_rects = ui.show_front_page(screen)
    elif game_state == 'main_game':
        ui.port_ui(screen)

        # port page conversion to sail page -------------------------------
        keys = pygame.key.get_pressed()
        # Draw the interface based on the current page
        if ui.port_page == 'dock':
            ui.dock_ui(screen)
        elif ui.port_page == 'market':
            ui.market_ui(screen)
        elif ui.port_page == 'ship':
            ui.ship_ui(screen)
        elif ui.port_page == 'save_game':
            ui.save_game_ui(screen)
        elif ui.port_page == 'sailing':
            keys = pygame.key.get_pressed()
            move_player_square(keys, player_square)
            sailing_canvas(screen, player_square)



    pygame.display.flip()

pygame.quit()




