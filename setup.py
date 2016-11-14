import versioneer
from distutils import sysconfig
from setuptools import setup, Extension

with open('requirements.txt', 'r') as fp:
  requirements = list(filter(bool, (line.strip() for line in fp)))

incDirs = [sysconfig.get_python_inc(), sysconfig.get_python_lib()]
setup(name='pyradiomics',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      packages=['radiomics'],
      data_files=[
        ('data', ['data/paramSchema.yaml', 'data/schemaFuncs.py', 'data/brain1_image.nrrd', 'data/brain1_label.nrrd'])],
      description='Radiomics features library for python',
      ext_modules=[Extension("radiomics._cmatrices",
                             ["radiomics/src/_cmatrices.c", "radiomics/src/cmatrices.c"],
                             include_dirs=incDirs)],
      url='http://github.com/Radiomics/pyradiomics',
      author='pyradiomics community',
      author_email='pyradiomics@googlegroups.com',
      license='Slicer',
      zip_safe=False,
      setup_requires=['cython'],
      install_requires=requirements)
