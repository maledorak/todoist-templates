#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md', encoding='utf-8') as changelog_file:
    changelog = changelog_file.read()

requirements = [
    'PyYAML>=5.3.1',
    'todoist-python>=8.1.1'
]

setup_requirements = []

test_requirements = [
    "mock",
    "coverage"
]

setup(
    author="Mariusz Korzekwa",
    author_email='maledorak@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Create Todoist projects from yaml template files",
    entry_points={
        'console_scripts': [
            'todoist_templates=todoist_templates.cli:main',
        ],
    },
    python_requires='>=3.5',
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + changelog,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='todoist_templates',
    name='todoist_templates',
    packages=find_packages(include=['todoist_templates']),
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    url='https://github.com/maledorak/todoist-templates',
    version='0.0.1',
    zip_safe=False,
)
