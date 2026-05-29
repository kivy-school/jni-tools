from typing import Any, ClassVar, overload
from javax.xml.namespace.QName import QName

class XPathVariableResolver:
    def resolveVariable(self, p0: QName) -> Any: ...
