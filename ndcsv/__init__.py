try:
    from .version import version as __version__  # noqa: F401
except ImportError:  # pragma: no cover
    raise ImportError('ndcsv not properly installed. If you are running '
                      'from the source directory, please instead '
                      'create a new virtual environment (using conda or '
                      'virtualenv) and then install it in-place by running: '
                      'pip install -e .')


from .read import read_csv  # noqa: F401
from .write import write_csv  # noqa: F401
