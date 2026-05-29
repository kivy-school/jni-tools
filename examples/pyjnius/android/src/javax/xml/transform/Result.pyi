from typing import Any, ClassVar, overload

class Result:
    PI_DISABLE_OUTPUT_ESCAPING: ClassVar[str]
    PI_ENABLE_OUTPUT_ESCAPING: ClassVar[str]
    def getSystemId(self) -> str: ...
    def setSystemId(self, p0: str) -> None: ...
