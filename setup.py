from setuptools import setup, find_packages
import platform

# Pull version from source without importing
# since we can't import something we haven't built yet :)
exec(open('kafka_influxdb/version.py').read())

# Create reStructuredText README file for PyPi
# http://stackoverflow.com/a/26737672/270334
try:
    import pypandoc

    long_description = pypandoc.convert('README.md',
                                        to='rst',
                                        extra_args=["--wrap=none", "--columns=200"],
                                        format='markdown_github')
    long_description = long_description.replace("\r", "")
except OSError as e:
    print("\n\n!!! pandoc not found, long_description is bad, don't upload this to PyPI !!!\n\n")
    import io

    # pandoc is not installed, fallback to using raw contents
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

requires = [
    "certifi",
    "funcsigs",
    "influxdb",
    "kafka-python",
    "pbr",
    "python-dateutil",
    "pytz",
    "PyYAML",
    "requests",
    "virtualenv",
    "wheel",
    "pytest-runner"
]

test_requires = [
    "pytest",
    'profilehooks'
]

# Get an additional speedup with ujson,
# which is faster than the normal Python json module.
# ujson does not work with PyPy
# See https://github.com/esnme/ultrajson/issues/98
if not platform.python_implementation() == 'PyPy':
    requires.extend([
        "ujson",
        "confluent_kafka"
    ])

setup(name='kafka_influxdb',
      version=__version__,
      description='A Kafka consumer for InfluxDB',
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: Apache Software License',
          'Topic :: Utilities',
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: Implementation :: PyPy",
      ],
      keywords='kafka influxdb metrics consumer',
      url='http://github.com/mre/kafka-influxdb',
      author='Matthias Endler',
      author_email='matthias-endler@gmx.net',
      license='Apache',
      packages=find_packages(),
      install_requires=requires,
      tests_require=test_requires,
      entry_points={
          'console_scripts': ['kafka_influxdb=kafka_influxdb.__main__:main'],
      },
      include_package_data=True,
      zip_safe=False)
