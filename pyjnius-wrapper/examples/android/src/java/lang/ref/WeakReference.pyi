from typing import Any, ClassVar, overload
from java.lang.ref.ReferenceQueue import ReferenceQueue

class WeakReference:
    @overload
    def __init__(self, arg0: Any) -> None: ...
    @overload
    def __init__(self, arg0: Any, arg1: ReferenceQueue) -> None: ...
