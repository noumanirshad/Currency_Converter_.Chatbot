from setuptools import find_packages, setup
from typing import List

hy_e = '-e .'

def get_requirements(path: str) -> List[str]:
    '''Returns a list of requirements'''
    requirement = []
    with open(path, 'r') as f: 
        requirement = f.readlines()
        requirement = [req.replace('\n', '') for req in requirement]
        if hy_e in requirement:
            requirement.remove(hy_e)
    return requirement


with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='Currency_Converter_Chatbot',
    version='0.0.1',
    author='noumanirshad',
    author_email='noumanirshad564@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL-3.0',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description='ChatBot Application',
    license="MIT License",
    long_description=readme,
    include_package_data=True,
    url='https://github.com/noumanirshad/Currency_Converter_.Chatbot.git',
    packages=find_packages(include=['Currency_Converter_Chatbot', 'Currency_Converter_Chatbot*']),
    install_requires=get_requirements('requirements.txt'),
    zip_safe=False,
)
