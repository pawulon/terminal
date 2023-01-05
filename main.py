import pygame
import sys

pygame.init()

pygame.display.set_caption('Terminal')
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


def handle_events() -> None:
    for event in pygame.event.get():
        handle_quit_event(event)


def handle_quit_event(event: pygame.event.Event) -> None:
    if event.type == pygame.QUIT:
        handle_quit()


def handle_quit() -> None:
    pygame.quit()
    sys.exit()


def main():
    while True:
        handle_events()
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
