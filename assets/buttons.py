'''
buttons.py - Button class that has numerous variables to make creating
    buttons much easier.
'''
from pyVariables import *
import pygame
from pygame.locals import *

class Button:
    def __init__(self, x=0, y=0, width=50,
        height=50, font_size=25,
        color=RED, color2=BLUE,
        font='arialblack', text='Text',
        display=None, function=None):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.color = color
        self.color2 = color2
        self.font = font
        self.text = text
        self.display = display
        self.function = function

        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.clicked = False

    def text_length(self):
        if len(self.text) >= 12:
            self.font_size = self.height/4
        elif len(self.text) >=9:
            self.font_size = self.height/3
        elif len(self.text) >= 6:
            self.font_size = self.height/2 - (self.height*0.1)

    def handle_mouse_location(self):
        if (self.x + self.width > self.mouse[0] > self.x and
            self.y + self.height > self.mouse[1] > self.y):
            return True

    def handle_button_colors(self):
        if (self.x + self.width > self.mouse[0] > self.x and
            self.y + self.height > self.mouse[1] > self.y):
            pygame.draw.rect(self.display, self.color2,
                            (self.x, self.y, self.width, self.height))

            self.handle_button_click()

        else:
            pygame.draw.rect(self.display, self.color,
                            (self.x, self.y, self.width, self.height))


    def handle_button_click(self):
        if self.click[0] == 1 and self.function != None:
            if self.click[0] == 0:
                self.function()
        else:
            None


    def create_button(self):
        '''Displays the button with text, and multiple colours on the screen'''
        self.text_length()
        self.handle_button_colors()

        font = pygame.font.SysFont(self.font, int(self.font_size))
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (self.x + self.width/2,
                            self.y + self.height/2)
        self.display.blit(text, text_rect)
