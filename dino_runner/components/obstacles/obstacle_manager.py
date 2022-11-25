import pygame
import random

from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, JALA_TYPE, END_SOUND
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        obstacle_type = [
            Cactus(),
            Bird(),
        ]

        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0,1)])

        for obstacle in self.obstacles:
                obstacle.update(game.game_speed, self.obstacles)
                if game.player.dino_rect.colliderect(obstacle.rect):
                    if not game.player.has_power_up:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        END_SOUND.play(0)
                        break
                    elif game.player.type == HAMMER_TYPE:
                        self.obstacles.remove(obstacle)
                    elif game.player.type == SHIELD_TYPE:
                        game.playing = True
                    elif game.player.type == JALA_TYPE:
                        game.game_speed = 20

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)