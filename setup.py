from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="teste_juan3232323",
    version="0.0.1",
    author="juan",
    author_email="juanpablomonteirofernandes@gmail.com",
    description="pequenas funções pertecentes a uma calculadora",
    long_description=page_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)