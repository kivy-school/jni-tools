from typing import Any, ClassVar, overload

class ModeAction:
    RESPONSE_CHALLENGE_ACK: ClassVar[int]
    RESPONSE_CHALLENGE_PASSPHRASE: ClassVar[int]
    RESPONSE_CHALLENGE_PIN: ClassVar[int]
    RESPONSE_FAIL: ClassVar[int]
    RESPONSE_OK: ClassVar[int]
    RESPONSE_UNKNOWN: ClassVar[int]
    TYPE_BOOLEAN: ClassVar[int]
    TYPE_COMMAND: ClassVar[int]
    TYPE_ERROR: ClassVar[int]
    TYPE_FLOAT: ClassVar[int]
    TYPE_MODE: ClassVar[int]
    @overload
    def __init__(self, p0: str, p1: int, p2: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: int) -> None: ...
    def getActionType(self) -> int: ...
    def getNewMode(self) -> int: ...
