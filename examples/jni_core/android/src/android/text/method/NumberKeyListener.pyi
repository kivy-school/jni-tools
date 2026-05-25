from typing import Any, ClassVar, overload
from android.text.Editable import Editable
from android.text.Spanned import Spanned
from android.view.KeyEvent import KeyEvent
from android.view.View import View

class NumberKeyListener:
    META_ALT_LOCKED: ClassVar[int]
    META_ALT_ON: ClassVar[int]
    META_CAP_LOCKED: ClassVar[int]
    META_SHIFT_ON: ClassVar[int]
    META_SYM_LOCKED: ClassVar[int]
    META_SYM_ON: ClassVar[int]
    def __init__(self) -> None: ...
    def onKeyDown(self, p0: View, p1: Editable, p2: int, p3: KeyEvent) -> bool: ...
    def filter(self, p0: str, p1: int, p2: int, p3: Spanned, p4: int, p5: int) -> str: ...
