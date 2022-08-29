from setuptools import setup
import unittest


def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='utils_unibs',
      version='0.1',
      description='A set of utility functions',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Topic :: Plots :: Tables',
      ],
      keywords='plots unibs tables',
      url='',
      author='Mattia Chiari',
      author_email='m.chiari017@unibs.it',
      license='MIT',
      packages=['utils_unibs'],
      install_requires=[
          'numpy',
          'matplotlib'
      ],
      test_suite='tests',
      include_package_data=True,
      zip_safe=False)