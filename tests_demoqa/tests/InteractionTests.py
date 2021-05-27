from selenium.webdriver import ActionChains

from tests_demoqa.testbase.DemoQaTestBase import DemoQaTestBase


class InteractionsTests(DemoQaTestBase):
    DROPPED_VALUE = "Dropped!";
    DROPPED_SQUARE_BACKGROUND_COLOR = "70, 130, 180";

    def test_droppable_test(self):
        navigation_page = super().navigate_to_tools_qa_page()
        interaction_page = navigation_page.navigate_to_interactions_page()
        droppable_page = interaction_page.get_droppable_page()

        action = ActionChains(self.driver)
        action.drag_and_drop(droppable_page.get_draggable_square_component(),
                             droppable_page.get_droppable_square_component()).perform()

        self.assertEqual(self.DROPPED_VALUE, droppable_page.get_droppable_square_component_text())
        self.assertTrue(droppable_page.get_droppable_square_component_background_color()
                        .find(self.DROPPED_SQUARE_BACKGROUND_COLOR) != -1)


