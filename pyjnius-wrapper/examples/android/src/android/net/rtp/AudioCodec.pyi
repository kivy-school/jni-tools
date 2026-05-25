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
    def getCodecs() -> list["AudioCodec"]: ...
    @staticmethod
    def getCodec(arg0: int, arg1: str, arg2: str) -> "AudioCodec": ...
