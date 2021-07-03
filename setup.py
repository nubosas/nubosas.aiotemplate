#!/usr/bin/env python3

from setuptools import find_namespace_packages, setup

setup(
    name='nubosas.aiotemplate',
    author='Carlos Perelló Marín',
    author_email='carlos@nubosas.com',
    description='Nubosas aio template service',
    url='https://gitlab.com/nubosas/nubosas.aiotemplate/',
    namespace_packages=['nubosas'],
    packages=find_namespace_packages(include=['nubosas.*']),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=[
        'aiodns>=3.0.0',
        'aiohttp>=3.7.4.post0',
        'aiopg>=1.3.0',
        'alembic>=1.6.5',
        'brotlipy>=0.7.0',
        'cchardet>=2.1.7',
        'chardet>=4.0.0',
        'SQLAlchemy>=1.4.20',
    ],
    entry_points={
        'console_scripts': [
            'init-accounts-db = nubosas.aiotemplate.scripts.init_db:run',
            'nubosas-aiotemplate = nubosas.aiotemplate.main:run',
        ],
    },
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ]
)
