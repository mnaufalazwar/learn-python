from abc import ABC, abstractmethod

class Button(ABC):

    @abstractmethod
    def click(self):
        pass


class PushButton(Button):

    def click(self):
        print("jalan woy")


tombol = PushButton()
tombol.click()