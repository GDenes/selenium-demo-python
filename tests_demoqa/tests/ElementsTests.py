from tests_demoqa.testbase.DemoQaTestBase import DemoQaTestBase


class ElementsTests(DemoQaTestBase):

    def test_dynamic_property_test(self):
        navigation_page = super().navigate_to_tools_qa_page()
        elements_page = navigation_page.navigate_to_elements_page()
        dynamic_properties_page = elements_page.navigate_to_dynamic_properties_page()

        self.assertTrue(dynamic_properties_page.will_enabled_button())
        self.assertTrue(dynamic_properties_page.color_changed_button())
        self.assertTrue(dynamic_properties_page.visible_button())
