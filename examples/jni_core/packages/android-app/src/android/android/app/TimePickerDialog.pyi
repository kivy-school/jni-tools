from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.DialogInterface import DialogInterface
from android.os.Bundle import Bundle
from android.widget.TimePicker import TimePicker

class TimePickerDialog:
    THEME_DEVICE_DEFAULT_DARK: ClassVar[int]
    THEME_DEVICE_DEFAULT_LIGHT: ClassVar[int]
    THEME_HOLO_DARK: ClassVar[int]
    THEME_HOLO_LIGHT: ClassVar[int]
    THEME_TRADITIONAL: ClassVar[int]
    BUTTON1: ClassVar[int]
    BUTTON2: ClassVar[int]
    BUTTON3: ClassVar[int]
    BUTTON_NEGATIVE: ClassVar[int]
    BUTTON_NEUTRAL: ClassVar[int]
    BUTTON_POSITIVE: ClassVar[int]
    @overload
    def __init__(self, p0: Context, p1: Any, p2: int, p3: int, p4: bool) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: int, p2: Any, p3: int, p4: int, p5: bool) -> None: ...
    def updateTime(self, p0: int, p1: int) -> None: ...
    def show(self) -> None: ...
    def onSaveInstanceState(self) -> Bundle: ...
    def onRestoreInstanceState(self, p0: Bundle) -> None: ...
    def onClick(self, p0: DialogInterface, p1: int) -> None: ...
    def onTimeChanged(self, p0: TimePicker, p1: int, p2: int) -> None: ...

    class OnTimeSetListener:
        def onTimeSet(self, p0: TimePicker, p1: int, p2: int) -> None: ...
