from typing import Any, ClassVar, overload

class Result:
    PI_DISABLE_OUTPUT_ESCAPING: ClassVar[str]
    PI_ENABLE_OUTPUT_ESCAPING: ClassVar[str]
    def setSystemId(self, arg0: str) -> None: ...
    def getSystemId(self) -> str: ...
