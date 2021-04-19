from abc import ABC, abstractmethod

class Button(ABC):

    def __init__(self, link):
        self.link = link

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass


class PushButton(Button):

    def click(self):
        print(f"push button go to {self.link}")

    @Button.link.setter
    def link(self, link):
        self.__link = link

    @link.getter
    def link(self):
        return self.__link


tombol = PushButton("www.google.com")
tombol.click()