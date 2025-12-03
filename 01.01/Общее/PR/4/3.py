from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def rest(self):
        pass

class Programmer(Worker):
    def work(self):
        return "Writing code"

    def rest(self):
        return "Taking a coffee break"

class Designer(Worker):
    def work(self):
        return "Creating design mockups"

    def rest(self):
        return "Sketching for fun"