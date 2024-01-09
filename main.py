
# Import External Librarys
import pygame
import jsonProcess
# import ui




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
clock = pygame.time.Clock()
running = True
dt = 0

def show_front_page():
    screen.fill((255, 255, 255))  # White background
    title_font = pygame.font.Font(None, 72)
    button_font = pygame.font.Font(None, 36)

    # Draw the title
    title_text = title_font.render('Cookie Clicker', True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(title_text, title_rect)

    # Draw the 'Start Game' button
    button_text = button_font.render('Start Game', True, (0, 0, 0))
    button_rect = button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    pygame.draw.rect(screen, (200, 200, 200), button_rect.inflate(20, 20))  # Button background
    screen.blit(button_text, button_rect)

    return button_rect  # Return the rect to check for mouse click

def is_button_clicked(button_rect):
    return button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]


"""
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
cookie_img = pygame.image.load('cookie.png')
cookie_rect = cookie_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if cookie_rect.collidepoint(event.pos):
                score += 1

    # Fill the screen with a background color
    screen.fill((255, 255, 255))

    # Draw the cookie
    screen.blit(cookie_img, cookie_rect)

    # Display the score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()