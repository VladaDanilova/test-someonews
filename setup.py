from setuptools import setup, find_packages

setup(
    name='MIGRATION TEST - link',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A simple project description',
    long_description=open('README.md').read(),
    install_requires=['altair', 'pytz'], 
    url='https://github.com/VladaDanilova/test-connectionSomeoneWS',
    author='Vlada Danilova',
    author_email='just.you177@gmail.com'
)
