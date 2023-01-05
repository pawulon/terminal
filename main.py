import pygame
import sys

pygame.init()

pygame.display.set_caption('Terminal')
screen = pygame.display.set_mode((640, 480))


def handle_quit_event(event):
    if event.type == pygame.QUIT:
        handle_quit()


def handle_quit():
    pygame.quit()
    sys.exit()


def main():
    while True:
        for event in pygame.event.get():
            handle_quit_event(event)
        pygame.display.update()


if __name__ == '__main__':
    main()
