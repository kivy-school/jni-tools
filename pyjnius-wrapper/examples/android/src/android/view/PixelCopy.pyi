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
    def request(arg0: SurfaceView, arg1: Bitmap, arg2: "OnPixelCopyFinishedListener", arg3: Handler) -> None: ...
    @overload
    @staticmethod
    def request(arg0: SurfaceView, arg1: Rect, arg2: Bitmap, arg3: "OnPixelCopyFinishedListener", arg4: Handler) -> None: ...
    @overload
    @staticmethod
    def request(arg0: Surface, arg1: Bitmap, arg2: "OnPixelCopyFinishedListener", arg3: Handler) -> None: ...
    @overload
    @staticmethod
    def request(arg0: Surface, arg1: Rect, arg2: Bitmap, arg3: "OnPixelCopyFinishedListener", arg4: Handler) -> None: ...
    @overload
    @staticmethod
    def request(arg0: Window, arg1: Bitmap, arg2: "OnPixelCopyFinishedListener", arg3: Handler) -> None: ...
    @overload
    @staticmethod
    def request(arg0: Window, arg1: Rect, arg2: Bitmap, arg3: "OnPixelCopyFinishedListener", arg4: Handler) -> None: ...
    @overload
    @staticmethod
    def request(arg0: "Request", arg1: Executor, arg2: Consumer) -> None: ...

    class OnPixelCopyFinishedListener:
        def onPixelCopyFinished(self, arg0: int) -> None: ...

    class Request:
        def getDestinationBitmap(self) -> Bitmap: ...
        def getSourceRect(self) -> Rect: ...

        class Builder:
            @overload
            @staticmethod
            def ofWindow(arg0: Window) -> "Builder": ...
            @overload
            @staticmethod
            def ofWindow(arg0: View) -> "Builder": ...
            @overload
            @staticmethod
            def ofSurface(arg0: Surface) -> "Builder": ...
            @overload
            @staticmethod
            def ofSurface(arg0: SurfaceView) -> "Builder": ...
            def setSourceRect(self, arg0: Rect) -> "Builder": ...
            def setDestinationBitmap(self, arg0: Bitmap) -> "Builder": ...
            def build(self) -> "Request": ...

    class Result:
        def getStatus(self) -> int: ...
        def getBitmap(self) -> Bitmap: ...
