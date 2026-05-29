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
    def __init__(self, arg0: str, arg1: ControlTemplate, arg2: int, arg3: int, arg4: int) -> None: ...
    def getTemplate(self) -> ControlTemplate: ...
    def getCurrentMode(self) -> int: ...
    def getCurrentActiveMode(self) -> int: ...
    def getModes(self) -> int: ...
    def getTemplateType(self) -> int: ...
