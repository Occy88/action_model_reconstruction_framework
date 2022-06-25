from abc import abstractmethod


class LearningModelInterface:
    def __init_subclass__(cls, **kwargs):
        pass

    @abstractmethod
    def train(self):
        ...
