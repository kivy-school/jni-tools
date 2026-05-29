from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.widget.photopicker.EmbeddedPhotoPickerProvider import EmbeddedPhotoPickerProvider

class EmbeddedPhotoPickerProviderFactory:
    @staticmethod
    def create(p0: Context) -> EmbeddedPhotoPickerProvider: ...
