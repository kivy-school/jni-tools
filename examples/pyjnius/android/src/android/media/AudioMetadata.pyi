from typing import Any, ClassVar, overload
from android.media.AudioMetadataMap import AudioMetadataMap

class AudioMetadata:
    @staticmethod
    def createMap() -> AudioMetadataMap: ...

    class Key:
        def getValueClass(self) -> type: ...
        def getName(self) -> str: ...

    class Format:
        KEY_ATMOS_PRESENT: ClassVar[Any]
        KEY_AUDIO_ENCODING: ClassVar[Any]
        KEY_BIT_RATE: ClassVar[Any]
        KEY_BIT_WIDTH: ClassVar[Any]
        KEY_CHANNEL_MASK: ClassVar[Any]
        KEY_MIME: ClassVar[Any]
        KEY_PRESENTATION_CONTENT_CLASSIFIER: ClassVar[Any]
        KEY_PRESENTATION_ID: ClassVar[Any]
        KEY_PRESENTATION_LANGUAGE: ClassVar[Any]
        KEY_PROGRAM_ID: ClassVar[Any]
        KEY_SAMPLE_RATE: ClassVar[Any]
