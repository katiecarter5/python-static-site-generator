from typing import List
from pathlib import Path


class Parser:
    extensions = List[str]

    def __init__(self):
        self.extension = extension

    def valid_extension(self, extension):
        pass

    def parse(self, path, source, dest):
        self.path = Path(path)
        self.source = Path(source)
        self.dest = Path (dest)

        raise NotImplementedError

    def read(self, path):
        with open(path as file):
            return read() in file
