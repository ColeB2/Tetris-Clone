from gameStates import *
from mainGameState import Game


if __name__ == '__main__':
    settings = {
        'size': DIS_SIZE,
        'fps' : FPS
    }

    pg.init()
    app = Control(**settings)
    state_dict = {
        'menu': Menu(),
        'game': Game(),
        'gameover': Game_Over()
    }

    app.setup_states(state_dict, 'menu')
    app.main_game_loop()
    pg.quit()
    sys.exit()



'''
    def draw_stat(self, screen, vertical_offset):
        x_offset = 0
        y_offset = 200 + vertical_offset * (2 * SCALE)

        pg.draw.rect(screen, BLACK,
                    (115, 150,
                    200, 425))
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col] == 1:
                    pg.draw.rect(screen, self.color,
                                (col*SCALE + x_offset,
                                row*SCALE + y_offset,
                                SCALE-1, SCALE-1))
'''
