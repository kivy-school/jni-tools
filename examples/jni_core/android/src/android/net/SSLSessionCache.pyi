from typing import Any, ClassVar, overload
from android.content.Context import Context
from java.io.File import File

class SSLSessionCache:
    @overload
    def __init__(self, p0: File) -> None: ...
    @overload
    def __init__(self, p0: Context) -> None: ...
