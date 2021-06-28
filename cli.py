import click
from players import ConsolePlayer, MiniMaxPlayer, NNPlayer
from game import play, simulate


def cli_play_tictactoe(sim_count):
    from tictactoe import TicTacToeState
    from tictactoe_model import TicTacToeModel
    from tictactoe_window import TicTacToeWindow

    model = TicTacToeModel()
    player = NNPlayer(model)
    model.train(simulate(TicTacToeState(), sim_count), epochs=3)
    # model.train(simulate(TicTacToeState(), sim_count, player, player))

    TicTacToeWindow(autoplayer=player).show()
    # states, _ = play(TicTacToeState(), player, ConsolePlayer())
    # print(states[-1].state)


def cli_play_connect4(sim_count):
    from connect4 import Connect4State
    from connect4_model import Connect4Model
    from connect4_window import Connect4Window

    model = Connect4Model()
    player = NNPlayer(model)
    model.train(simulate(Connect4State(), sim_count), epochs=3)
    # model.train(simulate(TicTacToeState(), sim_count, player, player))

    Connect4Window(autoplayer=player).show()
    # states, _ = play(TicTacToeState(), player, ConsolePlayer())
    # print(states[-1].state)


cli_play_connect4(100000)
