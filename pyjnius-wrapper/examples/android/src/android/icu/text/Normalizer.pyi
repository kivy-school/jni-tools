from typing import Any, ClassVar, overload

class Normalizer:
    COMPARE_CODE_POINT_ORDER: ClassVar[int]
    COMPARE_IGNORE_CASE: ClassVar[int]
    FOLD_CASE_DEFAULT: ClassVar[int]
    FOLD_CASE_EXCLUDE_SPECIAL_I: ClassVar[int]
    INPUT_IS_FCD: ClassVar[int]
    MAYBE: ClassVar["QuickCheckResult"]
    NO: ClassVar["QuickCheckResult"]
    YES: ClassVar["QuickCheckResult"]
    def clone(self) -> Any: ...
    @overload
    @staticmethod
    def compare(arg0: list[str], arg1: int, arg2: int, arg3: list[str], arg4: int, arg5: int, arg6: int) -> int: ...
    @overload
    @staticmethod
    def compare(arg0: str, arg1: str, arg2: int) -> int: ...
    @overload
    @staticmethod
    def compare(arg0: list[str], arg1: list[str], arg2: int) -> int: ...
    @overload
    @staticmethod
    def compare(arg0: int, arg1: int, arg2: int) -> int: ...
    @overload
    @staticmethod
    def compare(arg0: int, arg1: str, arg2: int) -> int: ...

    class QuickCheckResult:
        ...
