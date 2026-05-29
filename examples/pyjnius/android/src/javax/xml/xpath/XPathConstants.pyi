from typing import Any, ClassVar, overload
from javax.xml.namespace.QName import QName

class XPathConstants:
    NUMBER: ClassVar[QName]
    STRING: ClassVar[QName]
    BOOLEAN: ClassVar[QName]
    NODESET: ClassVar[QName]
    NODE: ClassVar[QName]
    DOM_OBJECT_MODEL: ClassVar[str]
