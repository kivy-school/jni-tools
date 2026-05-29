from typing import Any, ClassVar, overload
from android.service.controls.templates.ControlButton import ControlButton

class ToggleTemplate:
    TYPE_ERROR: ClassVar[int]
    TYPE_NO_TEMPLATE: ClassVar[int]
    TYPE_RANGE: ClassVar[int]
    TYPE_STATELESS: ClassVar[int]
    TYPE_TEMPERATURE: ClassVar[int]
    TYPE_THUMBNAIL: ClassVar[int]
    TYPE_TOGGLE: ClassVar[int]
    TYPE_TOGGLE_RANGE: ClassVar[int]
    def __init__(self, p0: str, p1: ControlButton) -> None: ...
    def getTemplateType(self) -> int: ...
    def getContentDescription(self) -> str: ...
    def isChecked(self) -> bool: ...
