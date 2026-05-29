from typing import Any, ClassVar, overload
from android.app.jank.RelativeFrameTimeHistogram import RelativeFrameTimeHistogram

class AppJankStats:
    WIDGET_CATEGORY_ANIMATION: ClassVar[str]
    WIDGET_CATEGORY_KEYBOARD: ClassVar[str]
    WIDGET_CATEGORY_MEDIA: ClassVar[str]
    WIDGET_CATEGORY_NAVIGATION: ClassVar[str]
    WIDGET_CATEGORY_OTHER: ClassVar[str]
    WIDGET_CATEGORY_SCROLL: ClassVar[str]
    WIDGET_CATEGORY_UNSPECIFIED: ClassVar[str]
    WIDGET_STATE_ANIMATING: ClassVar[str]
    WIDGET_STATE_DRAGGING: ClassVar[str]
    WIDGET_STATE_FLINGING: ClassVar[str]
    WIDGET_STATE_NONE: ClassVar[str]
    WIDGET_STATE_PLAYBACK: ClassVar[str]
    WIDGET_STATE_PREDICTIVE_BACK: ClassVar[str]
    WIDGET_STATE_SCROLLING: ClassVar[str]
    WIDGET_STATE_SWIPING: ClassVar[str]
    WIDGET_STATE_TAPPING: ClassVar[str]
    WIDGET_STATE_UNSPECIFIED: ClassVar[str]
    WIDGET_STATE_ZOOMING: ClassVar[str]
    def __init__(self, p0: int, p1: str, p2: str, p3: str, p4: str, p5: int, p6: int, p7: RelativeFrameTimeHistogram) -> None: ...
    def getWidgetState(self) -> str: ...
    def getWidgetCategory(self) -> str: ...
    def getTotalFrameCount(self) -> int: ...
    def getWidgetId(self) -> str: ...
    def getRelativeFrameTimeHistogram(self) -> RelativeFrameTimeHistogram: ...
    def getJankyFrameCount(self) -> int: ...
    def getNavigationComponent(self) -> str: ...
    def getUid(self) -> int: ...
