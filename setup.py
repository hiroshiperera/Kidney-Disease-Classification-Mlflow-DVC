
#Project details, version, about the author those details are there
import setuptools

with open("REASME.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-Deep-Learning-MLflow-DVC"
AUTHOR_USER_NAME = "hirplk"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "hiroshiperera007@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for CNN app",
    Long_description = long_description,
    Long_description_content = "text/markdown",
    url = f"https://giithub.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir = {"": "src"},
    packages=setuptools.find_packages(where="src")
)