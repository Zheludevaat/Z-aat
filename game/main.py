import pygame
import sys
from pathlib import Path

# Ensure project root is on sys.path for package imports
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from game.core.player import Player
from game.puzzles.sample_puzzle import sample_puzzle


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    player = Player()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        player.handle_input()
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
