#setup.py created because to allow anybody can use all packages and all
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''this function will return the kist of requirements'''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        [req.replace('\n','')for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements





setup(
name='mlprojects',
version='0.0.1',
author='Kunal',
author_email='kunalmahajan0202gmail.com',
packges=find_packages(),
install_requires=get_requirements('requirements.txt')
)
