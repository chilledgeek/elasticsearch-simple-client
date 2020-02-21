from setuptools import setup, find_packages

setup(name='elasticsearch_simple_client',
      version="0.0.1",
      author="E CHOW",
      author_email="chilledgeek@gmail.com",
      description='Interact to any elasticsearch server, with simple upload and search functionality',
      url="https://github.com/chilledgeek/elasticsearch-simple-client",
      packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
      license="MIT",
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
      ],
      install_requires=['elasticsearch', 'pandas'])
