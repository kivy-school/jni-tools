from typing import Any, ClassVar, overload
from android.view.KeyEvent import KeyEvent

class DialogInterface:
    BUTTON1: ClassVar[int]
    BUTTON2: ClassVar[int]
    BUTTON3: ClassVar[int]
    BUTTON_NEGATIVE: ClassVar[int]
    BUTTON_NEUTRAL: ClassVar[int]
    BUTTON_POSITIVE: ClassVar[int]
    def cancel(self) -> None: ...
    def dismiss(self) -> None: ...

    class OnShowListener:
        def onShow(self, p0: "DialogInterface") -> None: ...

    class OnMultiChoiceClickListener:
        def onClick(self, p0: "DialogInterface", p1: int, p2: bool) -> None: ...

    class OnKeyListener:
        def onKey(self, p0: "DialogInterface", p1: int, p2: KeyEvent) -> bool: ...

    class OnDismissListener:
        def onDismiss(self, p0: "DialogInterface") -> None: ...

    class OnClickListener:
        def onClick(self, p0: "DialogInterface", p1: int) -> None: ...

    class OnCancelListener:
        def onCancel(self, p0: "DialogInterface") -> None: ...
