import multiprocessing  # noqa

from setuptools import setup, find_packages

requirements = []
with open('requirements.txt', 'r') as in_:
    requirements = in_.readlines()

setup(
    name='myfitnesspal',
    version='1.0',
    url='http://github.com/realPrimoh/myfitnesspal-scraper/',
    description='Access health and fitness data stored in Myfitnesspal',
    author='Priyam Mohanty',
    author_email='priyam.mohanty@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    install_requires=requirements,
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock',
    ],
    entry_points={
        'console_scripts': [
            'myfitnesspal = myfitnesspal.cmdline:main'
        ]
    },
)
