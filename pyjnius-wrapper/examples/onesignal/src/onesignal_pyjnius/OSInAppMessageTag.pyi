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
class JSONArray:
    """Forward declaration for ``org.json.JSONArray``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONArray')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OSInAppMessageTag:
    def toJSONObject(self) -> JSONObject: ...
    def getTagsToAdd(self) -> JSONObject: ...
    def setTagsToAdd(self, arg0: JSONObject) -> None: ...
    def getTagsToRemove(self) -> JSONArray: ...
    def setTagsToRemove(self, arg0: JSONArray) -> None: ...
    def toString(self) -> str: ...
