import sys

import pytest
from testing import path
from testing.py_info import read_fixture

from virtualenv.util.path import Path

# Allows to import from `testing` into test submodules.
sys.path.append(str(Path(__file__).parent))


@pytest.fixture
def py_info(py_info_name):
    return read_fixture(py_info_name)


@pytest.fixture
def mock_files(mocker):
    return lambda paths, files: path.mock_files(mocker, paths, files)


@pytest.fixture
def mock_pypy_libs(mocker):
    return lambda pypy, libs: path.mock_pypy_libs(mocker, pypy, libs)
