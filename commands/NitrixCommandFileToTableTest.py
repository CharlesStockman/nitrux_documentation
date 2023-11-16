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
        self.assertTrue(command_name_and_summary_list[0].name, "aaa")
        self.assertTrue(command_name_and_summary_list[0].summary, "bbb")
        self.assertTrue(command_name_and_summary_list[1].name, "ccc")
        self.assertTrue(command_name_and_summary_list[1].summary, "dddd")

    def test_create_name_and_summary_json_document(self):
        command_name_and_summary_list = self.create_list()
        json = NitruxCommandFileToTable.to_json(command_name_and_summary_list)
        self.valid_json(json)

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
