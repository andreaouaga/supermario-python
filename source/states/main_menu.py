import pygame
from .. import setup
from .. import tools
from .. import constants as C
from ..components import info

class MainMenu:
    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor()
        self.info = info.Info('main_menu')

    def setup_background(self):
        self.background = setup.GRAPHICS['level_1']
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, 
        (int(self.background_rect.width * C.BG_MULTI), 
        int(self.background_rect.height * C.BG_MULTI)))

        self.viewpoint = setup.SCREEN.get_rect()
        self.caption = tools.get_image(
            setup.GRAPHICS['title_screen'], 
            1, 60, 176, 88, (255, 0 ,220), C.BG_MULTI)
        

    def setup_player(self):
        self.player_image = tools.get_image(
            setup.GRAPHICS['mario_bros'],
            178, 32, 12, 16, (0, 0, 0), C.BG_MULTI)

    def setup_cursor(self):
        self.cursor_image = tools.get_image(
            setup.GRAPHICS['title_screen'], 
            3, 155, 8, 8, (255, 0, 220), C.BG_MULTI)

    def update(self, surface):

        surface.blit(self.background, self.viewpoint)
        surface.blit(self.caption, (170, 100))
        surface.blit(self.cursor_image, (220, 360))
        surface.blit(self.player_image, (200, 495))

        self.info.update()
        self.info.draw(surface)