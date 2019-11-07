'''
tetrisObjects.py - main objects for tetris game
block, piece and board
'''

import pygame as pg
from pyVariables import *

class Block:
    def __init__(self, x, y, state=0, color=BLUE):
        self.x = x
        self.y = y
        self.state = state
        self.color = color

    def draw_block(self, screen, color, is_board=False):
        if self.state == 1:
            pg.draw.rect(screen, color,
                        (self.x, self.y, SCALE-1, SCALE-1))
        elif self.state == 0 and is_board == True:
            pg.draw.rect(screen, BLACK,
                        (self.x, self.y, SCALE-1, SCALE-1))

    #def draw_block(self, screen, color):
    #    pg.draw.rect(screen, color, (self.x, self.y, SCALE-1, SCALE-1))

    def __str__(self):
        return 'X: %s Y: %s State: %s' % (self.x, self.y, self.state)

class Piece:
    def __init__(self, shape):
        self.shape = shape
        self.color = RED
        self.piece_map = []
        self.create_piece()
        self.landed = False

    def create_piece(self):
        for i in range(len(self.shape)):
            self.piece_map.append(list())
            for j in range(len(self.shape)):
                self.piece_map[i].append(Block(x=i*SCALE + X_OFFSET + \
                                                     PIECE_X_OFFSET,
                                               y=j*SCALE + Y_OFFSET - \
                                                     PIECE_Y_OFFSET,
                                               state=self.shape[i][j],
                                               color=self.color))


    def piece_gravity(self):
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                block.y += 1*SCALE

    def piece_boundary(self, min_point, direction):
        '''
        min-point: 0 if going right, DIS_X if going left
        direction: 'left' or 'right'
        Returns farthest point shape contains in either left or right direction.
        Used to determine whether we can move the shape further in desired
        direction or whether part of the piece has hit a boundary wall
        '''
        farthest_point = min_point
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                if direction == 'left':
                    if block.x < farthest_point:
                        farthest_point = block.x
                elif direction == 'right':
                    if block.x > farthest_point:
                        farthest_point = block.x
        return farthest_point



    def move_piece(self, event):
        if event.key == pg.K_d or event.key == pg.K_RIGHT:
            if self.piece_boundary(0, 'right') == RIGHT_BOUND:
                pass
            else:
                for row in range(len(self.piece_map)):
                    for block in self.piece_map[row]:
                        block.x += 1*SCALE
        if event.key == pg.K_a or event.key == pg.K_LEFT:
            if self.piece_boundary(DIS_X, 'left')== LEFT_BOUND:
                pass
            else:
                for row in range(len(self.piece_map)):
                    for block in self.piece_map[row]:
                        block.x -= 1*SCALE

    def draw_piece(self, screen):
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                #print(row, block, block.x, block.y, block.state)
                block.draw_block(screen, block.color)

    def check_collision(self, board_obj):
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                if block.state == 1:
                    BLOCK_X = int((block.x - X_OFFSET)/SCALE)
                    BLOCK_Y = int((block.y - Y_OFFSET)/SCALE)
                    print(BLOCK_X, BLOCK_Y)
                    if BLOCK_Y+1 > 19:
                        self.handle_landing(board_obj, BLOCK_X, BLOCK_Y)
                    elif board_obj.board_state[BLOCK_Y+1][BLOCK_X].state == 0 and \
                        block.y < BOTTOM_BOUND-SCALE:
                        print('STATE: ', end=' ')
                        print(board_obj.board_state[BLOCK_Y][BLOCK_X].state)
                        self.piece_gravity()
                    else:
                        print('landed')
                        self.handle_landing(board_obj, BLOCK_X, BLOCK_Y)
                        print('STATE: ', end=' ')
                        print(board_obj.board_state[BLOCK_Y][BLOCK_X].state)

    def handle_landing(self, board_obj, x, y):
        self.landed = True
        print(y, x)
        board_obj.board_state[y][x].state = 1





class Board:
    def __init__(self, width=TETRIS_BOARD_WIDTH, height=TETRIS_BOARD_HEIGHT):
        self.is_board = True
        self.width = width
        self.height = height
        self.board_state = []
        self.create_blank_board()
        self.print_board()

    def __str__(self):
        return self.board_state

    def print_board(self):
        for i in range(len(self.board_state)):
            for block in self.board_state[i]:
                #print(block.state, end=' ')
                print(int((block.x - X_OFFSET)/SCALE),
                      int((block.y - Y_OFFSET)/SCALE),
                      block.state, end=' ')
            print()


    def create_blank_board(self):
        for row in range(self.height):
            self.board_state.append(list())
            for col in range(self.width):
                self.board_state[row].append(Block(x=col*SCALE + X_OFFSET,
                                                   y=row*SCALE + Y_OFFSET,
                                                   state=0,
                                                   color=BLUE))


    def draw_board(self, screen):
        for row in range(len(self.board_state)):
            for block in self.board_state[row]:
                block.draw_block(screen, RED, True)



    def lock_piece(self, piece_object):
        for row in range(len(piece_object.piece_map)):
            for block in piece_object.piece_map:
                self.board_state[piece_object.x][piece_object.y].state = 1
