import argparse
import sys

from .api import get_api
from .errors import (ApiError, ParserError, ValidationError)
from .generator import generate_project
from .parsers import get_project
from .validator import validate_project


def _generate(path):
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

    generate_project(api, project)


def main():
    parser = argparse.ArgumentParser(description='Generate Todoist project from template.')
    parser.add_argument('path', nargs='?', type=str, help='Path to template file')
    # parser.add_argument('path', nargs='?', type=argparse.FileType('r'), default=sys.stdin) // todo improve passing through bash pipe
    args = parser.parse_args()
    if not args.path:
        parser.print_help()
        sys.exit(1)

    _generate(args.path)
