from Player import Player


class Match:
    def __init__(self, match_id, a, b):
        self.__id = match_id
        self.__a = a
        self.__b = b
        self.__ended = False
        self.update_pred()

    def is_ended(self):
        return self.__ended

    def get_player1(self):
        return self.__a

    def get_player2(self):
        return self.__b

    def update_player(self, player_id, player):
        if not isinstance(player, Player):
            raise ValueError('Not a valid player')
        if (player_id == self.__a.get_id()):
            self.__a = player
        elif (player_id == self.__b.get_id()):
            self.__b = player
        else:
            raise KeyError('Player not in match')

    def update_pred(self):
        self.__p_a = 1 / \
            (1+10**((self.__b.get_rating()-self.__a.get_rating())/400))
        assert self.__p_a >= 0
        assert self.__p_a <= 1
        self.__p_b = 1 - self.__p_a
        assert self.__p_b >= 0
        assert self.__p_b <= 1
        return (self.__p_a, self.__p_b)

    def end_match(self, score_a, score_b):
        if self.is_ended():
            return
        new_a = self.__a.get_rating() + 32*(score_a.value - self.__p_a)
        new_b = self.__b.get_rating() + 32*(score_b.value - self.__p_b)
        self.__ended = True
        return new_a, new_b

    def set_ended(self, ended):
        self.__ended = ended

    def __str__(self):
        return ", ".join(map(lambda x: str(x), [
            self.__id,
            self.__a.get_id(),
            self.__b.get_id()
        ]))
