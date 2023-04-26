import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="task manager",
    version="1.0.0",
    author="Aleksandra Titova",
    author_email="st076009@student.spbu.ru",
    description=("A simple task manager with dependency resolution."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alxtitova/Task_Manager",
    project_urls={
        "Bug Tracker": "https://github.com/alxtitova/Task_Manager/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "manager = taskmanager.cli.cli:main",
        ]
    }
)