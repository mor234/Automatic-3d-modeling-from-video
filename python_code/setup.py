from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("extract_photos_Cython.pyx")
)


# To compile, run the following command:
#      python setup.py build_ext --inplace
