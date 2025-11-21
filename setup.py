from typing import List
from setuptools import find_packages, setup

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()

    # Remove "-e ." if someone accidentally put it in requirements.txt
    if '-e .' in requirements:
        requirements.remove('-e .')

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='GauravSahu',
    author_email='gaurav.sahu0112@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)