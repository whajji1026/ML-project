from setuptools import find_packages,setup
from typing import List



'''
this file setup.py is capable of building our machine learning 
project as a package
'''

hypen_e_dot='-e .'

'''Editable Mode ( pip install -e . )
When you install a Python package in editable mode (also known as development mode), 
Python will execute the package directly from the source code directory.
This means any changes you make to the source code should be reflected immediately 
without the need for reinstallation.
'''

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    
    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='whajji1026',
    author_email='wyeemhajjy26@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)