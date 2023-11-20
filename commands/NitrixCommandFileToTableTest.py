"""
A collection of test that will allow to verify a text file with two columns ( name of binary and summary ) into a
JSON file that web page can easily read.
"""

import unittest
import NitruxCommandFileToTable
from bs4 import BeautifulSoup


class NitruxCommandFileToJSONTests(unittest.TestCase):


    def test_CommandNamesAndSummaryList(self):
        command_name_and_summary_list = NitruxCommandFileToTable.read_lines_from_file("data")
        self.assertTrue(self, len(command_name_and_summary_list) > 0)

    def test_lineToCommandNameAndSummaryClass(self):
        command_name_and_summary_list = self.create_list()
        self.assertTrue(len(command_name_and_summary_list) == 2)
        self.assertTrue(command_name_and_summary_list[0].Name, "aaa")
        self.assertTrue(command_name_and_summary_list[0].Summary, "bbb")
        self.assertTrue(command_name_and_summary_list[1].Name, "ccc")
        self.assertTrue(command_name_and_summary_list[1].Summary, "dddd")

    def test_create_data_frame(self):
        command_and_summary_list = self.create_list()
        json = NitruxCommandFileToTable.to_json(command_and_summary_list)
        dataFrame = NitruxCommandFileToTable.to_dataframe(json)

        self.assertTrue(dataFrame.shape, (2,2))
        self.assertEqual(dataFrame.columns.to_list(), ['Name', 'Summary'])
        self.assertIn(dataFrame.iat[0,0], 'aaa')
        self.assertTrue(dataFrame.iat[0,1] == 'bbb')
        self.assertTrue(dataFrame.iat[1,0] == 'ccc')
        self.assertTrue(dataFrame.iat[1,1] == 'dddd')

    def test_create_name_and_summary_html_document(self):
        command_name_and_summary_list = self.create_list()
        json = NitruxCommandFileToTable.to_json(command_name_and_summary_list)
        dataframe = NitruxCommandFileToTable.to_dataframe(json)
        html = dataframe.to_html()

        self.assertTrue(self.valid_html(html))

    def test_workflow(self):
        html = NitruxCommandFileToTable.workflow("data")
        self.assertTrue(self.valid_html(html))

        with open("commands.html", "w+") as file1:
            file1.write(html)

    def test_workflow_with_invalid_filename(self):
        with self.assertRaises(IOError):
            NitruxCommandFileToTable.workflow("cccc")

    def valid_json(self, json):
        try:
            json.loads(json)
        except:
            self.assertFalse(False, "Invalid Json " + json)

        print(json)

    @staticmethod
    def valid_html(html):
        return bool(BeautifulSoup(html, "html.parser").find())

    @staticmethod
    def create_list():
        line = {"aaa (1)- bbb", "ccc (2)- dddd"}
        command_name_and_summary_list = NitruxCommandFileToTable.convert_line_to_name_and_summary_class(line)
        return command_name_and_summary_list


if __name__ == "__main__":
    unittest.main()
