from typing import Any, ClassVar, overload
from java.lang.ref.Cleaner import Cleaner

class SystemCleaner:
    @staticmethod
    def cleaner() -> Cleaner: ...
