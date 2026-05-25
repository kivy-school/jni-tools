from typing import Any, ClassVar, overload
from android.graphics.ColorSpace import ColorSpace
from android.hardware.camera2.params.OutputConfiguration import OutputConfiguration
from java.util.concurrent.Executor import Executor

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class StateCallback:
    """Forward declaration for ``android.hardware.camera2.CameraExtensionSession.StateCallback``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.hardware.camera2.CameraExtensionSession.StateCallback')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/hardware/camera2/CameraExtensionSession/StateCallback
    """
    ...
class Named:
    """Forward declaration for ``android.graphics.ColorSpace.Named``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.ColorSpace.Named')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/ColorSpace/Named
    """
    ...

class ExtensionSessionConfiguration:
    def __init__(self, arg0: int, arg1: list, arg2: Executor, arg3: StateCallback) -> None: ...
    def getExtension(self) -> int: ...
    def setPostviewOutputConfiguration(self, arg0: OutputConfiguration) -> None: ...
    def getPostviewOutputConfiguration(self) -> OutputConfiguration: ...
    def getOutputConfigurations(self) -> list: ...
    def getStateCallback(self) -> StateCallback: ...
    def getExecutor(self) -> Executor: ...
    def setColorSpace(self, arg0: Named) -> None: ...
    def clearColorSpace(self) -> None: ...
    def getColorSpace(self) -> ColorSpace: ...
