from typing import Any, ClassVar, overload
from org.w3c.dom.DOMError import DOMError

class DOMErrorHandler:
    def handleError(self, arg0: DOMError) -> bool: ...
