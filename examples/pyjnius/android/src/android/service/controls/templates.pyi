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

from typing import Any, ClassVar, overload

class RangeTemplate:
    TYPE_ERROR: ClassVar[int]
    TYPE_NO_TEMPLATE: ClassVar[int]
    TYPE_RANGE: ClassVar[int]
    TYPE_STATELESS: ClassVar[int]
    TYPE_TEMPERATURE: ClassVar[int]
    TYPE_THUMBNAIL: ClassVar[int]
    TYPE_TOGGLE: ClassVar[int]
    TYPE_TOGGLE_RANGE: ClassVar[int]
    def __init__(self, p0: str, p1: float, p2: float, p3: float, p4: float, p5: str) -> None: ...
    def getTemplateType(self) -> int: ...
    def getCurrentValue(self) -> float: ...
    def getFormatString(self) -> str: ...
    def getStepValue(self) -> float: ...
    def getMaxValue(self) -> float: ...
    def getMinValue(self) -> float: ...

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
    def getCurrentActiveMode(self) -> int: ...
    def getCurrentMode(self) -> int: ...
    def getModes(self) -> int: ...
    def getTemplate(self) -> ControlTemplate: ...
    def getTemplateType(self) -> int: ...

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
    def getThumbnail(self) -> Icon: ...
    def getTemplateType(self) -> int: ...
    def isActive(self) -> bool: ...
    def getContentDescription(self) -> str: ...

from typing import Any, ClassVar, overload

class StatelessTemplate:
    TYPE_ERROR: ClassVar[int]
    TYPE_NO_TEMPLATE: ClassVar[int]
    TYPE_RANGE: ClassVar[int]
    TYPE_STATELESS: ClassVar[int]
    TYPE_TEMPERATURE: ClassVar[int]
    TYPE_THUMBNAIL: ClassVar[int]
    TYPE_TOGGLE: ClassVar[int]
    TYPE_TOGGLE_RANGE: ClassVar[int]
    def __init__(self, p0: str) -> None: ...
    def getTemplateType(self) -> int: ...

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

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class ControlButton:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: bool, p1: str) -> None: ...
    def getActionDescription(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def isChecked(self) -> bool: ...

