#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='attack-maltego',
    author='Tatsuya Daitoku',
    version='1.0',
    author_email='tadmaddad@gmail.com',
    url='https://github.com/tadmaddad/attack-maltego',
    description='Maltego transform for MITRE ATT&CK.',
    license='GPLv3',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    package_data={
        '': ['*.gif', '*.png', '*.conf', '*.mtz', '*.machine']  # list of resources
    },
    install_requires=[
        'canari>=3.3.10,<4'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
