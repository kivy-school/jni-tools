from typing import Any, ClassVar, overload
from android.graphics.drawable.Icon import Icon

class ThumbnailTemplate:
    TYPE_ERROR: ClassVar[int]
    TYPE_NO_TEMPLATE: ClassVar[int]
    TYPE_RANGE: ClassVar[int]
    TYPE_STATELESS: ClassVar[int]
    TYPE_TEMPERATURE: ClassVar[int]
    TYPE_THUMBNAIL: ClassVar[int]
    TYPE_TOGGLE: ClassVar[int]
    TYPE_TOGGLE_RANGE: ClassVar[int]
    def __init__(self, p0: str, p1: bool, p2: Icon, p3: str) -> None: ...
    def getContentDescription(self) -> str: ...
    def getThumbnail(self) -> Icon: ...
    def getTemplateType(self) -> int: ...
    def isActive(self) -> bool: ...
