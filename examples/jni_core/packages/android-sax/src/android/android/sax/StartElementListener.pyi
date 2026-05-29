from typing import Any, ClassVar, overload
from org.xml.sax.Attributes import Attributes

class StartElementListener:
    def start(self, p0: Attributes) -> None: ...
