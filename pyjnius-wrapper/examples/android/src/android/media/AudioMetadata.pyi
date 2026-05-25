from typing import Any, ClassVar, overload
from android.media.AudioMetadataMap import AudioMetadataMap

class AudioMetadata:
    @staticmethod
    def createMap() -> AudioMetadataMap: ...

    class Format:
        KEY_ATMOS_PRESENT: ClassVar["Key"]
        KEY_AUDIO_ENCODING: ClassVar["Key"]
        KEY_BIT_RATE: ClassVar["Key"]
        KEY_BIT_WIDTH: ClassVar["Key"]
        KEY_CHANNEL_MASK: ClassVar["Key"]
        KEY_MIME: ClassVar["Key"]
        KEY_PRESENTATION_CONTENT_CLASSIFIER: ClassVar["Key"]
        KEY_PRESENTATION_ID: ClassVar["Key"]
        KEY_PRESENTATION_LANGUAGE: ClassVar["Key"]
        KEY_PROGRAM_ID: ClassVar["Key"]
        KEY_SAMPLE_RATE: ClassVar["Key"]

    class Key:
        def getName(self) -> str: ...
        def getValueClass(self) -> type: ...
