from typing import Any, ClassVar, overload
from org.w3c.dom.Element import Element
from org.w3c.dom.Node import Node

class LSParserFilter:
    FILTER_ACCEPT: ClassVar[int]
    FILTER_REJECT: ClassVar[int]
    FILTER_SKIP: ClassVar[int]
    FILTER_INTERRUPT: ClassVar[int]
    def acceptNode(self, p0: Node) -> int: ...
    def getWhatToShow(self) -> int: ...
    def startElement(self, p0: Element) -> int: ...
