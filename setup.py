from setuptools import find_packages, setup

setup(
    name='investspielapi',
    packages=find_packages(include=['investspielapi', 'investspielapi.*']),
    include_package_data=True,
    version='0.1.0',
    description='A third party Investspiel API',
    author='mallo321123',
    author_email='mario@binary-kitchen.de',
    url='https://github.com/Mallo321123/Investspiel_library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    
    python_requires='>=3.6',
    install_requires=[
        'requests==2.32.3',
        'configparser==7.0.0'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    package_data={
        'investspielapi': ['config/*.conf'],
    },
)