import asyncio
import pygame
import sys

pygame.init()

pygame.display.set_caption('Terminal')
screen = pygame.display.set_mode((1222, 653))
clock = pygame.time.Clock()
background = pygame.image.load('assets/background.jpg')
test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')
terminal_font = pygame.font.SysFont('Consolas', 50)
text_surface = terminal_font.render('Hello, hi! I am that guy.', False, 'Gray')


def handle_events() -> None:
    for event in pygame.event.get():
        handle_quit_event(event)


def handle_quit_event(event: pygame.event.Event) -> None:
    if event.type == pygame.QUIT:
        handle_quit()


def handle_quit() -> None:
    pygame.quit()
    sys.exit()


def draw_surface():
    screen.blit(background, (0, 0))
    screen.blit(test_surface, pygame.mouse.get_pos())
    screen.blit(text_surface, (300, 500))


async def main():
    while True:
        handle_events()
        draw_surface()
        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
