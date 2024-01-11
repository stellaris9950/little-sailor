
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

# Return button position and size
return_button = pygame.Rect(50, HEIGHT - 100, 100, 50)

# Dock UI sail button
sail_button = pygame.Rect(350, 250, 100, 50)
# Market UI buttons
buy_button = pygame.Rect(300, 200, 100, 50)
sell_button = pygame.Rect(300, 300, 100, 50)

# Ship UI button
upgrade_button = pygame.Rect(300, 250, 150, 50)

# Save game UI button
save_button = pygame.Rect(300, 250, 150, 50)


# Current page
port_page = None

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

# Port page functions -----------------------------------------

def port_ui(screen):
    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, DARK_BLUE, (0, 0, WIDTH, 50))

    if not port_page:
        pygame.draw.rect(screen, GREY, (50, 100, 700, 200))
        for name, rect in buttons.items():
            pygame.draw.rect(screen, BROWN, rect)

# Function to draw a return button
def draw_return_button(screen):
    pygame.draw.rect(screen, GREY, return_button)
    font = pygame.font.Font(None, 36)
    text_return = font.render('Return', True, WHITE)
    text_rect = text_return.get_rect(center=return_button.center)
    screen.blit(text_return, text_rect)
# Function to draw the dock UI
def dock_ui(screen):
    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, RED, sail_button)  # Sail button

    font = pygame.font.Font(None, 36)
    text = font.render('Sail', True, WHITE)
    text_rect = text.get_rect(center=sail_button.center)
    screen.blit(text, text_rect)

    draw_return_button(screen)

# Function to handle drawing and interaction for the market UI
def market_ui(screen):
    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, GREY, buy_button)
    pygame.draw.rect(screen, GREY, sell_button)
    # Draw text on the buttons
    font = pygame.font.Font(None, 36)
    text_buy = font.render('Buy', True, WHITE)
    text_sell = font.render('Sell', True, WHITE)
    screen.blit(text_buy, buy_button.topleft)
    screen.blit(text_sell, sell_button.topleft)

    draw_return_button(screen)

# Function to handle drawing and interaction for the ship UI
def ship_ui(screen):
    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, GREY, upgrade_button)
    # Draw text on the button
    font = pygame.font.Font(None, 36)
    text_upgrade = font.render('Upgrade Ship', True, WHITE)
    screen.blit(text_upgrade, upgrade_button.topleft)

    draw_return_button(screen)

# Function to handle drawing and interaction for the save game UI
def save_game_ui(screen):
    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, GREY, save_button)
    # Draw text on the button
    font = pygame.font.Font(None, 36)
    text_save = font.render('Save Game', True, WHITE)
    screen.blit(text_save, save_button.topleft)

    draw_return_button(screen)
# Function to draw the sailing canvas
def sailing_canvas(screen, player_square):
    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, GREY, player_square)  # Player square

# Function to check button clicks and call appropriate functions
def check_button_click(pos):
    global port_page
    if return_button.collidepoint(pos):
        port_page = None
    elif port_page == 'dock':
        if sail_button.collidepoint(pos):
            port_page = 'sailing'
    elif port_page == 'market':
        if buy_button.collidepoint(pos):
            print('Buy')
        elif sell_button.collidepoint(pos):
            print('Sell')
    elif port_page == 'ship':
        if upgrade_button.collidepoint(pos):
            print('Upgraded your ship')
    elif port_page == 'save_game':
        if save_button.collidepoint(pos):
            print('Saved game')
    else:
        for name, rect in buttons.items():
            if rect.collidepoint(pos):
                port_page = name

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
                check_button_click(event.pos)

                # if cookie_rect.collidepoint(event.pos):
                #     score += 1
                # elif save_button_rect.collidepoint(event.pos):
                #     save_game(score)


    # __________________________________________________________________

    if game_state == 'front_page':
        start_button_rects = ui.show_front_page(screen)
    elif game_state == 'main_game':
        port_ui(screen)

        # port page conversion to sail page -------------------------------
        keys = pygame.key.get_pressed()
        # Draw the interface based on the current page
        if port_page == 'dock':
            dock_ui(screen)
        elif port_page == 'market':
            market_ui(screen)
        elif port_page == 'ship':
            ship_ui(screen)
        elif port_page == 'save_game':
            save_game_ui(screen)
        elif port_page == 'sailing':
            keys = pygame.key.get_pressed()
            move_player_square(keys, player_square)
            sailing_canvas(screen, player_square)



    pygame.display.flip()

pygame.quit()




