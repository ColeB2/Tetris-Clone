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

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Menu State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        screen.fill((255,0,0))

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
            self.event_loop()
            self.update(delta_time)
            pg.display.update()
