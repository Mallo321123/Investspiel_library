from setuptools import find_packages, setup

setup(
    name='investspielapi',
    packages=find_packages(include=['investspielapi']),
    version='0.1.0',
    description='A third party Investspiel API',
    author='mallo321123',
    
    install_requires=[],
    read_requires=['requests', 'datetime', 'os', 'json', 'configparser'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)