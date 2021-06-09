import os

import allure

from tests_demoqa.testbase.DemoQaTestBase import DemoQaTestBase


@allure.epic("Demo Qa tests")
class ElementsTests(DemoQaTestBase):
    UPLOADED_FILE_PATH = "C:\\fakepath\\sampleFile.jpeg"
    LOCAL_FILE_PATH = "sampleFile.jpeg"

    @allure.description("In this case, test dynamically changes on elements")
    @allure.story("Dynamically elements change")
    def test_dynamic_property(self):
        navigation_page = super().navigate_to_tools_qa_page()
        elements_page = navigation_page.navigate_to_elements_page()
        dynamic_properties_page = elements_page.navigate_to_dynamic_properties_page()

        self.assertTrue(dynamic_properties_page.will_enabled_button(), 'Button is not enabled')
        self.assertTrue(dynamic_properties_page.color_changed_button(), 'The color of the button text has not changed')
        self.assertTrue(dynamic_properties_page.visible_button(), 'The button is not visible')

    @allure.story("Testing upload")
    @allure.description("In this case, test dynamical change elements")
    def test_upload(self):
        navigation_page = super().navigate_to_tools_qa_page()
        elements_page = navigation_page.navigate_to_elements_page()
        upload_and_download_page = elements_page.navigate_to_upload_and_download_page()
        upload_and_download_page.upload_sample_file(os.path.abspath(self.LOCAL_FILE_PATH))

        self.assertEquals(self.UPLOADED_FILE_PATH, upload_and_download_page.get_file_path_text(),
                          'The file has not been uploaded')
