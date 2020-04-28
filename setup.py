'''
Setup file for OpenAQAPIDataset
'''

import os
import setuptools

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

install_requires = [x.strip() for x in read('requirements.txt') if ('git+' not in x) and
                    (not x.startswith('#')) and (not x.startswith('-'))]

params = dict(name="openaqdataset",
              version="0.0.1",
              author="Santhoshkumar S",
              author_email="santhoshramuk@gmail.com",
              description="openaqdataset: An API Wrapper for generating dataset from OpenAQ",
              long_description=read('README.md'),
              license="MIT",
              keywords=['Air Quality','OpenAQ', 'API', 'Dataset Generator'],
              url="https://github.com/santhosh790/openaqapidataset",
              packages=setuptools.find_packages(),
              classifiers=["Development Status :: 3 - Alpha",
                           "Intended Audience :: Developers",
                           "Intended Audience :: Science/Research",
                           "License :: OSI Approved :: MIT License",
                           "Topic :: Scientific/Engineering",
                           'Programming Language :: Python',
                           'Programming Language :: Python :: 3.5',
                           'Programming Language :: Python :: 3.6',
                           ],
              )

try:
    from setuptools import setup

    params["install_requires"] = install_requires
    #params["extras_require"] = {"examples": ["parsimony>=0.2.1", "matplotlib>=1.1.1rc"],
    #                           "test": ["doctest"],
    #                           "tests": ["doctest", "nose", "unittest"],
    #                            }
except:
    from distutils.core import setup

setup(**params)