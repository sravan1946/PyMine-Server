from setuptools import setup


with open("README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="PyMine",
    version="0.1.0",
    description=("TODO"),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="TODO",
    author_email="TODO",
    license="GPLv3",
    packages=[
        "pymine",
        "pymine.api",
        "pymine.data",
        "pymine.logic",
        "pymine.net",
        "pymine.types",
        "pymine.util",
    ],
    keywords="pymine voxel game",
    install_requires=[
        "aiofile=>3.4.0",
        "aiohttp=>3.7.4",
        "async-timeout=>3.0.1",
        "asyncio-dgram=>1.2.0",
        "attrs=>20.3.0",
        "caio=>0.7.0",
        "cffi=>1.14.5",
        "chardet=>3.0.4",
        "classy-json=>3.0.3",
        "colorama=>0.4.4",
        "cryptography=>3.4.6",
        "gitdb=>4.0.5",
        "GitPython=>3.1.13",
        "idna=>3.1",
        "immutables=>0.15",
        "multidict=>5.1.0",
        "mutf8=>1.0.3",
        "numpy=>1.20.1",
        "pycparser=>2.20",
        "PyYAML=>5.4.1",
        "smmap=>3.0.5",
        "typing-extensions=>3.7.4.3",
        "yarl=>1.6.3",
        "prompt-toolkit=>3.0.16",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Games/Entertainment :: Simulation",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django CMS :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    url="https://github.com/py-mine/PyMine",
    project_urls={
        "Documentation": "TODO",
        "Source Code": "TODO",
        "Bug Tracker": "TODO",
        "Changelog": "TODO",
    },
)
