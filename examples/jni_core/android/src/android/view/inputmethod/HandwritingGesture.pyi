from typing import Any, ClassVar, overload

class HandwritingGesture:
    GRANULARITY_CHARACTER: ClassVar[int]
    GRANULARITY_WORD: ClassVar[int]
    def getFallbackText(self) -> str: ...
