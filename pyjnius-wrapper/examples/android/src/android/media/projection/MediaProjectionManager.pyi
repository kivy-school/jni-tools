from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.media.projection.MediaProjection import MediaProjection
from android.media.projection.MediaProjectionConfig import MediaProjectionConfig

class MediaProjectionManager:
    @overload
    def createScreenCaptureIntent(self) -> Intent: ...
    @overload
    def createScreenCaptureIntent(self, arg0: MediaProjectionConfig) -> Intent: ...
    def getMediaProjection(self, arg0: int, arg1: Intent) -> MediaProjection: ...
