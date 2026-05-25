from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle

class AdMobAdapter:
    NEW_BUNDLE: ClassVar[str]
    def __init__(self) -> None: ...
    def buildExtrasBundle(self, arg0: Bundle, arg1: Bundle) -> Bundle: ...
