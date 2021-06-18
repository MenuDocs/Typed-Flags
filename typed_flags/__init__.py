from .typed_flags import TypedFlags
from .exceptions import ReservedKeyword

__version__ = "1.1.1"

import logging
from collections import namedtuple

logging.getLogger(__name__).addHandler(logging.NullHandler())
VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel serial")
version_info = VersionInfo(major=1, minor=1, micro=1, releaselevel="final", serial=0)
