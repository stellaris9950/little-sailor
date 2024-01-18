import pygame
import json

import game_value
import ui
from color import *

# Initialize Pygame
pygame.init()


# Constants for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Window size
CANVAS_WIDTH, CANVAS_HEIGHT = 1600, 1200  # Canvas size
PLAYER_SPEED = game_value.player_level  # Movement speed

# Initialize Pygame


# Create the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Little Sailor")

# Load arrow images and store them in a dictionary
ship_images = {
    'left': pygame.image.load('Pictures/ship/left.png').convert_alpha(),
    'top_left': pygame.image.load('Pictures/ship/top_left.png').convert_alpha(),
    'top': pygame.image.load('Pictures/ship/top.png').convert_alpha(),
    'top_right': pygame.image.load('Pictures/ship/top_right.png').convert_alpha(),
    'right': pygame.image.load('Pictures/ship/right.png').convert_alpha(),
    'bottom_right': pygame.image.load('Pictures/ship/bottom_right.png').convert_alpha(),
    'bottom': pygame.image.load('Pictures/ship/bottom.png').convert_alpha(),
    'bottom_left': pygame.image.load('Pictures/ship/bottom_left.png').convert_alpha(),
}

def load_and_tile_background(filename, width, height):
    background = pygame.image.load(filename).convert()
    background_rect = background.get_rect()
    tiled_background = pygame.Surface((width, height))

    for y in range(0, height, background_rect.height):
        for x in range(0, width, background_rect.width):
            tiled_background.blit(background, (x, y))

    return tiled_background


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, images):
        super().__init__()
        self.images = images # Dictionary of images
        self.image = images['right'] # Default image
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.velocity = pygame.Vector2(0, 0)

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        self.rect.clamp_ip(pygame.Rect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT))

    def stop(self):
        self.velocity = pygame.Vector2(0, 0)
        self.image = self.images['right']  # Change to a neutral image if necessary

    def set_direction(self, direction):
        self.velocity = direction
        if direction.x < 0 and direction.y < 0:
            self.image = self.images['top_left']
        elif direction.x < 0 and direction.y > 0:
            self.image = self.images['bottom_left']
        elif direction.x > 0 and direction.y < 0:
            self.image = self.images['top_right']
        elif direction.x > 0 and direction.y > 0:
            self.image = self.images['bottom_right']
        elif direction.x < 0:
            self.image = self.images['left']
        elif direction.x > 0:
            self.image = self.images['right']
        elif direction.y < 0:
            self.image = self.images['top']
        elif direction.y > 0:
            self.image = self.images['bottom']

player = Player(ship_images)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

background = load_and_tile_background('Pictures/sea.jpg', CANVAS_WIDTH, CANVAS_HEIGHT)
offset = pygame.Vector2(0, 0)


def get_direction_to_mouse(player_rect, mouse_pos):
    """Calculate the direction from the player to the mouse click."""
    x_dir = 0
    y_dir = 0
    if mouse_pos[0] < player_rect.left:
        x_dir = -1
    elif mouse_pos[0] > player_rect.right:
        x_dir = 1
    if mouse_pos[1] < player_rect.top:
        y_dir = -1
    elif mouse_pos[1] > player_rect.bottom:
        y_dir = 1

    return pygame.Vector2(x_dir, y_dir)

port = pygame.image.load('Pictures/port.png').convert_alpha()
ports_index = ['topleft', 'topright', 'bottomleft', 'bottomright', 'middle']
ports_rect = {
    'topleft': port.get_rect(center=(200,100)),
    'topright': port.get_rect(center=(200,1000)),
    'bottomleft': port.get_rect(center=(1200, 100)),
    'bottomright': port.get_rect(center=(1200, 1000)),
    'middle': port.get_rect(center=(800, 600))
}

def drawPort(surface):
    global port, ports_rect
    surface.blit(port, ports_rect['topleft'])
    surface.blit(port, ports_rect['topright'])
    surface.blit(port, ports_rect['bottomleft'])
    surface.blit(port, ports_rect['bottomright'])
    surface.blit(port, ports_rect['middle'])


# Game variables
gold = 0
cabinet = False
font = pygame.font.Font(None, 36)

def renderGold(goldNum):
    font = pygame.font.Font(None, 24)
    gold_text = font.render(f'GOLD: {goldNum}', True, GOLD)
    gold_rect = gold_text.get_rect(center=(SCREEN_WIDTH-70, 10))
    screen.blit(gold_text, gold_rect)

# Main game loop -------------------------------------------

game_state = 'front_page'  # Initial game state
start_button_rects = (None, None)
save_button_rect = pygame.Rect(SCREEN_WIDTH - 150, 10, 140, 40)

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
                    game_state = 'port_page'
                elif ui.buttonClickDetect(load_button_rect):
                    game_value.loadGame()

            # when the game is at the port page --------------------------
            elif game_state == 'port_page':
                ui.check_button_click(event.pos)

            elif game_state == 'sail_page':
                mouse_pos = pygame.mouse.get_pos()
                adjusted_mouse_pos = (mouse_pos[0] + offset.x, mouse_pos[1] + offset.y)
                if player.rect.collidepoint(adjusted_mouse_pos):
                    player.stop()
                else:
                    direction_vector = get_direction_to_mouse(player.rect, adjusted_mouse_pos)
                    if direction_vector.length() > 0:
                        direction_vector = direction_vector.normalize()
                        # print(direction_vector)
                        player.set_direction(direction_vector * PLAYER_SPEED)
                break
    # __________________________________________________________________

    all_sprites.update()
    # Update the offset - keep the player in the center of the screen
    offset.x = player.rect.x - SCREEN_WIDTH // 2
    offset.y = player.rect.y - SCREEN_HEIGHT // 2

    if game_state == 'front_page':
        start_button_rects = ui.show_front_page(screen)
    elif game_state == 'port_page':
        ui.port_ui(screen)
        renderGold(game_value.gold)

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
            game_state = 'sail_page'

    elif game_state == 'sail_page':
        screen.fill(BLACK)
        screen.blit(background, -offset)  # Draw the background with the offset

        drawPort(background)
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect.topleft - offset)  # Draw sprites with the offset

        for index in ports_index:
            if ports_rect[index].collidepoint(player.rect.topleft):
                print('change')
                game_state = 'port_page'
                ui.port_ui(screen)
                break



    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()




