import pygame

class Paddle:
    def __init__(self, x, y, width, height, color, dy):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.dy = dy

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def update(self, height):
        self.y += self.dy

        if self.y < 0:
            self.y = 0
        elif self.y + self.height > height:
            self.y = height - self.height