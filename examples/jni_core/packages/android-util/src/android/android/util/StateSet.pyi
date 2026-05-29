from typing import Any, ClassVar, overload

class StateSet:
    NOTHING: ClassVar[Any]
    WILD_CARD: ClassVar[Any]
    @staticmethod
    def isWildCard(p0: Any) -> bool: ...
    @overload
    @staticmethod
    def stateSetMatches(p0: Any, p1: Any) -> bool: ...
    @overload
    @staticmethod
    def stateSetMatches(p0: Any, p1: int) -> bool: ...
    @staticmethod
    def trimStateSet(p0: Any, p1: int) -> Any: ...
    @staticmethod
    def dump(p0: Any) -> str: ...
