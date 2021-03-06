import os
import shutil
import pytest


@pytest.fixture(scope="session")
def project_root_path():
    """Root folder for the project (with setup.py)"""
    filepath = os.path.split(os.path.abspath(__file__))[0]
    return os.path.normpath(os.path.join(filepath, '../../'))


@pytest.fixture(scope="session", autouse=True)
def test_output_folder(project_root_path):
    """(Re)make an output folder for the tests 
    at the begining of each test session."""
    folder = project_root_path + '/{{ cookiecutter.package_dir_name }}/tests/tmp'
    reset = True
    if reset:
        if os.path.isdir(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)
    return folder