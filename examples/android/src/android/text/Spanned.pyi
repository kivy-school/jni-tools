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
    def getSpans(self, arg0: int, arg1: int, arg2: type) -> list: ...
    def getSpanStart(self, arg0: Any) -> int: ...
    def getSpanEnd(self, arg0: Any) -> int: ...
    def getSpanFlags(self, arg0: Any) -> int: ...
    def nextSpanTransition(self, arg0: int, arg1: int, arg2: type) -> int: ...
