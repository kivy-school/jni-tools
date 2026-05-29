from typing import Any, ClassVar, overload

class RangeValueIterator:
    def reset(self) -> None: ...
    def next(self, p0: Any) -> bool: ...

    class Element:
        limit: int
        start: int
        value: int
        def __init__(self) -> None: ...
