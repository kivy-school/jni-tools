from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from java.util.concurrent.Executor import Executor

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
class OnClickListener:
    """Forward declaration for ``android.content.DialogInterface.OnClickListener``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.DialogInterface.OnClickListener')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/DialogInterface/OnClickListener
    """
    ...

class PromptContentViewWithMoreOptionsButton:
    CREATOR: ClassVar[Creator]
    def getDescription(self) -> str: ...
    def getMoreOptionsButtonListener(self) -> OnClickListener: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def setDescription(self, arg0: str) -> "Builder": ...
        def setMoreOptionsButtonListener(self, arg0: Executor, arg1: OnClickListener) -> "Builder": ...
        def build(self) -> "PromptContentViewWithMoreOptionsButton": ...
