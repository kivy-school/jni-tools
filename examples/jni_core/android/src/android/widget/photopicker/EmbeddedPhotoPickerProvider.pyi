from typing import Any, ClassVar, overload
from android.os.IBinder import IBinder
from android.widget.photopicker.EmbeddedPhotoPickerClient import EmbeddedPhotoPickerClient
from android.widget.photopicker.EmbeddedPhotoPickerFeatureInfo import EmbeddedPhotoPickerFeatureInfo
from java.util.concurrent.Executor import Executor

class EmbeddedPhotoPickerProvider:
    def openSession(self, p0: IBinder, p1: int, p2: int, p3: int, p4: EmbeddedPhotoPickerFeatureInfo, p5: Executor, p6: EmbeddedPhotoPickerClient) -> None: ...
