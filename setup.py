# taken from https://github.com/pypa/sampleproject/blob/master/setup.py

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='bokehjournal', 
      version='0.1.0',
      description='Pretty HTML pages for Bokeh Charts',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/ryanhausen/bokehjournal',
      author='Ryan Hausen',
      author_email='ryan.hausen@gmail.com',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Bokeh Users',
          'Topic :: Data Visualization',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6'
      ],
      keywords='bokeh html visualization',
      packages=find_packages(),
      install_requires=[
          'webbrowser',
          'dominate',
          'bokeh'
      ])
