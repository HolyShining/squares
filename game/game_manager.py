from game.player import Player


class GameManager:
    """Control all ops above game"""

    def _get_player_deck(self, player_id):
        """Separate main deck for each player"""
        return self.deck[player_id::self.number_of_players]

    def _evaluate_player_result(self, player):
        """Evaluating result of game for each player based on player deck and sequence"""
        player_move = 0

        for step, square in enumerate(player.deck):
            # Loop because we has a cards with 1 or 2 squares
            for element in square:
                # -1 means '​No element in​ ​front​ ​of​ ​piece​ ​so​ ​it​ ​goes​ ​to​ ​last square'
                player_move = self.sequence.find(element, player_move) + 1 \
                    if self.sequence.find(element, player_move) != -1 else -1
        else:
            won_step_id = step

        # If player won calculate win card id and return successful result
        if player_move == -1 or player_move == len(self.sequence):
            last_card = player.id + (won_step_id * self.number_of_players)
            return True, player, last_card
        return False,

    def __init__(self, number_of_players, sequence, deck):
        self.number_of_players = number_of_players
        self.sequence = sequence
        self.deck = deck.replace(' ', '').split(',')
        self.players = [Player(player_id + 1, self._get_player_deck(player_id))
                        for player_id in range(number_of_players)]

    def result(self):
        """Get all results with win and returns better"""
        results = list(filter(lambda result: result[0],
                              [self._evaluate_player_result(player) for player in self.players]))
        results.sort(key=lambda result: result[2])
        return f'Player {results[0][1].id} won after {results[0][2]} cards.' if results \
            else f'No player won after {len(self.deck)} cards.'
