from model import Model


class TicTacToeModel(Model):
    def __init__(self, model=None):
        super().__init__(ninput=9,
                         layers=[64, 128, 128, 128, 128],
                         model=model)
