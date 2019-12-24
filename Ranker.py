import abc

class Ranker(abc.ABC):
    @abc.abstractmethod
    def init(self):
        pass

    @abc.abstractmethod
    def add_player(self):
        pass

    @abc.abstractmethod
    def remove_player(self):
        pass

    @abc.abstractmethod
    def get_player(self):
        pass

    @abc.abstractmethod
    def add_match(self):
        pass

    @abc.abstractmethod
    def end_match(self):
        pass

