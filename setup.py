from setuptools import find_packages, setup

setup(
    name='jpmora',
    packages=find_packages(include=['jpmora']),
    version='0.1.0',
    description='Library to count Japanese mora',
    author='arutaki',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
