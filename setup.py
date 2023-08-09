from setuptools import find_packages, setup

setup(
    name='ubot',
    version="1.0",
    author="Subrat PP",
    author_email="XXX@XXX",
    description="Umbrella-Bot Research Assistant",
    long_description=
    "Bot to assist in coding and paper reading or writing. Here, U is for Umbrella.",
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "ubot"},
    requires=['numpy', 'torch', 'gym', 'matplotlib', 'scipy', 'pandas'],
    packages=find_packages(where="ubot"),
    python_requires=">=3.9",
)
