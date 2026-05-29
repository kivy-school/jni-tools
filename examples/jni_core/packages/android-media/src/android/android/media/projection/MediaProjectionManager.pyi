from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.media.projection.MediaProjection import MediaProjection
from android.media.projection.MediaProjectionConfig import MediaProjectionConfig

class MediaProjectionManager:
    def getMediaProjection(self, p0: int, p1: Intent) -> MediaProjection: ...
    @overload
    def createScreenCaptureIntent(self) -> Intent: ...
    @overload
    def createScreenCaptureIntent(self, p0: MediaProjectionConfig) -> Intent: ...
