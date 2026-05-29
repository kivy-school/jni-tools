from typing import Any, ClassVar, overload
from android.text.Editable import Editable
from android.text.Spannable import Spannable
from android.view.KeyEvent import KeyEvent
from android.view.View import View

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Capitalize:
    """Forward declaration for ``android.text.method.TextKeyListener.Capitalize``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.text.method.TextKeyListener.Capitalize')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/text/method/TextKeyListener/Capitalize
    """
    ...

class QwertyKeyListener:
    def __init__(self, arg0: Capitalize, arg1: bool) -> None: ...
    @staticmethod
    def getInstance(arg0: bool, arg1: Capitalize) -> "QwertyKeyListener": ...
    @staticmethod
    def getInstanceForFullKeyboard() -> "QwertyKeyListener": ...
    def getInputType(self) -> int: ...
    def onKeyDown(self, arg0: View, arg1: Editable, arg2: int, arg3: KeyEvent) -> bool: ...
    @staticmethod
    def markAsReplaced(arg0: Spannable, arg1: int, arg2: int, arg3: str) -> None: ...
