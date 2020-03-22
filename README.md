todoist-templates
================
[![pypi](https://img.shields.io/pypi/v/todoist_templates.svg)](https://pypi.python.org/pypi/todoist_templates)

Create Todoist projects from file.

Supported file types:
 * yml, yaml

How to use?
-----------
* Install `pip install --user todoist_templates`
* Set environment variable with your TodoistApi `export TODOIST_API=123123123`
* Create project template based on `example_project.yml` file
* Run `todoist_templates path/to/project_template.yml`

Supported properties
--------
All supported properties based on this api: https://developer.todoist.com/sync/v8/

* `name` - Project name
* `color` - Project color [integer] from 30 to 49 - [More explanation](https://developer.todoist.com/sync/v8/#colors)
* `tasks` - Project tasks
    * `name` - Name of task
    * `priority` - Priority of task [integer] from 1 to 4
    * `tasks` - Subtasks
* `sections` - Project sections
    * `tasks` - Tasks in section, properties are the same like in base project `tasks`

Todo
----
* Add tests
* Add JSON support
