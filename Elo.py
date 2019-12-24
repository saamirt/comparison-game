from MatchOutcomes import MatchOutcomes
from Player import Player
from Match import Match
from Ranker import Ranker

@Ranker.register
class Elo:
    @staticmethod
    def init():
        Elo.__players = {}
        Elo.__matches = {}
        Elo.__match_count = 0

    @staticmethod
    def add_player(player_id, rating=1000):
        if player_id in Elo.__players:
            raise KeyError('Player ID taken')
        Elo.__players[player_id] = Player(player_id, rating)
        return Elo.__players[player_id]
        
    @staticmethod
    def remove_player(player_id):
        if player_id not in Elo.__players:
            raise KeyError('Player does not exist')
        del Elo.__players[player_id]

    @staticmethod
    def get_player(player_id):
        if player_id not in Elo.__players:
            raise KeyError('Player does not exist')
        return Elo.__players[player_id]

    @staticmethod
    def disp_players():
        for i in Elo.__players:
            print(Elo.__players[i])

    @staticmethod
    def disp_matches():
        for i in Elo.__matches:
            print(Elo.__matches[i])

    @staticmethod
    def add_match(a, b):
        if a.get_id() not in Elo.__players:
            raise KeyError('Player 1 does not exist')
        if b.get_id() not in Elo.__players:
            raise KeyError('Player 2 does not exist')
        Elo.__match_count += 1
        Elo.__matches[Elo.__match_count] = Match(Elo.__match_count, a, b)
        return (Elo.__match_count)

    @staticmethod
    def get_matches():
        return Elo.__matches

    @staticmethod
    def end_match(match_id, score_a, score_b):
        if match_id not in Elo.__matches:
            raise KeyError('Match does not exist')
        if not isinstance(score_a, MatchOutcomes):
            raise ValueError(
                'First player score is not a valid score.')
        if not isinstance(score_b, MatchOutcomes):
            raise ValueError(
                'Second player score is not a valid score.')
        match = Elo.__matches[match_id]
        a = match.get_player1()
        b = match.get_player2()
        new_a, new_b = match.end_match(score_a, score_b)
        a.set_rating(int(new_a))
        b.set_rating(int(new_b))

    @staticmethod
    def get_match_count():
        return Elo.__match_count