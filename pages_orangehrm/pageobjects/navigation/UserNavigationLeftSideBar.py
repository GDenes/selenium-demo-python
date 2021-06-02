from pages_orangehrm.enums.PageEnum import PageEnum
from pages_orangehrm.pageobjects.navigation.AbstractNavigationLeftSideBar import AbstractNavigationLeftSideBar


class UserNavigationLeftSideBar(AbstractNavigationLeftSideBar):

    def navigate_to_my_info_page(self):
        self.me

    def navigate_to(self, pageEnum: PageEnum):
        if pageEnum == PageEnum.MY_INFO_PAGE:
            return
        elif pageEnum == PageEnum.EXPENSE_CLAIMS_PAGE:
            return