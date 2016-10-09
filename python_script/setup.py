from setuptools import setup


requirements = [
    'click>=6.6',
    'jenkinsapi>=0.3.2'
]

setup(
    name = "seedstars-script",
    version = "0.1.0",
    packages=['script'],

    entry_points={
        'console_scripts': [
            'seedstars-script=script.cli:main'
        ]
    },
    install_requires=requirements,
    license="MIT license",
    author = "Richard Oyudo",
    author_email = "ebube.rc@gmail.com",
    url='https://github.com/yudori/seedstars_challenge',
    description = "This is a python script for the seedstars challenge",
    test_suite='tests',
)