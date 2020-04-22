from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='api-homebank',
      version='0.1',
      description='Api for homebank.kz',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Asetss/api-homebank.kz.git',
      author='Asetss',
      author_email='asets@protonmail.com',
      license='MIT',
      packages=['api_homebank'],
      zip_safe=False)