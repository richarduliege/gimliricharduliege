# -*- coding: utf-8 -*-
"""
pyGIMLi - An open-source library for modelling and inversion in geophysics
"""

import locale
import sys


def checkAndFixLocaleDecimal_point(verbose=False):
    """
    """
    if locale.localeconv()['decimal_point'] == ',':
        if verbose:
            print("Found locale decimal_point ',' "
                  "and change it to: decimal point '.'")
    try:
        locale.localeconv()['decimal_point']
        locale.setlocale(locale.LC_NUMERIC, 'C')
    except Exception as e:
        print(e)
        print('cannot set locale to decimal point')

    # LC_CTYPE should be something with UTF-8
    # export LC_CTYPE="de_DE.UTF-8"
    # python -c 'import sys; print(sys.stdout.encoding)'

checkAndFixLocaleDecimal_point(verbose=True)
#print(locale.localeconv()['decimal_point'])
#if locale.localeconv()['decimal_point'] == ',':
  #print("Found locale decimal_point ',' and change it to: decimal point '.'")
#try:
   #locale.localeconv()['decimal_point']
   #locale.setlocale(locale.LC_NUMERIC, 'C')
#except:
   #print('cannot set locale to decimal point')

################################################################################
# Please leave this block here until the following issue is fixed:
# https://github.com/ContinuumIO/anaconda-issues/issues/1068
if "conda" in __path__[0]:
    try:
        import PyQt5
        import matplotlib
        matplotlib.use("qt5agg", warn=False)
    except ImportError:
        pass
################################################################################

### Import everything that should be accessible through main namespace.
from ._version import get_versions
from .core import (BVector, CVector, DataContainer, DataContainerERT, dur,
                   Inversion, IVector, Line, Matrix, Mesh, Plane, Pos,
                   RVector3, Vector, abs, cat, center, exp, find, interpolate,
                   log, log10, logDropTol, math, matrix, min, search, setDebug,
                   setThreadCount, sort, sum, tic, toc, trans, unique,
                   versionStr, x, y, z, zero)
from .core.load import getConfigPath, getExampleFile, load, optImport
from .core.logger import (_, _d, _g, _r, _y, critical, d, debug, deprecated,
                          error, info, setLogLevel, setVerbose, v, verbose,
                          warn)
from .meshtools import createGrid, interpolate
from .solver import solve
# from .core import *
from .testing import test
from .utils import boxprint, cache, cut, unit
from .viewer import plt, show, wait

from .mplviewer.utils import prettyFloat as pf

def _get_branch():
    """Get current git branch."""
    from os.path import join, abspath, exists
    gitpath = abspath(join(__path__[0], "../../.git"))

    if exists(gitpath):
        from subprocess import check_output
        out = check_output(["git", "--git-dir", gitpath, "rev-parse",
                            "--abbrev-ref", "HEAD"]).decode("utf8")
        branch = out.split("\n")[0]
        if not "HEAD" in branch:
            return branch

_branch = _get_branch()
__version__ = get_versions()['version']

if get_versions()["dirty"]:
    __version__ = __version__.replace(".dirty", " (with local changes")
    if _branch:
        __version__ += " on %s branch)" % _branch
    else:
        __version__ += ")"
del get_versions, _get_branch, _branch

def version():
    """Shortcut to show and return current version."""
    info('Version: ' + __version__ + " core:" + versionStr())
    return __version__
