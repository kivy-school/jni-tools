from typing import Any, ClassVar, overload
from android.service.controls.templates.ControlButton import ControlButton
from android.service.controls.templates.RangeTemplate import RangeTemplate

class ToggleRangeTemplate:
    TYPE_ERROR: ClassVar[int]
    TYPE_NO_TEMPLATE: ClassVar[int]
    TYPE_RANGE: ClassVar[int]
    TYPE_STATELESS: ClassVar[int]
    TYPE_TEMPERATURE: ClassVar[int]
    TYPE_THUMBNAIL: ClassVar[int]
    TYPE_TOGGLE: ClassVar[int]
    TYPE_TOGGLE_RANGE: ClassVar[int]
    @overload
    def __init__(self, p0: str, p1: bool, p2: str, p3: RangeTemplate) -> None: ...
    @overload
    def __init__(self, p0: str, p1: ControlButton, p2: RangeTemplate) -> None: ...
    def getTemplateType(self) -> int: ...
    def getActionDescription(self) -> str: ...
    def getRange(self) -> RangeTemplate: ...
    def isChecked(self) -> bool: ...
