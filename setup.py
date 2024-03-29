from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.rst")).read()
NEWS = open(os.path.join(here, "NEWS.txt")).read()

version = "0.0.2"

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]

setup(
    name="dynamic_heartbeat",
    version=version,
    description="Dynamic Heartbeat Interval Generator for Python.",
    long_description=README + "\n\n" + NEWS,
    classifiers=[
        # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords="dynamic_heartbeat python",
    author="Hobee Liu",
    author_email="Hobee.Liu@gmail.com",
    url="https://github.com/HoBeedzc",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={"console_scripts": ["dynamic_heartbeat=dynamic_heartbeat:main"]},
)
