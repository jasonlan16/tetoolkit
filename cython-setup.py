from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['TEToolkit/EMAlgorithm.pyx',
                           'TEToolkit/GeneFeatures.pyx',
                           'TEToolkit/IntervalTree.pyx',
                           'TEToolkit/Normalization.pyx',
                           'TEToolkit/Prob.pyx',
                           'TEToolkit/TEindex.pyx',
                           'TEToolkit/ParseBEDFile.pyx',
                           'TEToolkit/ReadInputs.pyx',
                           'TEToolkit/FeatIO.pyx',
                          ],   
                          annotate=False),        
)

