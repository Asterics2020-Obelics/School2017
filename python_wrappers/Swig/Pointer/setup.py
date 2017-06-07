from distutils.core import setup, Extension

extension_mod = Extension("_modarray", ["modarray_wrap.c", "array_sum.c"])

setup(name = "modarray", ext_modules=[extension_mod])
