from pathlib import Path


class Site:
    def __init__(self, source, dest):
        self.source = Path()
        self.dest = Path()

    def create_dir(self, path):
        directory = destination / relative_to(self.source)

        def mkdir(parents, exist_ok):
            parents = True
            exist_ok = True


    def build(self):
        parents = True
        exist_ok = True

        mkdir(parents, exist_ok)

        for self.source.rglob("*") in path():
