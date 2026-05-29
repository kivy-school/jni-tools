from typing import Any, ClassVar, overload

class AudioCodec:
    AMR: ClassVar["AudioCodec"]
    GSM: ClassVar["AudioCodec"]
    GSM_EFR: ClassVar["AudioCodec"]
    PCMA: ClassVar["AudioCodec"]
    PCMU: ClassVar["AudioCodec"]
    fmtp: str
    rtpmap: str
    type: int
    @staticmethod
    def getCodecs() -> Any: ...
    @staticmethod
    def getCodec(p0: int, p1: str, p2: str) -> "AudioCodec": ...
