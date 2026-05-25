from typing import Any, ClassVar, overload
from android.net.Uri import Uri

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Builder:
    """Forward declaration for ``android.net.Uri.Builder``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.net.Uri.Builder')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/net/Uri/Builder
    """
    ...

class ContentUris:
    def __init__(self) -> None: ...
    @staticmethod
    def parseId(arg0: Uri) -> int: ...
    @staticmethod
    def appendId(arg0: Builder, arg1: int) -> Builder: ...
    @staticmethod
    def withAppendedId(arg0: Uri, arg1: int) -> Uri: ...
    @staticmethod
    def removeId(arg0: Uri) -> Uri: ...
