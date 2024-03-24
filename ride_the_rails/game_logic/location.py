
class Location:

    def __init__(self, name, *, paths=None) -> None:
        self.name = name
        self.paths = [] if paths is None else paths
    
    def add_path(self, path):
        self.paths.append(path)