from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

version = '1.0'

install_requires = [
    'requests'
]

setup(name='pymautic',
    version=version,
    description="Python Mautic API",
    long_description=README,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='mautic api',
    author='Jeff Tchang',
    author_email='jeff.tchang@gmail.com',
    url='',
    license='',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['pymautic=pymautic:main']
    }
)
