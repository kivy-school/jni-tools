from typing import Any, ClassVar, overload

class MediaFeature:
    def __init__(self) -> None: ...

    class HdrType:
        DOLBY_VISION: ClassVar[str]
        HDR10: ClassVar[str]
        HDR10_PLUS: ClassVar[str]
        HLG: ClassVar[str]
