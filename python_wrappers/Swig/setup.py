from distutils.core import setup, Extension

extension_mod = Extension("_modmath", ["modmath_wrap.c", "operation.c"])

setup(name = "modmath", ext_modules=[extension_mod])
