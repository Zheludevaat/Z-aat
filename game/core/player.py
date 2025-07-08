import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(300, 220, 16, 16)
        self.speed = 3

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
