# pyColor.py
# list of python colors you commonly use
from tetronimo import *

AQUA = (0,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
FUCHSIA = (255,0,255)
GRAY = (128,128,128)
GREEN = (0,128,0)
LIME = (0,255,0)
MAROON = (128,0,0)
NAVY_BLUE = (0,0,128)
OLIVE = (128,128,0)
PURPLE = (128,0,128)
RED = (255,0,0)
SILVER = (192,192,192)
TEAL = (0,128,128)
WHITE = (255,255,255)
WHITE2 = (230,230,250)
YELLOW = (255,255,0)


'''SCREEN SIZE'''
DIS_X = 900
DIS_Y = 650
DIS_SIZE = (DIS_X, DIS_Y)
'''PYGAME VARS'''
FPS = 5
'''TETRIS BOARD VARIABLES'''
SCALE = 25
TETRIS_BOARD_WIDTH = 10
TETRIS_BOARD_HEIGHT = 20
X_OFFSET = int( (DIS_X - (10*SCALE)) / 2) #325
Y_OFFSET = int( (DIS_Y - (20*SCALE)) / 2) #75
'''GRID BOUNDARIES from 0-9 and 0-19'''
BOTTOM_BOUND = TETRIS_BOARD_HEIGHT-1
LEFT_BOUND = 0
RIGHT_BOUND = TETRIS_BOARD_WIDTH-1
TOP_BOUND = 0
'''TETRIS VARS'''
TETRIS_PIECES = [
O_PIECE, I_PIECE,
S_PIECE, Z_PIECE,
J_PIECE, L_PIECE,
T_PIECE
]
'''TETRIS PIECE VARIBALES'''
PIECE_X_OFFSET = (SCALE*4)
PIECE_Y_OFFSET = (SCALE)
'''TETRIS UI BOARD VARIABLES'''
'''NEXT BOX'''
NEXT_BOX_WIDTH = 4 * SCALE
NEXT_BOX_HEIGHT =4 * SCALE
NEXT_BOX_X_PADDING = 10
NEXT_BOX_X = 575 + NEXT_BOX_X_PADDING
NEXT_BOX_Y = DIS_Y/2 - (NEXT_BOX_HEIGHT/2)
'''NEXT_BOX_TEXT'''
NEXT_TEXT_SIZE = 50
NEXT_TEXT_X = NEXT_BOX_X + (NEXT_BOX_WIDTH/2)
NEXT_TEXT_Y = NEXT_BOX_Y - (NEXT_TEXT_SIZE/4)
'''NEXT PIECE VARS'''
NEXT_X_OFF = NEXT_BOX_X
NEXT_Y_OFF = NEXT_BOX_Y