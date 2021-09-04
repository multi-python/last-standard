import sys
import platform

py39 = sys.version_info >= (3, 9)
py38 = sys.version_info >= (3, 8)
py37 = sys.version_info >= (3, 7)

pypy = platform.python_implementation() == "PyPy"
cpython = platform.python_implementation() == "CPython"

win32 = sys.platform.startswith("win")
osx = sys.platform.startswith("darwin")

arm = "aarch" in platform.machine().lower()
