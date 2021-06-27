from pygame.gfxdraw import aacircle
from pygame.draw import line
from tictactoe import TicTacToeState
from players import MiniMaxPlayer
from board_window import BoardWindow

CELL_COLORS = [(255, 255, 255),  # Empty cell
               (180, 40, 30),    # Player 1
               (180, 180, 30)]   # Player -1
BOARD_COLOR = (20, 30, 10)
GRID_COLOR = (200, 200, 200)


class TicTacToeWindow(BoardWindow):

    def __init__(self, state=None, autoplayer=None):
        super().__init__(
            state=state or TicTacToeState(),
            autoplayer=autoplayer or MiniMaxPlayer(5),
            cols=3, rows=3,
            grid_size=70, cell_padding=9,
            padding_v=0, padding_h=0)

    def action_for_cell(self, pos):
        return pos.col + pos.row*self.cols

    def draw_background(self, screen):
        screen.fill(BOARD_COLOR)
        gs = self.grid_size
        line(screen, GRID_COLOR, (gs, 0), (gs, 3*gs))
        line(screen, GRID_COLOR, (2*gs, 0), (2*gs, 3*gs))
        line(screen, GRID_COLOR, (0, gs), (3*gs, gs))
        line(screen, GRID_COLOR, (0, 2*gs), (3*gs,  2*gs))

    def draw_cell(self, screen, player, rect):
        color = CELL_COLORS[player]
        if player == 1:
            line(screen, color,
                 (rect.left, rect.top),
                 (rect.left + rect.width, rect.top + rect.height),
                 width=3)
            line(screen, color,
                 (rect.left + rect.width, rect.top),
                 (rect.left, rect.top + rect.height),
                 width=3)
        elif player == -1:
            radius = int(rect.width/2)
            center = rect.left + radius, rect.top + radius
            # pygame.draw.circle(self.screen, color, center, radius, width=3)
            aacircle(screen, *center, radius, color)
            aacircle(screen, *center, radius-1, color)
            aacircle(screen, *center, radius-2, color)


if __name__ == '__main__':
    window = TicTacToeWindow()
    window.show()
    print('hello')
