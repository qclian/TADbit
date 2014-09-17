

from pytadbit._version                 import __version__
from pytadbit.tadbit                   import tadbit, batch_tadbit, find_tads
from pytadbit.chromosome               import Chromosome
from pytadbit.experiment               import Experiment
from pytadbit.alignment                import Alignment, randomization_test, align_experiments
from pytadbit.chromosome               import load_chromosome
from pytadbit.imp.structuralmodels     import StructuralModels
from pytadbit.imp.structuralmodels     import load_structuralmodels
from pytadbit.imp.impmodel             import load_impmodel_from_cmm
from pytadbit.imp.impmodel             import load_impmodel_from_xyz
from pytadbit.imp.impmodel             import IMPmodel
from pytadbit.boundary_aligner.aligner import align
try:
    from pytadbit.imp.impoptimizer import IMPoptimizer
except ImportError:
    from warnings import warn
    warn('IMP not found, check PYTHONPATH\n')


def get_dependencies_version():
    """
    Check versions of TADbit and all dependencies, as well and retieves system
    info. May be used to ensure reproductibility.
    
    :returns: string with description of versions installed
    """
    versions = {'  TADbit': __version__ + '\n\n'}
    try:
        import IMP
        try:
            versions['IMP'] = IMP.kernel.get_module_version()
            IMP.kernel.random_number_generator.seed(1)
            seed = IMP.kernel.random_number_generator()
        except AttributeError:
            versions['IMP'] = IMP.get_module_version()
            IMP.random_number_generator.seed(1)
            seed = IMP.random_number_generator()
        versions['IMP'] += ' (random seed indexed at 1 = %s)' % (seed)
    except ImportError:
        versions['IMP'] = 'Not found'
    try:
        import scipy
        versions['scipy'] = scipy.__version__
    except ImportError:
        versions['scipy'] = 'Not found'
    try:
        import numpy
        versions['numpy'] = numpy.__version__
    except ImportError:
        versions['numpy'] = 'Not found'
    try:
        import matplotlib
        versions['matplotlib'] = matplotlib.__version__
    except ImportError:
        versions['matplotlib'] = 'Not found'
    from subprocess import Popen, PIPE
    try:
        mcl, err = Popen(['mcl', '--version'], stdout=PIPE,
                         stderr=PIPE).communicate()
        versions['MCL'] = mcl.split()[1]
    except:
        versions['MCL'] = 'Not found'
    try:
        chi, err = Popen(['chimera', '--version'], stdout=PIPE,
                         stderr=PIPE).communicate()
        versions['Chimera'] = chi.strip()
    except:
        versions['Chimera'] = 'Not found'
    try:
        chi, err = Popen(['chimera', '--version'], stdout=PIPE,
                         stderr=PIPE).communicate()
        versions['Chimera'] = chi.strip()
    except:
        versions['Chimera'] = 'Not found'
    try:
        uname, err = Popen(['uname', '-rom'], stdout=PIPE,
                           stderr=PIPE).communicate()
        versions[' Machine'] = uname
    except:
        versions[' Machine'] = 'Not found'

    return '\n'.join(['%15s : %s' % (k, versions[k]) for k in
                      sorted(versions.keys())])
