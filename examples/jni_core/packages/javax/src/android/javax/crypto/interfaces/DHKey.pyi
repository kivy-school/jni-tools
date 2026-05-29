from typing import Any, ClassVar, overload
from javax.crypto.spec.DHParameterSpec import DHParameterSpec

class DHKey:
    def getParams(self) -> DHParameterSpec: ...
