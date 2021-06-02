from abc import abstractmethod

from pages_orangehrm.enums.PageEnum import PageEnum


class HeaderInterface:
    @abstractmethod
    def navigate_to(self, pageEnum: PageEnum): raise NotImplementedError
