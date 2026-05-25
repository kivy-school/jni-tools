from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.os.Parcel import Parcel
from android.util.Printer import Printer
from java.lang.Throwable import Throwable

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

class ApplicationErrorReport:
    CREATOR: ClassVar[Creator]
    TYPE_ANR: ClassVar[int]
    TYPE_BATTERY: ClassVar[int]
    TYPE_CRASH: ClassVar[int]
    TYPE_NONE: ClassVar[int]
    TYPE_RUNNING_SERVICE: ClassVar[int]
    anrInfo: "AnrInfo"
    batteryInfo: "BatteryInfo"
    crashInfo: "CrashInfo"
    installerPackageName: str
    packageName: str
    processName: str
    runningServiceInfo: "RunningServiceInfo"
    systemApp: bool
    time: int
    type: int
    def __init__(self) -> None: ...
    @staticmethod
    def getErrorReportReceiver(arg0: Context, arg1: str, arg2: int) -> ComponentName: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def readFromParcel(self, arg0: Parcel) -> None: ...
    def describeContents(self) -> int: ...
    def dump(self, arg0: Printer, arg1: str) -> None: ...

    class AnrInfo:
        activity: str
        cause: str
        info: str
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Parcel) -> None: ...
        def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
        def dump(self, arg0: Printer, arg1: str) -> None: ...

    class BatteryInfo:
        checkinDetails: str
        durationMicros: int
        usageDetails: str
        usagePercent: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Parcel) -> None: ...
        def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
        def dump(self, arg0: Printer, arg1: str) -> None: ...

    class CrashInfo:
        exceptionClassName: str
        exceptionMessage: str
        stackTrace: str
        throwClassName: str
        throwFileName: str
        throwLineNumber: int
        throwMethodName: str
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Throwable) -> None: ...
        @overload
        def __init__(self, arg0: Parcel) -> None: ...
        def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
        def dump(self, arg0: Printer, arg1: str) -> None: ...

    class RunningServiceInfo:
        durationMillis: int
        serviceDetails: str
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: Parcel) -> None: ...
        def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
        def dump(self, arg0: Printer, arg1: str) -> None: ...
