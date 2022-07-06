from setuptools import setup, find_packages

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(
  name = 'dp_model',
  packages = find_packages(),
  include_package_data=True,
  version = '06.06.22',
  license='',
  description = 'Sugar analysis',
  author = 'William Finnigan',
  author_email = 'wjafinnigan@gmail.com',
  url = '',
  download_url = '',
  keywords = ['sugar'],
  install_requires=requirements,
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'],
)