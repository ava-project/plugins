import os
from distutils.core import setup, Extension

path = os.path.join(os.path.expanduser('~'), '.ava', 'plugins', 'say', 'say.cpp')
module = Extension('say', sources=[path])
setup(name = 'packagename',
    version='1.0',
    description = 'a test package',
    ext_modules = [module])
