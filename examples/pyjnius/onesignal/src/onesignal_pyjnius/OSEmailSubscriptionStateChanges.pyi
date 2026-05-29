from typing import Any, ClassVar, overload
from OSEmailSubscriptionState import OSEmailSubscriptionState

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

class OSEmailSubscriptionStateChanges:
    def __init__(self, arg0: OSEmailSubscriptionState, arg1: OSEmailSubscriptionState) -> None: ...
    def getTo(self) -> OSEmailSubscriptionState: ...
    def getFrom(self) -> OSEmailSubscriptionState: ...
    def toJSONObject(self) -> JSONObject: ...
    def toString(self) -> str: ...
