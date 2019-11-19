'''
mainGameState.py
'''
from assets.pyAssets import *
from gameStates import States
import pygame as pg
from pyShapes import *
from pyVariables import *
import random
from tetrisObjects import Block, Piece, Board

class Game(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'menu'
        self.board = Board()
        self.piece_count = {'O':0,'I':0, 'S':0,'Z':0,'J':0,'L':0, 'T':0}
        self.shape_list = TETRIS_PIECES
        self.piece = Piece(vitals=random.choice(self.shape_list),
                           board_obj=self.board)
        self.update_piece_stats(self.piece.name)
        self.next_piece = Piece(vitals=random.choice(self.shape_list),
                                board_obj=self.board)
        self.piece.spawn_piece()
        self.game_over = False
        self.high_score = 0

        self.move_left = False
        self.move_right = False
        self.move_down = False
        self.lateral_move_frequency = 150
        self.dt_last_lateral_move = pg.time.get_ticks()

        self.dt_last_down_move =pg.time.get_ticks()
        self.down_freq = 270
        self.down_move_frequency = self.down_freq


    def cleanup(self):
        print('cleaning up Game state stuff')

    def startup(self):
        print('starting Game state stuff')


    '''-----STATISTICS HUD-----'''
    def update_piece_stats(self, piece):
        self.piece_count[str(piece)] += 1

    def reset_piece_stats(self):
        for piece, value in self.piece_count.items():
            self.piece_count[piece] = 0

    def create_stat_pieces(self):
        stat_pieces = []
        for i in range(len(self.shape_list)):
            P = Piece(vitals=self.shape_list[i], board_obj=self.board)
            stat_pieces.append(P)

        return stat_pieces

    def display_stat_text(self, screen):
        font = pg.font.Font(PIXEL_FONT, 50)
        text = font.render('STATISTICS', True, WHITE)
        text_rect = text.get_rect(center=(STAT_TEXT_X, STAT_TEXT_Y))
        screen.blit(text, text_rect)

    def display_piece_values(self, screen):
        piece_stats = SHAPE_LIST
        for i in range(len(piece_stats)):
            font = pg.font.Font(PIXEL_FONT, 40)
            text = font.render(str(
                               self.piece_count[str(piece_stats[i])]).zfill(3),
                               True, WHITE)
            text_rect = text.get_rect(topleft=(STAT_X_VALUES,
                                      STAT_Y_VALUES + i*50))
            screen.blit(text,text_rect)

    def draw_piece_stats(self,screen):
        pg.draw.rect(screen, BLACK, (STAT_BOX_RECT))
        pieces = self.create_stat_pieces()
        for piece_num in range(len(pieces)):
            pieces[piece_num].draw_stat(screen, piece_num)

    '''-----SCORE BOARD-----'''
    def calculate_high_score(self):
        if self.board.points > self.high_score:
            self.high_score = self.board.points
        else:
            self.high_score = self.high_score

    def create_score_board(self, screen):
        pg.draw.rect(screen, BLACK, (SCORE_BOX_RECT))

    def display_score_text(self,screen):
        score_text = ('SCORE', str(self.board.points).zfill(6))
        x = SCORE_TEXT_X
        y = SCORE_TEXT_Y
        for i in range(len(score_text)):
            font = pg.font.Font(PIXEL_FONT, 60)
            text = font.render(score_text[i], True, WHITE)
            text_rect = text.get_rect(topleft=(x,y+i*40))
            screen.blit(text, text_rect)

    def display_high_score_text(self, screen):
        score_text = ('TOP', str(self.high_score).zfill(6))
        x = SCORE_TEXT_X
        y = SCORE_TEXT_Y - 90
        for i in range(len(score_text)):
            font = pg.font.Font(PIXEL_FONT, 60)
            text = font.render(score_text[i], True, WHITE)
            text_rect = text.get_rect(topleft=(x,y+i*40))
            screen.blit(text, text_rect)


    '''-----HEADS UP DISPLAY-----'''
    def display_lines(self, screen):
        pg.draw.rect(screen, BLACK, (LINE_BOX_RECT))
        font = pg.font.SysFont(None, 60)
        text = font.render('LINES - '+str(self.board.lines_cleared).zfill(3),
                          True, WHITE)
        text_rect = text.get_rect(center = (LINE_TEXT_COORD))
        screen.blit(text, text_rect)

    def display_statistics(self, screen):
        self.draw_piece_stats(screen)
        self.display_piece_values(screen)
        self.display_stat_text(screen)

    def display_score(self,screen):
        self.create_score_board(screen)
        self.display_score_text(screen)
        self.calculate_high_score()
        self.display_high_score_text(screen)



    def display_next_box(self, screen):
        pg.draw.rect(screen, BLACK, (NEXT_BOX_RECT))
        font = pg.font.SysFont(None, NEXT_TEXT_SIZE)
        text = font.render('NEXT', True, WHITE)
        text_rect = text.get_rect(center=(NEXT_TEXT_X, NEXT_TEXT_Y))
        screen.blit(text, text_rect)
        self.next_piece.draw_next(screen)

    def display_hud(self, screen):
        self.display_lines(screen)
        self.display_score(screen)
        self.display_next_box(screen)
        self.display_statistics(screen)

    def draw_tetris_board(self, screen):
        self.board.draw_board(screen)


        '''Game Logic and Game Over'''
    def game_over_check(self):
        if self.piece.valid_spawn == False:
            self.game_over = True

    def handle_game_over(self):
        self.next = 'gameover'
        self.done = True
        self.board.reset_board()
        self.piece = Piece(vitals=random.choice(self.shape_list),
                           board_obj=self.board)
        self.reset_piece_stats()
        self.update_piece_stats(self.piece.name)
        self.next_piece = Piece(vitals=random.choice(self.shape_list),
                                board_obj=self.board)
        self.piece.spawn_piece()
        self.game_over = False

    def game_logic(self):
        if self.piece.landed == True:
            self.piece = self.next_piece
            self.update_piece_stats(self.piece.name)
            self.piece.spawn_piece()
            self.down_move_frequency = self.down_freq
            self.next_piece = Piece(vitals=random.choice(self.shape_list),
                                    board_obj=self.board)
            self.game_over_check()
            if self.game_over == True:
                self.handle_game_over()
            self.piece.landed = False


    def piece_gravity(self):
        if pg.time.get_ticks() - self.dt_last_down_move > self.down_move_frequency:
            self.piece.handle_gravity()
            self.dt_last_down_move = pg.time.get_ticks()

    def set_gravity(self):
        self.down_freq = 0


        '''Controls'''
    def piece_movement(self, direction, rot=False):
        if rot == True:
            if direction == 'right':
                self.piece.handle_movement('right', rot)
            elif direction == 'left':
                self.piece.handle_movement('left', rot)
        elif rot == False:
            if direction == 'right':
                self.move_right = True
                self.move_left = False
                self.movement_handler()
            elif direction == 'left':
                self.move_left = True
                self.move_right = False
                self.movement_handler()
            elif direction == 'down':
                self.move_down = True
                self.movement_handler()


    def movement_handler(self):
        if  pg.time.get_ticks() - self.dt_last_lateral_move > self.lateral_move_frequency:
            if self.move_left:
                print(pg.time.get_ticks() - self.dt_last_lateral_move)
                self.piece.handle_movement('left')
                self.dt_last_lateral_move = pg.time.get_ticks()
            elif self.move_right:
                print(pg.time.get_ticks() - self.dt_last_lateral_move)
                self.piece.handle_movement('right')
                self.dt_last_lateral_move = pg.time.get_ticks()
        if self.move_down and self.piece.landed == False:
            self.down_move_frequency = 0
        else:
            self.down_move_frequency = self.down_freq

    def get_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_p:
            self.next = 'pause'
            self.done = True
        elif event.type == pg.KEYDOWN and event.key == (pg.K_d or pg.K_RIGHT):
            self.piece_movement('right')
        elif event.type == pg.KEYDOWN and event.key == (pg.K_a or pg.K_LEFT):
            self.piece_movement('left')
        elif event.type == pg.KEYDOWN and event.key == pg.K_KP7:
            self.piece_movement('left', rot=True)
        elif event.type == pg.KEYDOWN and event.key == pg.K_KP9:
            self.piece_movement('right', rot=True)
        elif event.type == pg.KEYDOWN and event.key == (pg.K_s or pg.K_DOWN):
            self.piece_movement('down')
        elif event.type == pg.KEYUP and event.key == (pg.K_a):
            self.move_left = False
        elif event.type == pg.KEYUP and event.key == (pg.K_d):
            self.move_right = False
        elif event.type == pg.KEYUP and event.key == (pg.K_s):
            self.move_down = False
    def move_logic(self):
        if self.move_left == True:
            pass

    def update(self, screen, dt):
        self.draw(screen)
        self.piece_gravity()
        self.movement_handler()
        self.game_logic()


    def draw(self, screen):
        screen.fill((LAVENDER_MIST))
        self.board.draw_board(screen)
        self.piece.draw_piece(screen)
        self.display_hud(screen)
