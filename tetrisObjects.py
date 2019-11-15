'''
tetrisObjects.py - main objects for tetris game
block, piece and board
'''

import pygame as pg
from pyVariables import *
from tetrisBoardStates import*
import time

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


    def __str__(self):
        return 'X: %s Y: %s State: %s' % (self.x, self.y, self.state)


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
            '''TESTING BG COLOR == YELLOW ''' '''
        elif self.state == 0 and is_board == False:
            pg.draw.rect(screen, YELLOW,
                        (self.get_x_coord(), self.get_y_coord(),
                        SCALE-1, SCALE-1)) '''
        elif self.state == 0 and is_board == True:
            pg.draw.rect(screen, BLACK,
                        (self.get_x_coord(), self.get_y_coord(),
                        SCALE-1, SCALE-1))


class Piece:
    def __init__(self, vitals, board_obj):
        self.name = vitals[2]
        self.orientation = 0
        self.rotation_states = vitals[0]
        self.shape = vitals[0][self.orientation]
        self.color = vitals[1]
        self.piece_map = []
        self.landed = False
        self.x_offset = int()
        self.y_offset = int()
        self.set_spawn_offset()
        self.board = board_obj
        self.valid_spawn = True

    def create_piece(self):
        for row in range(len(self.shape)):
            self.piece_map.append(list())
            for col in range(len(self.shape)):
                self.piece_map[row].append(Block(x=col + self.x_offset,
                                                 y=row - self.y_offset,
                                               state=self.shape[row][col],
                                               color=self.color))

    def set_spawn_offset(self):
        self.x_offset = int(7 - len(self.shape[0]))
        for row in range(len(self.shape)):
            if 1 in self.shape[row]:
                self.y_offset = row
                break

    def check_spawn(self):
        valid_spawn = True
        for row in range(len(self.shape)):
            for col in range(len(self.shape)):
                if self.shape[row][col] == 1:
                    x_val = (col+3)
                    y_val = (row-self.y_offset)
                    if self.board.open_space(x=x_val, y=y_val):
                        valid_spawn = True
                    else:
                        valid_spawn = False
        return valid_spawn

    def spawn_piece(self):
        valid_spawn = self.check_spawn()
        if valid_spawn == True:
            self.create_piece()
        else:
            self.valid_spawn = False
            return False


    def get_piece_type(self):
        return self.shape

    def move_piece_down(self):
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                block.y += 1

    def check_rotational_collision(self, rot_direction):
        rotate_piece = True
        for row in range(len(self.piece_map)):
            for col in range(len(self.piece_map[row])):
                block = self.piece_map[row][col]
                N =self.rotation_states[self.next_rotation_state(rot_direction)]
                next_state = N[row][col]
                if next_state == 1:
                    if self.board.open_space(x=block.x, y=block.y) and \
                        block.x >= LEFT_BOUND and \
                        block.x <= RIGHT_BOUND and \
                        rotate_piece != False:
                        rotate_piece = True
                    else:
                        rotate_piece = False

        if rotate_piece:
            self.rotate_piece(rot_direction)

    def next_rotation_state(self, rot_direction):
        '''
        calculates what index in piece list the next rotation state will be at.
        Can either be called to check what the next state will be or to change,
        To change call: self.orientation = self.next_rotation_state(rot_dir)
        '''
        if rot_direction == 'right':
            if self.orientation < 3:
                return self.orientation + 1
            else:
                return 0
        elif rot_direction == 'left':
            if self.orientation == 0:
                return 3
            else:
                return self.orientation - 1
                self.orientatiion -= 1

    def rotate_piece(self, rot_direction):
        self.next_rotation_state(rot_direction)
        self.orientation = self.next_rotation_state(rot_direction)
        self.shape = self.rotation_states[self.orientation]

        for row in range(len(self.piece_map)):
            for col in range(len(self.piece_map[row])):
                self.piece_map[row][col].state = self.shape[row][col]

    def check_lateral_collision(self, direction):
        move_piece = True
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                if direction == 'left':
                    if block.state == 1:
                        if block.x == LEFT_BOUND:
                            move_piece = False
                        elif self.board.open_space(x=block.x-1, y=block.y) and \
                            block.x > LEFT_BOUND and move_piece != False:
                            move_piece = True
                        else:
                            move_piece = False
                elif direction == 'right':
                    if block.state == 1:
                        if block.x == RIGHT_BOUND:
                            move_piece = False
                        elif self.board.open_space(x=block.x+1, y=block.y) and \
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
                    block.x -= 1
        elif direction == 'right':
            for row in range(len(self.piece_map)):
                for block in self.piece_map[row]:
                    block.x += 1

    def movement_controls(self, event):
        if event.key == pg.K_d or event.key == pg.K_RIGHT:
            self.check_lateral_collision('right')
        if event.key == pg.K_a or event.key == pg.K_LEFT:
            self.check_lateral_collision('left')
        if event.key == pg.K_KP9:
            self.check_rotational_collision('right')
        if event.key == pg.K_KP7:
            self.check_rotational_collision('left')
        #if event.key == pg.K_s or event.key == pg.K_DOWN:
        #    self.check_collision()


    def lock_piece(self):
        self.landed = True
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                if block.state == 1:
                    self.board.board_state[block.y][block.x].state = 1
                    self.board.board_state[block.y][block.x].color = self.color
        self.board.line_clear_check()

    def check_collision(self):
        move_piece = True
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                if block.state == 1:
                    if block.y+1 > BOTTOM_BOUND:
                        move_piece = False
                    elif self.board.open_space(x=block.x, y=block.y+1) and \
                        block.y < BOTTOM_BOUND and move_piece != False:
                        move_piece = True
                    else:
                        move_piece = False
        if move_piece == True:
            self.move_piece_down()
        else:
            self.lock_piece()

    def draw_piece(self, screen):
        for row in range(len(self.piece_map)):
            for block in self.piece_map[row]:
                block.draw_block(screen, block.color)

    def draw_next(self, screen):
        '''Draw function, used to draw the piece in the next box'''
        x_offset = NEXT_X_OFF
        y_offset = NEXT_Y_OFF#NEXT_BOX_Y

        piece_size = len(self.shape[0])
        if piece_size == 3:
            x_offset += 0.5*SCALE
            y_offset += 0.0*SCALE
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col] == 1:
                    pg.draw.rect(screen, self.color,
                                (col*SCALE + x_offset,
                                row*SCALE + y_offset,
                                SCALE-1, SCALE-1))

    def draw_stat(self, screen, vertical_offset):
        '''Draw function, used to draw mini pieces used in statistics box'''
        x_offset = STAT_X_OFFSET
        y_offset = STAT_Y_OFFSET + vertical_offset * (2.5 * PSCALE)
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col] == 1:
                    if self.name == 'I':
                        pg.draw.rect(screen, self.color,
                                    (col*PSCALE + x_offset-5,
                                    row*PSCALE + y_offset-15,
                                    PSCALE-1, PSCALE-1))
                    elif self.name == 'O':
                        pg.draw.rect(screen, self.color,
                                    (col*PSCALE + x_offset,
                                    row*PSCALE + y_offset-5,
                                    PSCALE-1, PSCALE-1))
                    else:
                        pg.draw.rect(screen, self.color,
                                    (col*PSCALE + x_offset,
                                    row*PSCALE + y_offset,
                                    PSCALE-1, PSCALE-1))


class Board:
    def __init__(self, width=TETRIS_BOARD_WIDTH, height=TETRIS_BOARD_HEIGHT):
        self.is_board = True
        self.width = width
        self.height = height
        self.board_state = []
        #self.create_blank_board()
        self.load_board_state(TETRIS_CENTER)
        self.lines_cleared = 0
        self.points = 0

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

    def load_board_state(self, loaded_state):
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
                block.draw_block(screen, block.color, True)

    def reset_board(self):
        for row in range(len(self.board_state)):
            for block in self.board_state[row]:
                block.state = 0
        self.lines_cleared = 0

    def handle_line_score(self, lines):
        if lines == 1:
            self.points += 40
        elif lines == 2:
            self.points += 100
        elif lines == 3:
            self.points += 300
        elif lines == 4:
            self.points += 1200

    def line_clear_check(self):
        lines_to_clear = []
        for row in range(len(self.board_state)):
            filled = True
            for block in self.board_state[row]:
                if block.state == 0:
                    filled = False
            if filled == True:
                lines_to_clear.append(row)
        if lines_to_clear:
            self.handle_line_score(len(lines_to_clear))
            for row in lines_to_clear:
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
        try:
            return self.board_state[y][x].state == 0
        except IndexError:
            return False
