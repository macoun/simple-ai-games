import click
from players import ConsolePlayer, MiniMaxPlayer, NNPlayer, RandomPlayer
from game import play, simulate
from tictactoe_model_cnn import TicTacToeModelCnn
from tictactoe_state import TicTacToeState


@click.command('connect4')
@click.option('--simulations', '-s',
              default=10000,
              help='How many plays to simulate for training.')
@click.option('--mode', '-m',
              default='window',
              type=click.Choice(['console', 'window']),
              help='Starts game in a terminal or a window.')
@click.option('--ai-player', '-p',
              default='nn',
              type=click.Choice(['nn', 'minimax']),
              help='Number of epochs to train.')
@click.option('--epochs', '-e',
              default=3,
              help='Number of epochs to train. (only for ai-player=nn)')
@click.option('--lookahead', '-l',
              default=3,
              help='Lookahead depth for the minimax algorithm.'
              ' (only for ai-player=minimax)')
def tictactoe(simulations, mode, ai_player, epochs, lookahead):
    state = TicTacToeState()

    if ai_player == 'nn':
        from tictactoe_model import TicTacToeModel
        model = TicTacToeModelCnn()
        plays = simulate(state, simulations, player1=RandomPlayer(), player2=MiniMaxPlayer(1))
        model.train(plays, epochs=epochs, batch_size = 100)
        autoplayer = NNPlayer(model)
    else:
        autoplayer = MiniMaxPlayer(lookahead=lookahead)

    if mode == 'console':
        states, _ = play(state, ConsolePlayer(), autoplayer)
        print(states[-1].state)
    else:
        from tictactoe_window import TicTacToeWindow
        TicTacToeWindow(autoplayer=autoplayer).show()


if __name__ == '__main__':
    tictactoe()
