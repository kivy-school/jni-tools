from typing import Any, ClassVar, overload

class ZipPathValidator:
    @staticmethod
    def clearCallback() -> None: ...
    @staticmethod
    def setCallback(p0: Any) -> None: ...

    class Callback:
        def onZipEntryAccess(self, p0: str) -> None: ...
