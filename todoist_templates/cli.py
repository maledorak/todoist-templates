import argparse
import sys

from .api import get_api
from .errors import (ApiError, ParserError, ValidationError)
from .generator import generate_project
from .parsers import get_project
from .validator import validate_project


def _generate(path, project_name=None):
    try:
        api = get_api()
    except ApiError as error:
        print("Error:", error)
        sys.exit(1)

    try:
        project = get_project(path)
    except ParserError as error:
        print("Error:", error)
        sys.exit(1)

    try:
        validate_project(project)
    except ValidationError as error:
        print("Error:", error)
        sys.exit(1)

    if project_name:
        print('Using override project name: "{}" instead of: "{}"'.format(project_name, project['name']))
        project['name'] = project_name

    generate_project(api, project)


def main():
    parser = argparse.ArgumentParser(description='Generate Todoist project from template.')
    parser.add_argument('path', nargs='?', type=str, help='Path to template file')
    parser.add_argument('--name', type=str, help='Project name override', required=False)
    args = parser.parse_args()
    if not args.path:
        parser.print_help()
        sys.exit(1)

    _generate(args.path, project_name=args.name)
