from typing import Any, ClassVar, overload
from javax.xml.namespace.QName import QName
from javax.xml.xpath.XPathFunction import XPathFunction

class XPathFunctionResolver:
    def resolveFunction(self, arg0: QName, arg1: int) -> XPathFunction: ...
