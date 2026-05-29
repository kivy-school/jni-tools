from typing import Any, ClassVar, overload
from org.w3c.dom.Node import Node

class DOMLocator:
    def getOriginatingNode(self) -> Node: ...
