from setuptools import setup, find_packages
import os

# Read the README file if it exists
this_directory = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

setup(
    name="customErrorMessagesToSaveYourMentalHealth",
    version="0.1.1",
    packages=find_packages(),
    description="DONT KILL YOURSELF JUST YET, ENJOY ADDING EMOJIS AND WHATNOT TO YOUR ERROR MESSAGES",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Teo Richard",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
