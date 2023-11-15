"""
    The goal of is to provide commands that will convert a file with two columns ( Name, Summary) into a JSON structure
"""
import json
import pandas as pd
import re
from dataclasses import dataclass, asdict


def read_lines_from_file(source_file):
    with open(source_file) as source_file:
        lines = source_file.readlines()

    return lines


def convert_line_to_name_and_summary_class(lines):
    #
    # Coding note : Thought about map and list comprehension, but after study they do not seem
    # to handle multiple statements easily without creating a functino which would
    command_name_and_summary_list = []
    for line in lines:
        #data = line.split("-")
        data = re.split(r'\(\d+[xslpma]*\)', line )
        print(data)
        summary = re.sub(r"-\s+", '', data[1]).replace("\n","")
        print("*** ", summary)
        command_name_and_summary_list.append(CommandNameAndSummaryElement(data[0], summary))

    return command_name_and_summary_list


def to_json(command_name_and_summary):
    dictionary = [asdict(instance) for instance in command_name_and_summary]
    return json.dumps(dictionary)


def to_html(json):
    return pd.read_json(json).to_html(index=False)


def workflow(fileName):
    lines_from_file = read_lines_from_file(fileName)
    command_and_summary_list = convert_line_to_name_and_summary_class(lines_from_file)
    return to_html(to_json(command_and_summary_list))


@dataclass
class CommandNameAndSummaryElement:
    """ A container for the command name and summary """
    name: str
    summary: str
