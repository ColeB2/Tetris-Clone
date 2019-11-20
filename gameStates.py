'''
gameStates.py
'''
from assets.pyAssets import *
import os
import pygame as pg
from pyVariables import *
import sys

class States(object):
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

class Menu(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'game'

    def cleanup(self):
        print('cleaning up Menu state stuff')

    def startup(self):
        print('starting Menu state stuff')

    def python_logo(self, screen):
        python_logo = pg.image.load(PYTHON_LOGO)
        pygame_logo = pg.image.load(PYGAME_LOGO)
        python_logo_rect = python_logo.get_rect(topleft=(PYTHON_RECT))
        pygame_logo_rect = pygame_logo.get_rect(topleft=(PYGAME_RECT))
        screen.blit(python_logo, (python_logo_rect))
        screen.blit(pygame_logo, (pygame_logo_rect))

    def credit(self,screen):
        font = pg.font.Font(PIXEL_TITLE_FONT, 13)
        text = font.render(
        '''Created by Cole B\
        Originally created by Alexey Pajitnov\
        Fonts by KenneyNL Website: kenney.nl ''', True, BLACK)
        text_rect = text.get_rect(bottomleft=(0, DIS_Y))
        screen.blit(text, text_rect)

    def title_text(self, screen):
        font = pg.font.Font(BLOCK_FONT, 80)
        text = font.render('TETRIS CLONED', True, BLACK)
        text_rect = text.get_rect(midtop=(DIS_X/2, 0-SCALE))
        screen.blit(text, text_rect)

    def instruction_text(self, screen):
        font = pg.font.Font(PIXEL_FONT, 60)
        text = font.render('Press Space Bar to Play!', True, BLACK)
        text_rect = text.get_rect(center=(DIS_X/2, DIS_Y/2 + 50 ))
        screen.blit(text, (text_rect))

    def controls_text(self, screen):
        font = pg.font.Font(PIXEL_FONT, 50)
        ctrl_text = ['a - left', 'd - right', 's - down',
                     'numpad7 - rotate reft', 'numpad9 - rotate right' ,
                     'p - pause']
        for i in range(len(ctrl_text)):
            text = font.render(ctrl_text[i], True, BLACK)
            text_rect = text.get_rect(center=(DIS_X/2, DIS_Y/4 + i*30))
            screen.blit(text, (text_rect))

    def display_text(self, screen):
        self.title_text(screen)
        self.instruction_text(screen)
        self.controls_text(screen)
        self.credit(screen)

    def get_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            self.done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            pass

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        screen.fill(LAVENDER_MIST)
        self.display_text(screen)
        self.python_logo(screen)

class Game_Over(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'game'

    def cleanup(self):
        print('cleaning up Menu state stuff')

    def startup(self):
        print('starting Menu state stuff')

    def get_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_h:
            self.next = 'menu'
            self.done = True
        elif event.type == pg.KEYDOWN and event.key != pg.K_m:
            self.next = 'game'
            self.done = True

    def title_text(self, screen):
        pg.draw.rect(screen, LAVENDER_MIST, (GAMEOVER_RECT))
        font = pg.font.Font(PIXEL_FONT, 100)
        text = font.render('GAME OVER', True, BLACK)
        text_rect = text.get_rect(center=(DIS_X/2, DIS_Y/3))
        screen.blit(text, (text_rect))

    def instruction_text(self, screen):
        font = pg.font.Font(PIXEL_FONT, 60)
        text = font.render('Press any key to Restart', True, BLACK)
        text_rect = text.get_rect(center=(DIS_X/2, DIS_Y/2))
        screen.blit(text, text_rect)

    def home_text(self, screen):
        font = pg.font.Font(PIXEL_FONT, 60)
        text = font.render('Press h to return Home', True, BLACK)
        text_rect = text.get_rect(center = (DIS_X/2, DIS_Y/2 + 100))
        screen.blit(text, text_rect)



    def display_text(self, screen):
        self.title_text(screen)
        self.instruction_text(screen)
        self.home_text(screen)


    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        self.display_text(screen)

class Pause(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'game'


    def cleanup(self):
        print('cleaning up Pause state stuff')

    def startup(self):
        print('starting Pause state stuff')


    def get_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_p:
            self.next = 'game'
            self.done = True
        elif event.type == pg.KEYDOWN:
            pass

    def title_text(self, screen):
        font = pg.font.Font(PIXEL_FONT, 100)
        text = font.render('Paused', True, BLACK)
        text_rect = text.get_rect(center=(DIS_X/2, DIS_Y/3))
        screen.blit(text, (text_rect))

    def instruction_text(self, screen):
        font = pg.font.Font(PIXEL_FONT, 30)
        text = font.render('Press p to Unpause!', True, BLACK)
        text_rect = text.get_rect(center=(DIS_X/2, DIS_Y/3+100))
        screen.blit(text, (text_rect))

    def display_text(self, screen):
        self.title_text(screen)
        self.instruction_text(screen)


    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        screen.fill(LAVENDER_MIST)
        self.display_text(screen)

class Control:
    def __init__(self, **settings):
        self.__dict__.update(settings)
        self.done = False
        self.screen = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        self.state.done = False
        previous,self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous

    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, dt)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)

    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick(self.fps)/1000.0
            starting_level = 0
            self.event_loop()
            self.update(delta_time)
            pg.display.update()
