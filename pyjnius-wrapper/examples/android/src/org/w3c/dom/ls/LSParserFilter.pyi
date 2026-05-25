from typing import Any, ClassVar, overload
from org.w3c.dom.Element import Element
from org.w3c.dom.Node import Node

class LSParserFilter:
    FILTER_ACCEPT: ClassVar[int]
    FILTER_INTERRUPT: ClassVar[int]
    FILTER_REJECT: ClassVar[int]
    FILTER_SKIP: ClassVar[int]
    def startElement(self, arg0: Element) -> int: ...
    def acceptNode(self, arg0: Node) -> int: ...
    def getWhatToShow(self) -> int: ...
