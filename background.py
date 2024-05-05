import pygame

class Background (pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/space.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    
    Background = Background("image/space.png", [0, 0])