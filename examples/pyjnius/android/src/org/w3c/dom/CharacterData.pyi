from typing import Any, ClassVar, overload

class CharacterData:
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
    def getLength(self) -> int: ...
    def setData(self, p0: str) -> None: ...
    def getData(self) -> str: ...
    def substringData(self, p0: int, p1: int) -> str: ...
    def appendData(self, p0: str) -> None: ...
    def insertData(self, p0: int, p1: str) -> None: ...
    def deleteData(self, p0: int, p1: int) -> None: ...
    def replaceData(self, p0: int, p1: int, p2: str) -> None: ...
