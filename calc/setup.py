from setuptools import setup

setup(
    name="calc",
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        calc=calc:calc
    ''',
)
