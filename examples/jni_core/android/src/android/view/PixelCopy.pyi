from typing import Any, ClassVar, overload
from android.graphics.Bitmap import Bitmap
from android.graphics.Rect import Rect
from android.os.Handler import Handler
from android.view.Surface import Surface
from android.view.SurfaceView import SurfaceView
from android.view.View import View
from android.view.Window import Window
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class PixelCopy:
    ERROR_DESTINATION_INVALID: ClassVar[int]
    ERROR_SOURCE_INVALID: ClassVar[int]
    ERROR_SOURCE_NO_DATA: ClassVar[int]
    ERROR_TIMEOUT: ClassVar[int]
    ERROR_UNKNOWN: ClassVar[int]
    SUCCESS: ClassVar[int]
    @overload
    @staticmethod
    def request(p0: Surface, p1: Rect, p2: Bitmap, p3: Any, p4: Handler) -> None: ...
    @overload
    @staticmethod
    def request(p0: Window, p1: Rect, p2: Bitmap, p3: Any, p4: Handler) -> None: ...
    @overload
    @staticmethod
    def request(p0: SurfaceView, p1: Rect, p2: Bitmap, p3: Any, p4: Handler) -> None: ...
    @overload
    @staticmethod
    def request(p0: Window, p1: Bitmap, p2: Any, p3: Handler) -> None: ...
    @overload
    @staticmethod
    def request(p0: SurfaceView, p1: Bitmap, p2: Any, p3: Handler) -> None: ...
    @overload
    @staticmethod
    def request(p0: Any, p1: Executor, p2: Consumer) -> None: ...
    @overload
    @staticmethod
    def request(p0: Surface, p1: Bitmap, p2: Any, p3: Handler) -> None: ...

    class Result:
        def getStatus(self) -> int: ...
        def getBitmap(self) -> Bitmap: ...

    class Request:
        def getSourceRect(self) -> Rect: ...
        def getDestinationBitmap(self) -> Bitmap: ...

        class Builder:
            def setSourceRect(self, p0: Rect) -> Any: ...
            @overload
            @staticmethod
            def ofSurface(p0: SurfaceView) -> Any: ...
            @overload
            @staticmethod
            def ofSurface(p0: Surface) -> Any: ...
            @overload
            @staticmethod
            def ofWindow(p0: Window) -> Any: ...
            @overload
            @staticmethod
            def ofWindow(p0: View) -> Any: ...
            def setDestinationBitmap(self, p0: Bitmap) -> Any: ...
            def build(self) -> Any: ...

    class OnPixelCopyFinishedListener:
        def onPixelCopyFinished(self, p0: int) -> None: ...
