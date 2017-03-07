from setuptools import setup

setup(
    name = 'tickets',
    py_module = ['tickets', 'stations', 'trainscollection'],
    install_requires=['requests', 'docopt', 'prettytable', 'colorama'],
    entry_points={
        'console_scripts': ['tickets=tickets:cli']
    }
)