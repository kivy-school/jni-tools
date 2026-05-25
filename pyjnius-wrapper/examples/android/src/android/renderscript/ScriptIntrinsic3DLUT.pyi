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

class ScriptIntrinsic3DLUT:
    @staticmethod
    def create(arg0: RenderScript, arg1: Element) -> "ScriptIntrinsic3DLUT": ...
    def setLUT(self, arg0: Allocation) -> None: ...
    @overload
    def forEach(self, arg0: Allocation, arg1: Allocation) -> None: ...
    @overload
    def forEach(self, arg0: Allocation, arg1: Allocation, arg2: LaunchOptions) -> None: ...
    def getKernelID(self) -> KernelID: ...
