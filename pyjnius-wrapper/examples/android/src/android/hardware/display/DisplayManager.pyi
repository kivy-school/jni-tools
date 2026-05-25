from typing import Any, ClassVar, overload
from android.hardware.display.HdrConversionMode import HdrConversionMode
from android.hardware.display.VirtualDisplay import VirtualDisplay
from android.hardware.display.VirtualDisplayConfig import VirtualDisplayConfig
from android.os.Handler import Handler
from android.view.Display import Display
from android.view.Surface import Surface

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Callback:
    """Forward declaration for ``android.hardware.display.VirtualDisplay.Callback``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.hardware.display.VirtualDisplay.Callback')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/hardware/display/VirtualDisplay/Callback
    """
    ...

class DisplayManager:
    DISPLAY_CATEGORY_PRESENTATION: ClassVar[str]
    MATCH_CONTENT_FRAMERATE_ALWAYS: ClassVar[int]
    MATCH_CONTENT_FRAMERATE_NEVER: ClassVar[int]
    MATCH_CONTENT_FRAMERATE_SEAMLESSS_ONLY: ClassVar[int]
    MATCH_CONTENT_FRAMERATE_UNKNOWN: ClassVar[int]
    VIRTUAL_DISPLAY_FLAG_AUTO_MIRROR: ClassVar[int]
    VIRTUAL_DISPLAY_FLAG_OWN_CONTENT_ONLY: ClassVar[int]
    VIRTUAL_DISPLAY_FLAG_PRESENTATION: ClassVar[int]
    VIRTUAL_DISPLAY_FLAG_PUBLIC: ClassVar[int]
    VIRTUAL_DISPLAY_FLAG_SECURE: ClassVar[int]
    def getDisplay(self, arg0: int) -> Display: ...
    @overload
    def getDisplays(self) -> list[Display]: ...
    @overload
    def getDisplays(self, arg0: str) -> list[Display]: ...
    def registerDisplayListener(self, arg0: "DisplayListener", arg1: Handler) -> None: ...
    def unregisterDisplayListener(self, arg0: "DisplayListener") -> None: ...
    @overload
    def createVirtualDisplay(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: Surface, arg5: int) -> VirtualDisplay: ...
    @overload
    def createVirtualDisplay(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: Surface, arg5: int, arg6: Callback, arg7: Handler) -> VirtualDisplay: ...
    @overload
    def createVirtualDisplay(self, arg0: VirtualDisplayConfig) -> VirtualDisplay: ...
    @overload
    def createVirtualDisplay(self, arg0: VirtualDisplayConfig, arg1: Handler, arg2: Callback) -> VirtualDisplay: ...
    def getHdrConversionMode(self) -> HdrConversionMode: ...
    def getMatchContentFrameRateUserPreference(self) -> int: ...

    class DisplayListener:
        def onDisplayAdded(self, arg0: int) -> None: ...
        def onDisplayRemoved(self, arg0: int) -> None: ...
        def onDisplayChanged(self, arg0: int) -> None: ...
