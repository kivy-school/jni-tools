from typing import Any, ClassVar, overload

class DownloadListener:
    def onDownloadStart(self, p0: str, p1: str, p2: str, p3: str, p4: int) -> None: ...
