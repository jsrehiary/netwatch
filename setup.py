# setup.py

from setuptools import setup, find_packages

setup(
    name='netwatch',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'psutil',
    ],
    author='Necrawldia',
    description='Lightweight network activity tracer for Python processes',
    entry_points={
    'console_scripts': [
        'netwatcher = netwatch.cli:main',  # example
        ],
    },
    url='https://github.com/jsrehiary/netwatch',  # Optional
)
