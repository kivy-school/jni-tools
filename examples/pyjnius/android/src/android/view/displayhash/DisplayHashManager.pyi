from typing import Any, ClassVar, overload
from android.view.displayhash.DisplayHash import DisplayHash
from android.view.displayhash.VerifiedDisplayHash import VerifiedDisplayHash

class DisplayHashManager:
    def verifyDisplayHash(self, p0: DisplayHash) -> VerifiedDisplayHash: ...
    def getSupportedHashAlgorithms(self) -> set: ...
