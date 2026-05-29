from typing import Any, ClassVar, overload
from org.w3c.dom.DOMImplementation import DOMImplementation
from org.w3c.dom.DOMImplementationList import DOMImplementationList

class DOMImplementationSource:
    def getDOMImplementationList(self, p0: str) -> DOMImplementationList: ...
    def getDOMImplementation(self, p0: str) -> DOMImplementation: ...
