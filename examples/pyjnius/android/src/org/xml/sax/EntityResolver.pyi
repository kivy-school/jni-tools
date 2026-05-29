from typing import Any, ClassVar, overload
from org.xml.sax.InputSource import InputSource

class EntityResolver:
    def resolveEntity(self, arg0: str, arg1: str) -> InputSource: ...
