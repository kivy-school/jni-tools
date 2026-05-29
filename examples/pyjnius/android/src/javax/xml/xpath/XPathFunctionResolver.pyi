from typing import Any, ClassVar, overload
from javax.xml.namespace.QName import QName
from javax.xml.xpath.XPathFunction import XPathFunction

class XPathFunctionResolver:
    def resolveFunction(self, p0: QName, p1: int) -> XPathFunction: ...
