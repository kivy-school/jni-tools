from typing import Any, ClassVar, overload

class StateSet:
    NOTHING: ClassVar[list[int]]
    WILD_CARD: ClassVar[list[int]]
    @staticmethod
    def isWildCard(arg0: list[int]) -> bool: ...
    @overload
    @staticmethod
    def stateSetMatches(arg0: list[int], arg1: list[int]) -> bool: ...
    @overload
    @staticmethod
    def stateSetMatches(arg0: list[int], arg1: int) -> bool: ...
    @staticmethod
    def trimStateSet(arg0: list[int], arg1: int) -> list[int]: ...
    @staticmethod
    def dump(arg0: list[int]) -> str: ...
