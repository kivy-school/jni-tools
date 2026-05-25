from typing import Any, ClassVar, overload
from OneSignalAPIClient import OneSignalAPIClient
from OneSignalApiResponseHandler import OneSignalApiResponseHandler

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

class OSOutcomeEventsV1Service:
    def __init__(self, arg0: OneSignalAPIClient) -> None: ...
    def sendOutcomeEvent(self, arg0: JSONObject, arg1: OneSignalApiResponseHandler) -> None: ...
