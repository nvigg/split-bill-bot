from abc import ABC, abstractmethod
from typing import TypeVar

C = TypeVar("C")
R = TypeVar("R")


class UseCaseAbstract[C, R](ABC):
    @abstractmethod
    async def __call__(self, command: C) -> R:
        pass
