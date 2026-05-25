from typing import Any, ClassVar, overload
from java.lang.Runnable import Runnable
from java.util.concurrent.ThreadFactory import ThreadFactory

class Cleaner:
    @overload
    @staticmethod
    def create(p0: ThreadFactory) -> "Cleaner": ...
    @overload
    @staticmethod
    def create() -> "Cleaner": ...
    def register(self, p0: Any, p1: Runnable) -> Any: ...

    class Cleanable:
        def clean(self) -> None: ...
