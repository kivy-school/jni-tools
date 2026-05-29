from typing import Any, ClassVar, overload
from org.w3c.dom.Element import Element
from org.w3c.dom.TypeInfo import TypeInfo

class Attr:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]
    def getName(self) -> str: ...
    def getValue(self) -> str: ...
    def setValue(self, p0: str) -> None: ...
    def getSpecified(self) -> bool: ...
    def getOwnerElement(self) -> Element: ...
    def getSchemaTypeInfo(self) -> TypeInfo: ...
    def isId(self) -> bool: ...
