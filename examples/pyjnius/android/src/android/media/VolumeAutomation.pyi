from typing import Any, ClassVar, overload
from android.media.VolumeShaper import VolumeShaper

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Configuration:
    """Forward declaration for ``android.media.VolumeShaper.Configuration``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.media.VolumeShaper.Configuration')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/media/VolumeShaper/Configuration
    """
    ...

class VolumeAutomation:
    def createVolumeShaper(self, arg0: Configuration) -> VolumeShaper: ...
