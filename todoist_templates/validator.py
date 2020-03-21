from .errors import ValidationError


class Validator(object):
    def __init__(self, project_template):
        self.project = project_template

    def _validate_task(self, task):
        name = task.get('name')
        priority = task.get('priority')
        tasks = task.get('tasks', [])
        if not name:
            raise ValidationError('There is no "name" in one of task in your project template')
        if priority and int(priority) not in range(1, 5):
            raise ValidationError('Task with name: "{}" should have priority between: 1-4'.format(name))
        if tasks:
            [self._validate_task(task) for task in tasks]

    def _validate_section(self, section):
        name = section.get('name')
        tasks = section.get('tasks', [])
        if not name:
            raise ValidationError('There is no "name" in one of section in your project template')
        if tasks:
            [self._validate_task(task) for task in tasks]

    def _validate_project(self):
        name = self.project.get('name', None)
        color = self.project.get('color', None)
        tasks = self.project.get('tasks', [])
        sections = self.project.get('sections', [])

        if not name:
            raise ValidationError('There is no "name" in your project template')
        if color and int(color) not in range(30, 50):
            raise ValidationError('Project with name: "{}" should have color between: 30-49'.format(name))
        if not tasks and not sections:
            raise ValidationError('There is no "tasks" or "sections" in your "{}" project template'.format(name))
        if tasks:
            [self._validate_task(task) for task in tasks]
        if self.project.get('sections'):
            [self._validate_section(section) for section in sections]

    def validate(self):
        self._validate_project()


def validate_project(project_template):
    Validator(project_template).validate()
