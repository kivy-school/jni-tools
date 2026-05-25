from typing import Any, ClassVar, overload

class CodingErrorAction:
    IGNORE: ClassVar["CodingErrorAction"]
    REPLACE: ClassVar["CodingErrorAction"]
    REPORT: ClassVar["CodingErrorAction"]
    def toString(self) -> str: ...
