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
ORANGE = (255, 165, 1)
SILVER = (192,192,192)
TEAL = (0,128,128)
WHITE = (255,255,255)
LAVENDER_MIST = (230,230,250)
YELLOW = (255,255,0)
LIGHT_GOLDENROD_YELLOW = (250,250,230)



'''TETRIS COLORS'''
T_COLOR = (160, 1, 241)
J_COLOR = (1,0,241)
Z_COLOR = (240,0,1)
O_COLOR = (248,230,8)
S_COLOR = (2,241,2)
I_COLOR = (1,241,242)
L_COLOR = (239,130,1)


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
Y_PADDING = 30
Y_OFFSET = int( (DIS_Y - (20*SCALE)) / 2)  + Y_PADDING #75 + 30 = 105
'''TETRIS ROUNDED BACKGROUND'''
RTSCALE = 30
ROUNDED_TETRIS_BOARD_RECT = (X_OFFSET-RTSCALE, Y_OFFSET-RTSCALE,
                             (10*SCALE)+(2*RTSCALE),(20*SCALE)+(2*RTSCALE))
'''GRID BOUNDARIES from 0-9 and 0-19'''
BOTTOM_BOUND = TETRIS_BOARD_HEIGHT-1
LEFT_BOUND = 0
RIGHT_BOUND = TETRIS_BOARD_WIDTH-1
TOP_BOUND = 0
'''TETRIS VARS'''
TETRIS_PIECES = [
(O_PIECE, O_COLOR, 'O'),
(I_PIECE, I_COLOR, 'I'),
(S_PIECE, S_COLOR, 'S'),
(Z_PIECE, Z_COLOR, 'Z'),
(J_PIECE, J_COLOR, 'J'),
(L_PIECE, L_COLOR, 'L'),
(T_PIECE, T_COLOR, 'T')
]
SHAPE_LIST = [
'O','I',
'S','Z',
'J','L',
'T'
]
'''TETRIS PIECE VARIBALES'''
PIECE_X_OFFSET = (SCALE*4)
PIECE_Y_OFFSET = (SCALE)
'''TETRIS UI BOARD VARIABLES'''
'''NEXT BOX'''
NEXT_BOX_WIDTH = 4 * SCALE
NEXT_BOX_HEIGHT = 100+50#4 * SCALE
NEXT_BOX_X_PADDING = 5
NEXT_BOX_X = (X_OFFSET + (SCALE* TETRIS_BOARD_WIDTH)) + NEXT_BOX_X_PADDING
NEXT_BOX_Y = DIS_Y/2 - (NEXT_BOX_HEIGHT/2) + Y_PADDING
NEXT_BOX_RECT = (NEXT_BOX_X, NEXT_BOX_Y, NEXT_BOX_WIDTH, NEXT_BOX_HEIGHT)
'''NEXT_BOX_TEXT'''
NEXT_TEXT_SIZE = 50
NEXT_TEXT_X = NEXT_BOX_X + (NEXT_BOX_WIDTH/2)
NEXT_TEXT_Y = NEXT_BOX_Y + (NEXT_TEXT_SIZE/2)
'''NEXT PIECE VARS'''
NEXT_X_OFF = NEXT_BOX_X - 0*SCALE
NEXT_Y_OFF = NEXT_BOX_Y + 2*SCALE
'''GAMEOVER VARS'''
GAMEOVER_RECT = (DIS_Y/4,DIS_Y/4,DIS_X-300,DIS_Y-300)
'''STATISTICS BOX'''
STAT_BOX_WIDTH = 200
STAT_BOX_HEIGHT = 425
STAT_BOX_PADDING = 5
STAT_BOX_X = X_OFFSET - STAT_BOX_WIDTH - STAT_BOX_PADDING
STAT_BOX_Y = 180
STAT_BOX_Y = Y_OFFSET + (3*SCALE)
STAT_BOX_RECT = (STAT_BOX_X, STAT_BOX_Y, STAT_BOX_WIDTH, STAT_BOX_HEIGHT)
PSCALE = 20 #Scale - size for mini pieces used in statistics
'''STAT PIECES LOCATION X/Y COORDS'''
STAT_X_OFFSET = STAT_BOX_X + 45
STAT_Y_OFFSET = STAT_BOX_Y + 40
STAT_X_VALUES = STAT_X_OFFSET + 75
STAT_Y_VALUES = STAT_Y_OFFSET + 20
'''STATISTICS TITLE TEXT'''
STAT_TEXT_X = (STAT_BOX_X) + (STAT_BOX_WIDTH / 2)
STAT_TEXT_Y = STAT_BOX_Y + PSCALE
'''LINES BOX'''
LINE_BOX_WIDTH = 250
LINE_BOX_HEIGHT = 45
LINE_BOX_X = 325
LINE_BOX_Y = Y_OFFSET - LINE_BOX_HEIGHT - 5
LINE_BOX_RECT = (LINE_BOX_X, LINE_BOX_Y, LINE_BOX_WIDTH, LINE_BOX_HEIGHT)

LINE_TEXT_X = (LINE_BOX_X) + (LINE_BOX_WIDTH/2)
LINE_TEXT_Y = LINE_BOX_Y
LINE_TEXT_COORD = (LINE_TEXT_X, (LINE_TEXT_Y+(LINE_BOX_HEIGHT/2 + 2)) )
'''SCORE/HIGHSCORE BOX'''
SCORE_LINE_PADDING = 5
SCORE_BOX_X = LINE_BOX_X + (LINE_BOX_WIDTH) + SCORE_LINE_PADDING
SCORE_BOX_Y = LINE_BOX_Y
SCORE_BOX_WIDTH = 200
SCORE_BOX_HEIGHT = 200
SCORE_BOX_RECT = (SCORE_BOX_X, SCORE_BOX_Y, SCORE_BOX_WIDTH, SCORE_BOX_HEIGHT)
SCORE_TEXT_X = (SCORE_BOX_X) + 5
SCORE_TEXT_Y = SCORE_BOX_Y + SCORE_BOX_HEIGHT/2
SCORE_COORDS = (SCORE_TEXT_X, SCORE_TEXT_Y)
'''PYTHON/PYGAME LOGOS'''
PYTHON_RECT = (100, DIS_Y - 150)
PYGAME_RECT = (DIS_X-350, DIS_Y-170)
