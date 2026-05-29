from typing import Any, ClassVar, overload

class ElementType:
    TYPE: ClassVar["ElementType"]
    FIELD: ClassVar["ElementType"]
    METHOD: ClassVar["ElementType"]
    PARAMETER: ClassVar["ElementType"]
    CONSTRUCTOR: ClassVar["ElementType"]
    LOCAL_VARIABLE: ClassVar["ElementType"]
    ANNOTATION_TYPE: ClassVar["ElementType"]
    PACKAGE: ClassVar["ElementType"]
    TYPE_PARAMETER: ClassVar["ElementType"]
    TYPE_USE: ClassVar["ElementType"]
    MODULE: ClassVar["ElementType"]
    RECORD_COMPONENT: ClassVar["ElementType"]
    TYPE: ClassVar["ElementType"]
    FIELD: ClassVar["ElementType"]
    METHOD: ClassVar["ElementType"]
    PARAMETER: ClassVar["ElementType"]
    CONSTRUCTOR: ClassVar["ElementType"]
    LOCAL_VARIABLE: ClassVar["ElementType"]
    ANNOTATION_TYPE: ClassVar["ElementType"]
    PACKAGE: ClassVar["ElementType"]
    TYPE_PARAMETER: ClassVar["ElementType"]
    TYPE_USE: ClassVar["ElementType"]
    MODULE: ClassVar["ElementType"]
    RECORD_COMPONENT: ClassVar["ElementType"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "ElementType": ...
