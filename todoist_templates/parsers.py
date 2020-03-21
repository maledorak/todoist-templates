import yaml
from .errors import ParserError

def _open_yaml_project(path):
    with open(path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def get_project(path):
    openers_map = {
        'yaml': _open_yaml_project
    }

    # todo add automatic resolving file type
    file_type = 'yaml'
    opener = openers_map.get(file_type, None)
    if not opener:
        raise ParserError('This file is not supported! Supported files: [{}]'.format( openers_map.keys()))
    return opener(path)
