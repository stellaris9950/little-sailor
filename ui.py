import pygame
from color import *

WIDTH, HEIGHT = 800, 600

def buttonClickDetect(button_rect):
    return button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]


def show_front_page(screen):
    screen.fill((255, 255, 255))  # White background
    title_font = pygame.font.Font(None, 72)
    button_font = pygame.font.Font(None, 36)

    # Draw the title
    title_text = title_font.render('Little Sailor', True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(title_text, title_rect)

    # Draw the 'Start Game' button
    start_button_text = button_font.render('Start Game', True, (0, 0, 0))
    start_button_rect = start_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    pygame.draw.rect(screen, (200, 200, 200), start_button_rect.inflate(20, 20))
    screen.blit(start_button_text, start_button_rect)

    # Draw the 'Load Game' button
    load_button_text = button_font.render('Load Game', True, (0, 0, 0))
    load_button_rect = load_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    pygame.draw.rect(screen, (200, 200, 200), load_button_rect.inflate(20, 20))
    screen.blit(load_button_text, load_button_rect)

    return start_button_rect, load_button_rect


# Port page functions -----------------------------------------

port_page = None
buttons = {
    "dock": pygame.Rect(50, 500, 80, 80),
    "market": pygame.Rect(150, 500, 80, 80),
    "ship": pygame.Rect(250, 500, 80, 80),
    "save_game": pygame.Rect(350, 500, 80, 80)
}
def port_ui(screen):
    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, DARK_BLUE, (0, 0, WIDTH, 50))

    if not port_page:
        pygame.draw.rect(screen, GREY, (50, 100, 700, 200))
        for name, rect in buttons.items():
            pygame.draw.rect(screen, BROWN, rect)

# Return button position and size
return_button = pygame.Rect(50, HEIGHT - 100, 100, 50)
# Function to draw a return button

def draw_return_button(screen):
    pygame.draw.rect(screen, GREY, return_button)
    font = pygame.font.Font(None, 36)
    text_return = font.render('Return', True, WHITE)
    text_rect = text_return.get_rect(center=return_button.center)
    screen.blit(text_return, text_rect)


# Dock UI sail button
sail_button = pygame.Rect(350, 250, 100, 50)
# Function to draw the dock UI

def dock_ui(screen):
    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, RED, sail_button)  # Sail button

    font = pygame.font.Font(None, 36)
    text = font.render('Sail', True, WHITE)
    text_rect = text.get_rect(center=sail_button.center)
    screen.blit(text, text_rect)

    draw_return_button(screen)


# Market UI buttons
buy_button = pygame.Rect(300, 200, 100, 50)
sell_button = pygame.Rect(300, 300, 100, 50)
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

# Ship UI button
upgrade_button = pygame.Rect(300, 250, 150, 50)
# Function to handle drawing and interaction for the ship UI
def ship_ui(screen):
    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, GREY, upgrade_button)
    # Draw text on the button
    font = pygame.font.Font(None, 36)
    text_upgrade = font.render('Upgrade Ship', True, WHITE)
    screen.blit(text_upgrade, upgrade_button.topleft)

    draw_return_button(screen)

# Save game UI button
save_button = pygame.Rect(300, 250, 150, 50)
# Function to handle drawing and interaction for the save game UI
def save_game_ui(screen):
    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, GREY, save_button)
    # Draw text on the button
    font = pygame.font.Font(None, 36)
    text_save = font.render('Save Game', True, WHITE)
    screen.blit(text_save, save_button.topleft)

    draw_return_button(screen)


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