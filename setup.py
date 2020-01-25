from pathlib import Path
from setuptools import setup, find_namespace_packages
RUNNER_PATH = Path(Path.cwd().parent, 'runner')

TEST_REQUIREMENTS = ['pylint']

setup(
    name='runner-ext',
    version='2020.01.24.10',
    description='',
    url='https://github.com/interifter/runner-ext',
    author='interifter',
    author_email='zachary@interift.com',
    license='MIT',
    package_dir={"": "src"},
    install_requires=[
        f'runner@git+https://github.com/interifter/runner.git@master#egg=runner-2020.01.24.0'
    ],
    packages=find_namespace_packages(where="src"),
    zip_safe=False,
    entry_points='''
        [runner.colors.plugins] 
        blue = ext.blue
        green = ext.green
        
    ''',
    extras_require={
        'test':TEST_REQUIREMENTS
    }
    )