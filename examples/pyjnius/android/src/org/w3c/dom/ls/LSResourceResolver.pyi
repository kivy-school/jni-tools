from typing import Any, ClassVar, overload
from org.w3c.dom.ls.LSInput import LSInput

class LSResourceResolver:
    def resolveResource(self, p0: str, p1: str, p2: str, p3: str, p4: str) -> LSInput: ...
