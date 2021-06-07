from tests_demoqa.testbase.DemoQaTestBase import DemoQaTestBase


class WidgetTests(DemoQaTestBase):
    BUTTON_TOOL_TIP_TEXT = "You hovered over the Button";
    TEXT_FIELD_TOOL_TIP_TEXT = "You hovered over the text field";

    def test_tool_tips(self):
        navigation_page = super().navigate_to_tools_qa_page()
        widgets_page = navigation_page.navigate_to_widget_page()
        tool_tips_page = widgets_page.navigate_to_tool_tips_page()

        self.assertEqual(self.BUTTON_TOOL_TIP_TEXT, tool_tips_page.hover_tool_tip_button_and_get_text(),
                         'The tooltip of button did not appear')
        self.assertEqual(self.TEXT_FIELD_TOOL_TIP_TEXT, tool_tips_page.hover_tool_tip_text_field_and_get_text(),
                         'The tooltip of input field did not appear')
