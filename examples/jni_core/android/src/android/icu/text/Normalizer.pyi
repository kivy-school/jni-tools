from typing import Any, ClassVar, overload

class Normalizer:
    COMPARE_CODE_POINT_ORDER: ClassVar[int]
    COMPARE_IGNORE_CASE: ClassVar[int]
    FOLD_CASE_DEFAULT: ClassVar[int]
    FOLD_CASE_EXCLUDE_SPECIAL_I: ClassVar[int]
    INPUT_IS_FCD: ClassVar[int]
    MAYBE: ClassVar[Any]
    NO: ClassVar[Any]
    YES: ClassVar[Any]
    def clone(self) -> Any: ...
    @overload
    @staticmethod
    def compare(p0: int, p1: int, p2: int) -> int: ...
    @overload
    @staticmethod
    def compare(p0: Any, p1: Any, p2: int) -> int: ...
    @overload
    @staticmethod
    def compare(p0: int, p1: str, p2: int) -> int: ...
    @overload
    @staticmethod
    def compare(p0: str, p1: str, p2: int) -> int: ...
    @overload
    @staticmethod
    def compare(p0: Any, p1: int, p2: int, p3: Any, p4: int, p5: int, p6: int) -> int: ...

    class QuickCheckResult:
        ...
