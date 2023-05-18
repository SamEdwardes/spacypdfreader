import shutil


def copy_readme(*args, **kwargs):
    shutil.copy("README.md", "docs/index.md")
