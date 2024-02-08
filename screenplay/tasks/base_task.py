from abc import ABC, abstractmethod

from screenplay.actor import Actor


class BaseTask(ABC):
    @abstractmethod
    def perform(self, actor: Actor):
        pass
