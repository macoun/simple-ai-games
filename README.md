## Setup

Clone repository and change to the cloned source dir.

    git clone ...
    cd ...

Create and source a virtual env. (Example for macos/linux)

    python3 -m venv --prompt venv venv
    source venv/bin/activate

Install requirements.

    pip install -r requirements.txt

## Play Connect 4

The entry point is _connect4.py_.

    python -m connect4

This will start a gui game with a trained AI (neural network) player.

To play the game in your terminal, use the `--mode console` option.

    python -m connect4 --mode console


## Play Tic Tac Toe

The entry point is _tictactoe.py_.

    python -m tictactoe

This will start a gui game with a trained AI (neural network) player.

To play the gamein your terminal, use the `--mode console` option.

    python -m connect4 --mode console

