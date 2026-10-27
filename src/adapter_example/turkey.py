from abc import ABC, abstractmethod


class Turkey(ABC):
    @abstractmethod
    def gobble(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def fly(self) -> str:
        raise NotImplementedError
