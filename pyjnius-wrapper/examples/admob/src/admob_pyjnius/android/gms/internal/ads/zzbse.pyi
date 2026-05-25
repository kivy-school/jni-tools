from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class State:
    """Forward declaration for ``com.google.android.gms.ads.initialization.AdapterStatus.State``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.ads.initialization.AdapterStatus.State')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/ads/initialization/AdapterStatus/State
    """
    ...

class zzbse:
    def __init__(self, arg0: State, arg1: str, arg2: int) -> None: ...
    def getInitializationState(self) -> State: ...
    def getDescription(self) -> str: ...
    def getLatency(self) -> int: ...
