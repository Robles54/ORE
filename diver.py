import pygame

class Diver:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.shots = []

    def move_up(self):
        self.y -= 50

    def move_down(self):
        self.y += 50

    def move_left(self):
        self.x -= 50

    def move_right(self):
        self.x += 50

    def shoot(self):
        shot = Shot(self.x, self.y)
        self.shots.append(shot)

    def update_shots(self):
        for shot in self.shots:
            shot.move()
            if shot.y < 0:
                self.shots.remove(shot)

    def draw_shots(self, screen):
        for shot in self.shots:
            shot.draw(screen)

    def check_collision(self, other_object):
        distance = ((self.x - other_object.x) ** 2 + (self.y - other_object.y) ** 2) ** 0.5
        return distance < self.radius + other_object.radius

class Shot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.y -= 10

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 5)

        
