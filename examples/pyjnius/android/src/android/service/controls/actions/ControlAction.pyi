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
    def isValidResponse(p0: int) -> bool: ...
    @staticmethod
    def getErrorAction() -> "ControlAction": ...
