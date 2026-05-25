from typing import Any, ClassVar, overload

class DownloadListener:
    def onDownloadStart(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: int) -> None: ...
