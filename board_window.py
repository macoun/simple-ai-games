from types import SimpleNamespace
import pygame


class BoardWindow:

    def __init__(self, state, autoplayer, cols, rows, grid_size, padding_v, padding_h, cell_padding):
        self.cols = cols
        self.rows = rows
        self.state = state
        self.initial_state = state
        self.autoplayer = autoplayer
        self.grid_size = grid_size
        self.padding_v = padding_v
        self.padding_h = padding_h
        self.cell_padding = cell_padding

    def move(self, action):
        state = self.state
        if action in state.actions():
            state = state.move(action)
            if not state.gameover() and self.autoplayer:
                action = self.autoplayer.next_action(state)
                state = state.move(action)
        self.state = state

    def reset(self):
        self.state = self.initial_state

    def show(self, autoplayer=None):
        pygame.init()

        screen = pygame.display.set_mode(
            size=(self.grid_size * self.cols + 2 * self.padding_h,
                  self.grid_size * self.rows + 2*self.padding_v))

        self.draw(screen)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.reset()
                    self.draw(screen)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cell = self._cell_from_mouse_pos()
                    if cell and not self.state.gameover():
                        action = self.action_for_cell(cell)
                        self.move(action)
                        self.draw(screen)

            pygame.display.update()

    def draw(self, screen):
        self.draw_background(screen)
        for i, value in enumerate(self.state.cells):
            r, c = divmod(i, self.cols)
            rect = SimpleNamespace(
                left=self.padding_h + c*self.grid_size + self.cell_padding,
                top=self.padding_v + r*self.grid_size + self.cell_padding,
                width=self.grid_size - 2*self.cell_padding,
                height=self.grid_size - 2*self.cell_padding)

            self.draw_cell(screen=screen, player=value, rect=rect)

    def action_for_cell(self, pos):
        ...

    def draw_background(self, screen):
        ...

    def draw_cell(self, screen, player, rect):
        ...

    def _cell_from_mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        col, row = x//self.grid_size, y//self.grid_size
        if 0 <= col < self.cols and 0 <= row < self.rows:
            return SimpleNamespace(col=col, row=row)
