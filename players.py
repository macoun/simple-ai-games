from random import randint


class Player:
    def next_action(self, state):
        moves = self.next_actions(state)
        return moves[randint(0, len(moves) - 1)]

    def next_actions(self, state):
        raise NotImplementedError()


class RandomPlayer(Player):
    def next_actions(self, state):
        return state.actions()


class ConsolePlayer(Player):

    def next_action(self, state):
        actions = state.actions()
        while True:
            try:
                print(state)
                action = input(f'Action [{actions}]: ')
                action = int(action)
                if action in actions:
                    return action
            except Exception:
                pass


class MiniMaxPlayer(Player):
    def __init__(self, lookahead):
        assert lookahead > 0
        self.lookahead = lookahead

    def next_actions(self, state):
        moves, _ = self.value(state, self.lookahead)
        return moves

    def value(self, state, lookahead):
        if lookahead == 0 or state.gameover():
            return [], 1.0*state.winner()*(lookahead+1)
        behaviour = max if state.player() == 1 else min
        return self.minimax(state, behaviour, lookahead)

    def minimax(self, state, behaviour, lookahead):
        moves, res = [], -10000*state.player()
        for cell in state.actions():
            _, v = self.value(state.move(cell), lookahead-1)
            if res == v:
                moves.append(cell)
            elif behaviour(res, v) == v:
                moves, res = [cell], v
        return moves, res


class NNPlayer(Player):
    def __init__(self, model):
        self.model = model

    def next_action(self, state):
        import numpy as np
        actions = state.actions()
        current_player = state.player()
        states = [state.move(action).cells for action in actions]
        probs = [p[current_player] for p in self.model.predict(states)]
        return actions[np.argmax(probs)]

    def next_actions(self, state):
        actions = state.actions()
        states = [state.move(action).cells for action in actions]
        winners = self.model.predict(states)
        current_player = state.player()
        winning_moves = [action
                         for action, winner in zip(actions, winners)
                         if winner == current_player]
        return winning_moves or actions
