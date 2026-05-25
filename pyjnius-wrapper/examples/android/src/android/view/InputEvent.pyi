from typing import Any, ClassVar, overload
from android.view.InputDevice import InputDevice

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...

class InputEvent:
    CREATOR: ClassVar[Creator]
    def getDeviceId(self) -> int: ...
    def getDevice(self) -> InputDevice: ...
    def getSource(self) -> int: ...
    def isFromSource(self, arg0: int) -> bool: ...
    def getEventTime(self) -> int: ...
    def describeContents(self) -> int: ...
