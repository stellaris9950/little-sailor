
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

screen = pygame.display.set_mode((720, 540))
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