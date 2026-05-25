from typing import Any, ClassVar, overload
from android.content.res.AssetFileDescriptor import AssetFileDescriptor

class AssetsProvider:
    def loadAssetFd(self, arg0: str, arg1: int) -> AssetFileDescriptor: ...
