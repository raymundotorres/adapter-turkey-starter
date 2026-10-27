from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def fly(self) -> list[str]:
        raise NotImplementedError
