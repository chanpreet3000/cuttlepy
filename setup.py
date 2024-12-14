from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cuttlepy",
    version="0.1.0",
    author="Chanpreet Singh",
    author_email="chanpreet3000@gmail.com",
    description="Typed python HTTP client wrapper for PRIMP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chanpreet3000/cuttlepy",
    project_urls={
        "Bug Tracker": "https://github.com/chanpreet3000/cuttlepy/issues",
        "Source Code": "https://github.com/chanpreet3000/cuttlepy",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "primp==0.8.3",
    ],
    keywords=[
        "http",
        "client",
        "wrapper",
        "primp",
        "requests",
        "httpx",
        "aiohhtp",
    ],
    package_data={
        "cuttlepy": ["py.typed"],
    },
    include_package_data=True,
)
