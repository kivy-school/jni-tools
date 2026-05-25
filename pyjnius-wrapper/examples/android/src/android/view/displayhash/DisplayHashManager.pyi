from typing import Any, ClassVar, overload
from android.view.displayhash.DisplayHash import DisplayHash
from android.view.displayhash.VerifiedDisplayHash import VerifiedDisplayHash

class DisplayHashManager:
    def getSupportedHashAlgorithms(self) -> set: ...
    def verifyDisplayHash(self, arg0: DisplayHash) -> VerifiedDisplayHash: ...
