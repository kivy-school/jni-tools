from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.text.Editable import Editable
from android.view.View import View
from android.widget.AdapterView import AdapterView

class CharacterPickerDialog:
    BUTTON1: ClassVar[int]
    BUTTON2: ClassVar[int]
    BUTTON3: ClassVar[int]
    BUTTON_NEGATIVE: ClassVar[int]
    BUTTON_NEUTRAL: ClassVar[int]
    BUTTON_POSITIVE: ClassVar[int]
    def __init__(self, p0: Context, p1: View, p2: Editable, p3: str, p4: bool) -> None: ...
    def onItemClick(self, p0: AdapterView, p1: View, p2: int, p3: int) -> None: ...
    def onClick(self, p0: View) -> None: ...
