from typing import Any, ClassVar, overload

class MicrophoneDirection:
    MIC_DIRECTION_AWAY_FROM_USER: ClassVar[int]
    MIC_DIRECTION_EXTERNAL: ClassVar[int]
    MIC_DIRECTION_TOWARDS_USER: ClassVar[int]
    MIC_DIRECTION_UNSPECIFIED: ClassVar[int]
    def setPreferredMicrophoneDirection(self, p0: int) -> bool: ...
    def setPreferredMicrophoneFieldDimension(self, p0: float) -> bool: ...
