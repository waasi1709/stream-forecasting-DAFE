# +
from abc import ABC, abstractmethod

class BaseStream(ABC):
    @abstractmethod
    def stream(self):
        pass

