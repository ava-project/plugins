import os
from distutils.core import setup, Extension

path = os.path.join(os.path.expanduser('~'), '.ava', 'plugins', 'hello_world', 'hello_world.cpp')
module = Extension('hello_world', sources=[path])
setup(name = 'packagename',
    version='1.0',
    description = 'a test package',
    ext_modules = [module])
