from typing import Any, ClassVar, overload
from android.view.ContentInfo import ContentInfo
from android.view.View import View

class OnReceiveContentListener:
    def onReceiveContent(self, p0: View, p1: ContentInfo) -> ContentInfo: ...
