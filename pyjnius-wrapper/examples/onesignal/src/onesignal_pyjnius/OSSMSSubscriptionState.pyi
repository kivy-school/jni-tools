from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class OSObservable:
    """Forward declaration for ``com.onesignal.OSObservable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.OSObservable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OSSMSSubscriptionState:
    def getSmsUserId(self) -> str: ...
    def getSMSNumber(self) -> str: ...
    def isSubscribed(self) -> bool: ...
    def getObservable(self) -> OSObservable: ...
    def clone(self) -> Any: ...
    def toJSONObject(self) -> JSONObject: ...
    def toString(self) -> str: ...
