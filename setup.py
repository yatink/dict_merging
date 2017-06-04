from setuptools import setup, find_packages

setup(
    name='dict_merge',
    version='0.1.0',
    description='Simple helpers for merging nested dictionaries',
    packages=find_packages(exclude=[
        '*.test',
        '*.test.*',
        'test.*',
        'test',
        '.ignored',]),
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'hypothesis'],
)
