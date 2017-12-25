from setuptools import setup

setup(
    name="gates",
    version='1.0',
    py_modules=['calc'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gates=gates:gates
    ''',
)
