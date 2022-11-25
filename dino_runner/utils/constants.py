import pygame
pygame.mixer.init()
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_JALA = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/dino_run_jala1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/dino_run_jala2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_JALA = pygame.image.load(os.path.join(IMG_DIR, "Dino/dino_jump_jala.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_JALA = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/dino_duck_jala1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/dino_duck_jala2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
JALA = pygame.image.load(os.path.join(IMG_DIR, 'Other/jala.png'))
DEAD = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDead.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
RESET = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png'))

SHIELD_SOUND= pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/SHIELD_POWER.wav'))
HAMMER_SOUND= pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/HAMMER_POWER.wav'))
JUMP_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/MARIO_JUMPING.wav'))
END_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/GAME_OVER.wav'))
BACKGROUND_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/BACKGROUND_GAME.wav'))
JALA_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/JALA_SOUND.ogg'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
JALA_TYPE = "jala"
