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

from typing import Any, ClassVar, overload

class ControlAction:
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
    def getTemplateId(self) -> str: ...
    def getActionType(self) -> int: ...
    def getChallengeValue(self) -> str: ...
    @staticmethod
    def getErrorAction() -> "ControlAction": ...
    @staticmethod
    def isValidResponse(p0: int) -> bool: ...

from typing import Any, ClassVar, overload

class BooleanAction:
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
    def __init__(self, p0: str, p1: bool, p2: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: bool) -> None: ...
    def getActionType(self) -> int: ...
    def getNewState(self) -> bool: ...

from typing import Any, ClassVar, overload

class FloatAction:
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
    def __init__(self, p0: str, p1: float, p2: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: float) -> None: ...
    def getActionType(self) -> int: ...
    def getNewValue(self) -> float: ...

from typing import Any, ClassVar, overload

class CommandAction:
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
    def __init__(self, p0: str, p1: str) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    def getActionType(self) -> int: ...

