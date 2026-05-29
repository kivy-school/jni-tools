from typing import Any, ClassVar, overload
from android.service.controls.templates.ControlTemplate import ControlTemplate

class TemperatureControlTemplate:
    FLAG_MODE_COOL: ClassVar[int]
    FLAG_MODE_ECO: ClassVar[int]
    FLAG_MODE_HEAT: ClassVar[int]
    FLAG_MODE_HEAT_COOL: ClassVar[int]
    FLAG_MODE_OFF: ClassVar[int]
    MODE_COOL: ClassVar[int]
    MODE_ECO: ClassVar[int]
    MODE_HEAT: ClassVar[int]
    MODE_HEAT_COOL: ClassVar[int]
    MODE_OFF: ClassVar[int]
    MODE_UNKNOWN: ClassVar[int]
    TYPE_ERROR: ClassVar[int]
    TYPE_NO_TEMPLATE: ClassVar[int]
    TYPE_RANGE: ClassVar[int]
    TYPE_STATELESS: ClassVar[int]
    TYPE_TEMPERATURE: ClassVar[int]
    TYPE_THUMBNAIL: ClassVar[int]
    TYPE_TOGGLE: ClassVar[int]
    TYPE_TOGGLE_RANGE: ClassVar[int]
    def __init__(self, p0: str, p1: ControlTemplate, p2: int, p3: int, p4: int) -> None: ...
    def getTemplateType(self) -> int: ...
    def getCurrentActiveMode(self) -> int: ...
    def getCurrentMode(self) -> int: ...
    def getModes(self) -> int: ...
    def getTemplate(self) -> ControlTemplate: ...
