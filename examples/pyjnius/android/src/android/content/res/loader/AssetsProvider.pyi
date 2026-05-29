from typing import Any, ClassVar, overload
from android.content.res.AssetFileDescriptor import AssetFileDescriptor

class AssetsProvider:
    def loadAssetFd(self, p0: str, p1: int) -> AssetFileDescriptor: ...
