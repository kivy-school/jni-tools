from typing import Any, ClassVar, overload
from android.hardware.display.HdrConversionMode import HdrConversionMode
from android.hardware.display.VirtualDisplay import VirtualDisplay
from android.hardware.display.VirtualDisplayConfig import VirtualDisplayConfig
from android.os.Handler import Handler
from android.view.Display import Display
from android.view.Surface import Surface
from java.util.concurrent.Executor import Executor

class DisplayManager:
    DISPLAY_CATEGORY_PRESENTATION: ClassVar[str]
    EVENT_TYPE_DISPLAY_ADDED: ClassVar[int]
    EVENT_TYPE_DISPLAY_CHANGED: ClassVar[int]
    EVENT_TYPE_DISPLAY_REFRESH_RATE: ClassVar[int]
    EVENT_TYPE_DISPLAY_REMOVED: ClassVar[int]
    EVENT_TYPE_DISPLAY_STATE: ClassVar[int]
    MATCH_CONTENT_FRAMERATE_ALWAYS: ClassVar[int]
    MATCH_CONTENT_FRAMERATE_NEVER: ClassVar[int]
    MATCH_CONTENT_FRAMERATE_SEAMLESSS_ONLY: ClassVar[int]
    MATCH_CONTENT_FRAMERATE_UNKNOWN: ClassVar[int]
    VIRTUAL_DISPLAY_FLAG_AUTO_MIRROR: ClassVar[int]
    VIRTUAL_DISPLAY_FLAG_OWN_CONTENT_ONLY: ClassVar[int]
    VIRTUAL_DISPLAY_FLAG_PRESENTATION: ClassVar[int]
    VIRTUAL_DISPLAY_FLAG_PUBLIC: ClassVar[int]
    VIRTUAL_DISPLAY_FLAG_SECURE: ClassVar[int]
    @overload
    def getDisplays(self, p0: str) -> Any: ...
    @overload
    def getDisplays(self) -> Any: ...
    @overload
    def createVirtualDisplay(self, p0: str, p1: int, p2: int, p3: int, p4: Surface, p5: int, p6: Any, p7: Handler) -> VirtualDisplay: ...
    @overload
    def createVirtualDisplay(self, p0: str, p1: int, p2: int, p3: int, p4: Surface, p5: int) -> VirtualDisplay: ...
    @overload
    def createVirtualDisplay(self, p0: VirtualDisplayConfig, p1: Handler, p2: Any) -> VirtualDisplay: ...
    @overload
    def createVirtualDisplay(self, p0: VirtualDisplayConfig) -> VirtualDisplay: ...
    def getHdrConversionMode(self) -> HdrConversionMode: ...
    def getMatchContentFrameRateUserPreference(self) -> int: ...
    @overload
    def registerDisplayListener(self, p0: Any, p1: Handler) -> None: ...
    @overload
    def registerDisplayListener(self, p0: Executor, p1: int, p2: Any) -> None: ...
    def unregisterDisplayListener(self, p0: Any) -> None: ...
    def getDisplay(self, p0: int) -> Display: ...

    class DisplayListener:
        def onDisplayAdded(self, p0: int) -> None: ...
        def onDisplayChanged(self, p0: int) -> None: ...
        def onDisplayRemoved(self, p0: int) -> None: ...
