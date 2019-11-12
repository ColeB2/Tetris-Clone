'''
tetrisObjects.py - main objects for tetris game
block, piece and board
'''

import pygame as pg
from pyVariables import *
from tetrisBoardStates import*

class Block:
    def __init__(self, x, y, state=0, color=BLUE):
        self.x = x
        self.y = y
        self.state = state
        self.color = color
        self.x_coord = self.get_x_coord()
        self.y_coord = self.get_y_coord()

    def __iter__(self):
        return self

    def __next__(self):
        pass



    def get_x_coord(self):
        '''returns X coordinate pixel position'''
        return int((self.x * SCALE) + X_OFFSET)

    def get_y_coord(self):
        '''returns Y coordinate pixel position'''
        return int((self.y * SCALE) + Y_OFFSET)

    def empty(self):
        return self.state == 0

    def draw_block(self, screen, color, is_board=False):
        if self.state == 1:
            pg.draw.rect(screen, color,
                        (self.get_x_coord(), self.get_y_coord(),
                        SCALE-1, SCALE-1))
        elif self.state == 0 and is_board == True:
            pg.draw.rect(screen, BLACK,
                        (self.get_x_coord(), self.get_y_coord(),
                        SCALE-1, SCALE-1))

    def draw_next_block(self, screen, color, piece_size):
        x_offset = NEXT_X_OFF
        y_offset = NEXT_Y_OFF
        if piece_size == 3:
            x_offset += 0.5*SCALE
            y_offset += 0.0*SCALE
        if self.state == 1:
            pg.draw.rect(screen, color,
                        (self.x*SCALE + x_offset, self.y*SCALE + y_offset,
                        SCALE-1, SCALE-1))


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
        for row in range(len(self.shape)):
            self.piece_map.append(list())
            for col in range(len(self.shape)):
                self.piece_map[row].append(Block(x=col, y=row,
                                               state=self.shape[row][col],
                                               color=self.color))

    def get_piece_type(self):
        return self.shape

    def piece_gravity(self):
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                block.y += 1
    def check_rotational_collision(self, rot_direction, board_obj):
        pass

    def check_lateral_collision(self, direction, board_obj):
        move_piece = True
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                if direction == 'left':
                    if block.state == 1:
                        if block.x == LEFT_BOUND:
                            move_piece = False
                        elif board_obj.open_space(x=block.x-1, y=block.y) and \
                            block.x > LEFT_BOUND and move_piece != False:
                            move_piece = True
                        else:
                            move_piece = False
                elif direction == 'right':
                    if block.state == 1:
                        if block.x == RIGHT_BOUND:
                            move_piece = False
                        elif board_obj.open_space(x=block.x+1, y=block.y) and \
                            block.x < RIGHT_BOUND and move_piece != False:
                            move_piece = True
                        else:
                            move_piece = False

        if move_piece == True:
            self.move_piece(direction)
        else:
            pass

    def move_piece(self, direction):
        if direction == 'left':
            for row in range(len(self.piece_map)):
                for block in self.piece_map[row]:
                    if block.state == 1:
                        block.x -= 1
        elif direction == 'right':
            for row in range(len(self.piece_map)):
                for block in self.piece_map[row]:
                    if block.state == 1:
                        block.x += 1

    def movement_controls(self, event, board_obj):
        if event.key == pg.K_d or event.key == pg.K_RIGHT:
            self.check_lateral_collision('right', board_obj)
        if event.key == pg.K_a or event.key == pg.K_LEFT:
            self.check_lateral_collision('left', board_obj)
        if event.key == pg.K_s or event.key == pg.K_DOWN:
            self.check_collision(board_obj)


    def lock_piece(self, board_obj):
        self.landed = True
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                if block.state == 1:
                    board_obj.board_state[block.y][block.x].state = 1
        board_obj.line_clear_check()

    def check_collision(self, board_obj):
        move_piece = True
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                if block.state == 1:
                    if block.y+1 > BOTTOM_BOUND:
                        move_piece = False
                    elif board_obj.open_space(x=block.x, y=block.y+1) and \
                        block.y < BOTTOM_BOUND and move_piece != False:
                        move_piece = True
                    else:
                        move_piece = False
        if move_piece == True:
            self.piece_gravity()
        else:
            self.lock_piece(board_obj)

    def draw_piece(self, screen):
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                block.draw_block(screen, block.color)

    def draw_next(self, screen):
        piece_size = len(self.piece_map[0])
        pg.draw.rect(screen, BLACK,
                    (NEXT_BOX_X, NEXT_BOX_Y,
                    NEXT_BOX_WIDTH, NEXT_BOX_HEIGHT))
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                block.draw_next_block(screen, block.color, piece_size)



class Board:
    def __init__(self, width=TETRIS_BOARD_WIDTH, height=TETRIS_BOARD_HEIGHT):
        self.is_board = True
        self.width = width
        self.height = height
        self.board_state = []
        self.create_blank_board()
        #self.load_board_state(BOARD_1)
        self.lines_cleared = 0

        self.print_board()


    def __str__(self):
        return self.board_state

    def print_board(self):
        for i in range(len(self.board_state)):
            for block in self.board_state[i]:
                print(block.x, block.y, block.state, end=' ')
            print()

    def create_blank_board(self):
        for row in range(self.height):
            self.board_state.append(list())
            for col in range(self.width):
                self.board_state[row].append(Block(x=col, y=row, state=0,
                                                   color=BLUE))

    def load_board_state(self, loaded_state=BOARD_1):
        '''Loads outside board state for challenges and testing purposes'''
        for row in range(self.height):
            self.board_state.append(list())
            for col in range(self.width):
                self.board_state[row].append(Block(x=col, y=row,
                                                   state=loaded_state[row][col],
                                                   color=BLUE))

    def draw_board(self, screen):
        for row in range(len(self.board_state)):
            for block in self.board_state[row]:
                block.draw_block(screen, RED, True)

    def line_clear_check(self):
        for row in range(len(self.board_state)):
            filled = True
            for block in self.board_state[row]:
                if block.state == 0:
                    filled = False
            if filled == True:
                self.handle_line_clear(row)

    def handle_line_clear(self, row):
        self.clear_line(row)
        self.move_rows_down(row)

    def clear_line(self, row_to_be_cleared):
        for block in self.board_state[row_to_be_cleared]:
            block.state = 0
        self.lines_cleared += 1

    def move_rows_down(self, row_cleared):
        for row in range(row_cleared, 0, -1):
            for block in range(len(self.board_state[row])):
                block_state = self.board_state[row-1][block].state
                self.board_state[row][block].state = block_state

    def open_space(self, x, y):
        print(x, y)
        return self.board_state[y][x].state == 0
