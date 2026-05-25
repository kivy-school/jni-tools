from typing import Any, ClassVar, overload

class ZipPathValidator:
    @staticmethod
    def clearCallback() -> None: ...
    @staticmethod
    def setCallback(arg0: "Callback") -> None: ...

    class Callback:
        def onZipEntryAccess(self, arg0: str) -> None: ...
