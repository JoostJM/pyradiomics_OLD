import versioneer
from distutils import sysconfig
from setuptools import setup, Extension
import numpy

with open('requirements.txt', 'r') as fp:
  requirements = list(filter(bool, (line.strip() for line in fp)))

incDirs = [sysconfig.get_python_inc(), numpy.get_include()]
setup(name='pyradiomics',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      packages=['radiomics'],
      data_files=[
        ('data', ['data/paramSchema.yaml', 'data/schemaFuncs.py', 'data/brain1_image.nrrd', 'data/brain1_label.nrrd'])],
      description='Radiomics features library for python',
      ext_modules=[Extension("_cmatrices",
                             ["radiomics/src/_cmatrices.c", "radiomics/src/cmatrices.c"],
                             include_dirs=incDirs, extra_compile_args=['-std=c99'])],
      url='http://github.com/Radiomics/pyradiomics',
      author='pyradiomics community',
      author_email='pyradiomics@googlegroups.com',
      license='Slicer',
      zip_safe=False,
      setup_requires=['cython', 'numpy>=1.10.0'],
      install_requires=requirements)
