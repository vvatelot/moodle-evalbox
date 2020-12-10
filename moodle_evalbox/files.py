from os import listdir
from typing import List

from xmltodict import parse


def read_xml_file(file_path: str) -> str:
    f = open(file_path)
    return parse(f.read())


def create_file(filename: str, data):
    with open(filename, "w") as output:
        output.write(data)
