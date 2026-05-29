from typing import Any, ClassVar, overload
from javax.xml.transform.Source import Source

class URIResolver:
    def resolve(self, p0: str, p1: str) -> Source: ...
