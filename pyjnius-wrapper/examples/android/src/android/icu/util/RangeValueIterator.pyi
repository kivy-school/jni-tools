from typing import Any, ClassVar, overload

class RangeValueIterator:
    def next(self, arg0: "Element") -> bool: ...
    def reset(self) -> None: ...

    class Element:
        limit: int
        start: int
        value: int
        def __init__(self) -> None: ...
