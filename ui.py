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
    title_text = title_font.render('Cookie Clicker', True, (0, 0, 0))
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


def drawPort(screen):
    # Fill the background
    screen.fill(LIGHT_BLUE)

    # Draw the top bar
    pygame.draw.rect(screen, DARK_BLUE, (0, 0, WIDTH, 50))

    # Draw the main area
    pygame.draw.rect(screen, GREY, (50, 100, 700, 200))

    # Draw the bottom icons
    icon_positions = [(50, 500), (150, 500), (250, 500), (350, 500), (450, 500)]
    for pos in icon_positions:
        pygame.draw.circle(screen, BROWN, pos, 40)

    # You can add text by creating a font object and rendering it to create a surface, like this:
    # font = pygame.font.Font(None, 36)
    # text = font.render('Some Text', True, WHITE)
    # screen.blit(text, (text_position_x, text_position_y))
