from typing import Any, ClassVar, overload

class XmlResourceParser:
    CDSECT: ClassVar[int]
    COMMENT: ClassVar[int]
    DOCDECL: ClassVar[int]
    END_DOCUMENT: ClassVar[int]
    END_TAG: ClassVar[int]
    ENTITY_REF: ClassVar[int]
    FEATURE_PROCESS_DOCDECL: ClassVar[str]
    FEATURE_PROCESS_NAMESPACES: ClassVar[str]
    FEATURE_REPORT_NAMESPACE_ATTRIBUTES: ClassVar[str]
    FEATURE_VALIDATION: ClassVar[str]
    IGNORABLE_WHITESPACE: ClassVar[int]
    NO_NAMESPACE: ClassVar[str]
    PROCESSING_INSTRUCTION: ClassVar[int]
    START_DOCUMENT: ClassVar[int]
    START_TAG: ClassVar[int]
    TEXT: ClassVar[int]
    TYPES: ClassVar[Any]
    def getAttributeNamespace(self, p0: int) -> str: ...
    def close(self) -> None: ...
