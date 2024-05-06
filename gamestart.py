import pygame
import sys
import random
import time
from diver import Diver
from asteroid import Asteroid
from score import Score
from enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("ORE")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.diver = Diver(400, 300, 20)
        self.diver_image = pygame.image.load("image/player_walk_2.png").convert_alpha()
        self.asteroids = []
        self.last_asteroid_spawn_time = pygame.time.get_ticks()  # Time of last asteroid spawn
        self.score = Score()
        self.game_over = False
        self.paused = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.diver.move_up()
                elif event.key == pygame.K_DOWN:
                    self.diver.move_down()
                elif event.key == pygame.K_LEFT:
                    self.diver.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.diver.move_right()
                elif event.key == pygame.K_SPACE:
                    self.diver.shoot()
                elif event.key == pygame.K_p:
                    self.paused = not self.paused

    def update(self):
        if not self.paused:
            self.diver.update_shots()

            # Spawn asteroids every 5 seconds
            current_time = pygame.time.get_ticks()
            if current_time - self.last_asteroid_spawn_time > 5000:
                x = random.randint(0, 800)  # Random x-coordinate
                asteroid = Asteroid(x, 0)  # Spawn asteroid at the top of the screen
                self.asteroids.append(asteroid)
                self.last_asteroid_spawn_time = current_time  # Update last spawn time

        # Move and update asteroids
            for asteroid in self.asteroids:
                asteroid.move()

            # Check collision with shots
                for shot in self.diver.shots:
                    if asteroid.check_collision(shot):
                        self.asteroids.remove(asteroid)
                        self.diver.shots.remove(shot)
                        self.score.score_up() #Updates score when there is a collision
                        break  # Break out of the inner loop once collision is detected
                
                    if asteroid.check_collision(shot):
                        self.score.score_up()

                if not self.game_over:
                    for asteroid in self.asteroids:
                        if self.diver.check_collision(asteroid):
                            self.game_over = True
                            break
                else:
                    self.show_game_over_screen()
        else:
            self.show_game_paused_screen()

            #Checking if there's a collision with diver
            # if self.diver.check_collision(asteroid):
            #     self.is_running = False
            #     break

    def show_game_paused_screen (self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont("comicsans", 50, True, True)
        text = font.render("Paused", 1, (255, 255, 255))
        self.screen.blit(text, (300, 250))
        pygame.display.flip()

    def draw(self):
        self.screen.fill((0, 0, 255))
        self.diver.draw_shots(self.screen)
        self.score.show_score(self.screen)
        self.screen.blit(self.diver_image, (self.diver.x - self.diver_image.get_width() / 2, self.diver.y - self.diver_image.get_height() / 2))

        # Draw asteroids
        for asteroid in self.asteroids:
            asteroid.draw(self.screen)

        pygame.display.flip()

    def show_game_over_screen(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont("comicsans", 50, True, True)
        text = font.render("Game Over", 1, (255, 255, 255))
        self.screen.blit(text, (200, 250))
        pygame.display.flip()

    def start(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
import time

# # Add a 3-second pause
# time.sleep(3)

print('hi')

if __name__ == "__main__":
    game = Game()
    game.start()
    pygame.quit()
    sys.exit()