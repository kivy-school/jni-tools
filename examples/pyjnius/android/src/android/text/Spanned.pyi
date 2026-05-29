from typing import Any, ClassVar, overload

class Spanned:
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
    def getSpanEnd(self, p0: Any) -> int: ...
    def getSpanFlags(self, p0: Any) -> int: ...
    def getSpanStart(self, p0: Any) -> int: ...
    def nextSpanTransition(self, p0: int, p1: int, p2: type) -> int: ...
    def getSpans(self, p0: int, p1: int, p2: type) -> Any: ...
