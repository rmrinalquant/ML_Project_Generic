from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'
def get_requirements(file_path : str)->list[str]:
    '''Get requirements from requirements.txt'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='src',
    packages=find_packages(),
    version='0.0.1',
    author='Mrinal',
    author_email='rmmrinal.q@gmail.com',
    license='MIT',
    install_requires= get_requirements('requirement.txt'),
)