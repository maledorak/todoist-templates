import os

import todoist

from .errors import ApiError

todoist_api = os.getenv('TODOIST_API')


def get_api():
    if not todoist_api:
        raise ApiError('Please set TODOIST_API environment variable and try again!')

    api = todoist.TodoistAPI(todoist_api)
    api.sync()

    if not api.state['user']:
        raise ApiError('Can\'t connect - probably TODOIST_API environment variable is wrong!')

    full_name = api.state['user']['full_name']
    print('TodoistAPI connected for user: {}'.format(full_name))
    return api
