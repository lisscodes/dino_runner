import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEAD, DEFAULT_TYPE, RESET
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

RECORD_COLOR = pygame.Color(202, 197, 196)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.record = 0
        self.death_count = 0
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.cloud = Cloud()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.reset_game()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running= False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.cloud.update(self.game_speed)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5

        if self.score >= self.record:
            self.record = self.score

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #ffffff
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        draw_message_component(
            f"Score:{self.score}", 
            self.screen,
            pos_x_center=1000,
            pos_y_center=15)
        draw_message_component(
            f"Record:{self.record}", 
            self.screen,
            pos_x_center = 1000,
            pos_y_center = 35,
            font_color = RECORD_COLOR
        )

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", 
                    self.screen, 
                    pos_x_center=500,
                    pos_y_center=40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN: # não confunda: K_DOWN
                self.run()

    def show_menu(self):
        print(self.death_count)
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            draw_message_component(
                f"Press any key to start", 
                self.screen, 
                pos_x_center = 550, 
                pos_y_center = 550 // 2, 
                font_size = 45
            )
            self.screen.blit(ICON, (half_screen_width - 50, half_screen_height + 40))
        else:
            draw_message_component(
                f"You Died", 
                self.screen, 
                pos_y_center = half_screen_height - 170, 
                font_size = 70
            )
            draw_message_component(
                f"Deaths: {self.death_count}",
                self.screen,
                pos_y_center = half_screen_height,
                font_size = 40
            )          
            draw_message_component(
                f"Score: {self.score}",
                self.screen,
                pos_y_center = half_screen_height + 50,
                font_size = 45
            )
            draw_message_component(
                f"Record: {self.record}",
                self.screen,
                pos_y_center = half_screen_height + 100,
                font_size = 47
            )
            draw_message_component(
                f"Press any key to restart", 
                self.screen, 
                pos_y_center = half_screen_height + 170,
                font_size = 50
            )
            self.screen.blit(DEAD, (half_screen_width - 40, half_screen_height - 120))
            self.screen.blit(RESET, (half_screen_width - 35, half_screen_height + 210))

        pygame.display.update()
        self.handle_events_menu()
    
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.score = 0
        self.game_speed = 20