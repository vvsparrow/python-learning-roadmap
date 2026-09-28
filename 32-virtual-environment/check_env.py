import sys

import numpy
from packaging.version import Version


def check_environment() -> None:
    assert sys.prefix != sys.base_prefix, (
        "CRITICAL: Running outside virtual environment!"
    )
    assert sys.version_info >= (3, 12), "CRITICAL: Requires Python 3.12+"
    assert Version(numpy.__version__).major == 2, (
        "Version mismatch: Expected Numpy 2.5.3"
    )


if __name__ == "__main__":
    check_environment()
