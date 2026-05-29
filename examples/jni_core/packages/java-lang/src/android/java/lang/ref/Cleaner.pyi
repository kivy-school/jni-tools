from typing import Any, ClassVar, overload
from java.lang.Runnable import Runnable
from java.util.concurrent.ThreadFactory import ThreadFactory

class Cleaner:
    def register(self, p0: Any, p1: Runnable) -> Any: ...
    @overload
    @staticmethod
    def create() -> "Cleaner": ...
    @overload
    @staticmethod
    def create(p0: ThreadFactory) -> "Cleaner": ...

    class Cleanable:
        def clean(self) -> None: ...
