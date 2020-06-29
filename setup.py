
from setuptools import setup, find_packages
from zoom-cli.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='zoom-cli',
    version=VERSION,
    description='CLI-wrapper around the Zoom API',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Michael Brauweiler',
    author_email='rattletat@posteo.io',
    url='https://github.com/rattletat/zoom-cli',
    license='UNLICENSE',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'zoom-cli': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        zoom-cli = zoom-cli.main:main
    """,
)
