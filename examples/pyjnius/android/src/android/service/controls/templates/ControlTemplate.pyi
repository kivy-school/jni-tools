from typing import Any, ClassVar, overload

class ControlTemplate:
    TYPE_ERROR: ClassVar[int]
    TYPE_NO_TEMPLATE: ClassVar[int]
    TYPE_RANGE: ClassVar[int]
    TYPE_STATELESS: ClassVar[int]
    TYPE_TEMPERATURE: ClassVar[int]
    TYPE_THUMBNAIL: ClassVar[int]
    TYPE_TOGGLE: ClassVar[int]
    TYPE_TOGGLE_RANGE: ClassVar[int]
    def getTemplateId(self) -> str: ...
    @staticmethod
    def getErrorTemplate() -> "ControlTemplate": ...
    @staticmethod
    def getNoTemplateObject() -> "ControlTemplate": ...
    def getTemplateType(self) -> int: ...
