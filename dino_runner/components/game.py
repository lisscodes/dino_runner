import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEAD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

FONT_STYLE = "freesansbold.ttf"
MENU_COLOR = pygame.Color(0, 0, 0)
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
        self.death_count = 0
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.record = 0

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
        self.update_score()

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
        self.draw_score()
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
        self.generate_text(f"Score:{self.score}", 965, 15, 20, MENU_COLOR)
        self.generate_text(f"Record:{self.record}", 965, 35, 20, RECORD_COLOR)

    def handle_events_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN: # não confuda: K_DOWN
                self.run()

    def generate_text(self, text, half_screen_width, half_screen_height, size, color):
        font = pygame.font.Font(FONT_STYLE, size)
        text = font.render(f"{text}", True, color)
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        print(self.death_count)
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.generate_text("Press any key to start", 550, 550 // 2, 45, MENU_COLOR)
            self.screen.blit(ICON, (half_screen_width - 20, half_screen_height - 140))
        else:
            self.generate_text("You Died",  half_screen_width, half_screen_height - 170, 70, MENU_COLOR)
            self.generate_text(f"Deaths: {self.death_count}", half_screen_width, half_screen_height, 40, MENU_COLOR)
            self.generate_text(f"Score: {self.score}",  half_screen_width, half_screen_height + 50, 45, MENU_COLOR)
            self.generate_text(f"Record: {self.record}", half_screen_width, half_screen_height + 100, 47, MENU_COLOR)
            self.generate_text("Press any key to restart", half_screen_width, half_screen_height + 170, 50, MENU_COLOR)
            self.screen.blit(DEAD, (half_screen_width - 40, half_screen_height - 120))

        pygame.display.update()
        self.handle_events_menu()
    
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.score = 0
        self.game_speed = 20