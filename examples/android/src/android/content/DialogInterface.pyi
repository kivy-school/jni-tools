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

    class OnCancelListener:
        def onCancel(self, arg0: "DialogInterface") -> None: ...

    class OnClickListener:
        def onClick(self, arg0: "DialogInterface", arg1: int) -> None: ...

    class OnDismissListener:
        def onDismiss(self, arg0: "DialogInterface") -> None: ...

    class OnKeyListener:
        def onKey(self, arg0: "DialogInterface", arg1: int, arg2: KeyEvent) -> bool: ...

    class OnMultiChoiceClickListener:
        def onClick(self, arg0: "DialogInterface", arg1: int, arg2: bool) -> None: ...

    class OnShowListener:
        def onShow(self, arg0: "DialogInterface") -> None: ...
