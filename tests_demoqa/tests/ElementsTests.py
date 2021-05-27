import os

from tests_demoqa.testbase.DemoQaTestBase import DemoQaTestBase


class ElementsTests(DemoQaTestBase):
    UPLOADED_FILE_PATH = "C:\\fakepath\\sampleFile.jpeg"
    LOCAL_FILE_PATH = "sampleFile.jpeg"

    def test_dynamic_property_test(self):
        navigation_page = super().navigate_to_tools_qa_page()
        elements_page = navigation_page.navigate_to_elements_page()
        dynamic_properties_page = elements_page.navigate_to_dynamic_properties_page()

        self.assertTrue(dynamic_properties_page.will_enabled_button())
        self.assertTrue(dynamic_properties_page.color_changed_button())
        self.assertTrue(dynamic_properties_page.visible_button())

    def test_upload_test(self):
        navigation_page = super().navigate_to_tools_qa_page()
        elements_page = navigation_page.navigate_to_elements_page()
        upload_and_download_page = elements_page.navigate_to_upload_and_download_page()
        upload_and_download_page.upload_sample_file(os.path.abspath(self.LOCAL_FILE_PATH))

        self.assertEquals(self.UPLOADED_FILE_PATH, upload_and_download_page.get_file_path_text())
