from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OSNotificationAction:
    def __init__(self, arg0: "ActionType", arg1: str) -> None: ...
    def getType(self) -> "ActionType": ...
    def getActionId(self) -> str: ...
    def toJSONObject(self) -> JSONObject: ...

    class ActionType:
        Opened: ClassVar["ActionType"]
        ActionTaken: ClassVar["ActionType"]
        @staticmethod
        def values() -> list["ActionType"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "ActionType": ...
