from typing import Any, ClassVar, overload

class Spannable:
    SPAN_COMPOSING: ClassVar[int]
    SPAN_EXCLUSIVE_EXCLUSIVE: ClassVar[int]
    SPAN_EXCLUSIVE_INCLUSIVE: ClassVar[int]
    SPAN_INCLUSIVE_EXCLUSIVE: ClassVar[int]
    SPAN_INCLUSIVE_INCLUSIVE: ClassVar[int]
    SPAN_INTERMEDIATE: ClassVar[int]
    SPAN_MARK_MARK: ClassVar[int]
    SPAN_MARK_POINT: ClassVar[int]
    SPAN_PARAGRAPH: ClassVar[int]
    SPAN_POINT_MARK: ClassVar[int]
    SPAN_POINT_MARK_MASK: ClassVar[int]
    SPAN_POINT_POINT: ClassVar[int]
    SPAN_PRIORITY: ClassVar[int]
    SPAN_PRIORITY_SHIFT: ClassVar[int]
    SPAN_USER: ClassVar[int]
    SPAN_USER_SHIFT: ClassVar[int]
    def removeSpan(self, p0: Any) -> None: ...
    def setSpan(self, p0: Any, p1: int, p2: int, p3: int) -> None: ...

    class Factory:
        def __init__(self) -> None: ...
        @staticmethod
        def getInstance() -> Any: ...
        def newSpannable(self, p0: str) -> "Spannable": ...
