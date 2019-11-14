'''
mainGameState.py
'''
from assets.pyAssets import *
from gameStates import States
import pygame as pg
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
        self.piece = Piece(self.shape_list[1], board_obj=self.board)
        self.update_piece_stats(self.piece.name)
        self.next_piece = Piece(vitals=random.choice(self.shape_list),
                                board_obj=self.board)
        self.piece.spawn_piece()
        self.game_over = False


    def cleanup(self):
        print('cleaning up Game state stuff')

    def startup(self):
        print('starting Game state stuff')
    '''TODO: STATISTIC SECTION'''
    def update_piece_stats(self, piece):
        self.piece_count[str(piece)] += 1

    def display_piece_stats(self, screen):
        piece_stats = ['O', 'I', 'S', 'Z', 'J', 'L', 'T']
        for i in range(len(piece_stats)):
            font = pg.font.SysFont(None, 40)
            text = font.render(str(piece_stats[i])
                               + str(self.piece_count[str(piece_stats[i])]),
                               True, WHITE)
            text_rect = text.get_rect(topleft = (225, 220 + i*50))
            screen.blit(text,text_rect)

    def create_stat_pieces(self):
        stat_pieces = []
        for i in range(len(self.shape_list)):
            P = Piece(vitals=self.shape_list[i], board_obj=self.board)
            stat_pieces.append(P)

        return stat_pieces

    def draw_piece_stats(self,screen):
        pg.draw.rect(screen, BLACK,
                    (115, 150,
                    200, 425))
        pieces = self.create_stat_pieces()
        for piece_num in range(len(pieces)):
            pieces[piece_num].draw_stat(screen, piece_num)
    '''^^^^STATS SECTION'''
    def display_lines(self, screen):
        font = pg.font.SysFont(None, 40)
        text = font.render('Lines: '+str(self.board.lines_cleared), True, BLACK)
        text_rect = text.get_rect(topleft = (0,0))
        screen.blit(text, text_rect)

    def display_score(self,screen):
        font = pg.font.SysFont(None, 40)
        text = font.render('Score: '+str(self.board.points), True, BLACK)
        text_rect = text.get_rect(topleft=(0,50))
        screen.blit(text, text_rect)

    def display_next_box(self, screen):
        font = pg.font.SysFont(None, NEXT_TEXT_SIZE)
        text = font.render('NEXT', True, BLACK)
        text_rect = text.get_rect(center=(NEXT_TEXT_X, NEXT_TEXT_Y))
        screen.blit(text, text_rect)
        self.next_piece.draw_next(screen)

    def display_hud(self, screen):
        self.display_lines(screen)
        self.display_score(screen)
        self.display_next_box(screen)
        self.display_piece_stats(screen)

    def game_over_check(self):
        if self.piece.valid_spawn == False:
            self.game_over = True

    def handle_game_over(self):
        print('Handling game over')
        self.next = 'gameover'
        self.done = True
        self.board.reset_board()
        self.piece = Piece(vitals=random.choice(self.shape_list),
                           board_obj=self.board)
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
            self.next_piece = Piece(vitals=random.choice(self.shape_list),
                                    board_obj=self.board)
            self.game_over_check()
            if self.game_over == True:
                self.handle_game_over()
            self.piece.landed = False
            self.piece.check_collision()
            self.board.print_board()


    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            self.piece.movement_controls(event)
            print('Game State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True

    def update(self, screen, dt):
        self.draw(screen)
        self.piece.check_collision()
        self.game_logic()


    def draw(self, screen):
        screen.fill((LAVENDER_MIST))
        self.board.draw_board(screen)
        self.piece.draw_piece(screen)
        self.draw_piece_stats(screen)
        self.display_hud(screen)
