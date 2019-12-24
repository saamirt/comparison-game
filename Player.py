class Player:
    def __init__(self, player_id, rating=1200):
        self.__id = str(player_id)
        self.__rating = rating
        self.__matches = []

    def __str__(self):
        return ", ".join(map(lambda x: str(x), [self.__id, self.__rating]))

    def get_rating(self):
        return self.__rating

    def set_rating(self, new_rating):
        self.__rating = new_rating

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def add_match(self, match):
        self.__matches.append(match)

    def get_match_by_index(self, match_num):
        if (match_num >= len(self.__matches)):
            raise IndexError('There is not match number of that value')
        return self.__matches[match_num]

    def get_match_by_id(self, match_id):
        for i in self.__matches:
            if i.get_id() == match_id:
                return i.get_id()
        raise KeyError('Match does not exist or player was not in that match')

    def __eq__(self, other):
        if not other: return False
        return self.__id == other.get_id()