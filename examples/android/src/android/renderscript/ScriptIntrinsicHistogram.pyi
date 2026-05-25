from typing import Any, ClassVar, overload
from android.renderscript.Allocation import Allocation
from android.renderscript.Element import Element
from android.renderscript.RenderScript import RenderScript

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class LaunchOptions:
    """Forward declaration for ``android.renderscript.Script.LaunchOptions``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.renderscript.Script.LaunchOptions')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/renderscript/Script/LaunchOptions
    """
    ...
class KernelID:
    """Forward declaration for ``android.renderscript.Script.KernelID``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.renderscript.Script.KernelID')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/renderscript/Script/KernelID
    """
    ...
class FieldID:
    """Forward declaration for ``android.renderscript.Script.FieldID``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.renderscript.Script.FieldID')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/renderscript/Script/FieldID
    """
    ...

class ScriptIntrinsicHistogram:
    @staticmethod
    def create(arg0: RenderScript, arg1: Element) -> "ScriptIntrinsicHistogram": ...
    @overload
    def forEach(self, arg0: Allocation) -> None: ...
    @overload
    def forEach(self, arg0: Allocation, arg1: LaunchOptions) -> None: ...
    def setDotCoefficients(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...
    def setOutput(self, arg0: Allocation) -> None: ...
    @overload
    def forEach_Dot(self, arg0: Allocation) -> None: ...
    @overload
    def forEach_Dot(self, arg0: Allocation, arg1: LaunchOptions) -> None: ...
    def getKernelID_Separate(self) -> KernelID: ...
    def getFieldID_Input(self) -> FieldID: ...
