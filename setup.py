from setuptools import find_packages,setup
from typing import List

HYPHEN = '-e .'
def  get_requirements(file_path:str)->List[str]:
    '''
    this function is used to get all the pythonn requried packages for the project
    '''
    requirements= []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements


setup(
    name="ml_project",
    version="0.0.1",
    packages=find_packages(),
    author = ' arihant',
    author_email='arihantsingla21@gmail.com',
    install_requires = get_requirements('requirements.txt')
)

