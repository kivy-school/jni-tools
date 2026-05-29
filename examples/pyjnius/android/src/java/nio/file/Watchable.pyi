from typing import Any, ClassVar, overload
from java.nio.file.WatchKey import WatchKey
from java.nio.file.WatchService import WatchService

class Watchable:
    @overload
    def register(self, p0: WatchService, p1: Any, p2: Any) -> WatchKey: ...
    @overload
    def register(self, p0: WatchService, p1: Any) -> WatchKey: ...
