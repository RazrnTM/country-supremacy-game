class Game:
    def __init__(self, players):
        self.players = players
        self.current_turn = 0
        self.game_state = 'waiting'
        self.turns_taken = 0

    def start_game(self):
        if len(self.players) < 2:
            raise ValueError('Not enough players to start the game.')
        self.game_state = 'active'
        print('Game has started!')

    def end_game(self):
        self.game_state = 'ended'
        print('Game has ended!')

    def next_turn(self):
        if self.game_state != 'active':
            raise Exception('The game is not currently active.')
        self.current_turn = (self.current_turn + 1) % len(self.players)
        self.turns_taken += 1
        print(f"It's {self.players[self.current_turn]}'s turn.")

    def get_game_info(self):
        return {
            'current_turn': self.players[self.current_turn],
            'turns_taken': self.turns_taken,
            'game_state': self.game_state
        }