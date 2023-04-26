import yaml

class Loader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_yaml(self):
        result = {}
        with open(self.file_path, "r") as stream:
            try:
                result = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print("Error loading YAML file {file}: {error}".format(file=file_path, error=exc))
        return result