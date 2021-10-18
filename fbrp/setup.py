from setuptools import find_packages
from setuptools import setup


setup(
    name="facebook_robotics_platform",
    version="0.0.2",
    author="Leonid Shamis",
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        include=["*"],
    ),
    python_requires=">=3.7",
    install_requires=[
        "aiodocker>=0.21.0",
        "alephzero>=v0.3",
        "docker>=5.0.0",
        "psutil>=5.8.0",
        "six>=1.16.0",
    ],
)