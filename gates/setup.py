from setuptools import setup

setup(
    name="gates",
    version='0.1',
    py_modules=['gates'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gates=gates:cli
    ''',
)
