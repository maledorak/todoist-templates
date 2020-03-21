class Generator(object):
    def __init__(self, api, project):
        self.api = api
        self.project = project

    def _generate_task(self, task_template, project_id, section_id=None, parent_id=None):
        name = task_template.get('name')
        priority = task_template.get('priority')
        tasks = task_template.get('tasks', [])

        task = self.api.items.add(
            content=name,
            project_id=project_id,
            section_id=section_id,
            parent_id=parent_id,
            priority=priority
        )
        [self._generate_task(
            task_item,
            project_id=project_id,
            section_id=section_id,
            parent_id=task['id']
        ) for task_item in tasks]

    def _generate_section(self, section_template, project_id):
        name = section_template.get('name')
        tasks = section_template.get('tasks', [])

        section = self.api.sections.add(
            name=name,
            project_id=project_id
        )
        [self._generate_task(
            task_item,
            project_id=project_id,
            section_id=section['id']
        ) for task_item in tasks]

    def _generate_project(self):
        name = self.project.get('name')
        color = self.project.get('color')
        tasks = self.project.get('tasks', [])
        sections = self.project.get('sections', [])

        project = self.api.projects.add(name=name, color=color)
        [self._generate_task(task_item, project_id=project['id']) for task_item in tasks]
        [self._generate_section(section_item, project_id=project['id']) for section_item in sections]

    def generate(self, dry_run=False):
        self._generate_project()

        if not dry_run:
            self.api.commit()
        print('Project "{}" was generated'.format(self.project.get('name')))


def generate_project(api, project):
    Generator(api, project).generate()
