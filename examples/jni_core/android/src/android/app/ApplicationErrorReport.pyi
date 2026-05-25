from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.os.Parcel import Parcel
from android.util.Printer import Printer
from java.lang.Throwable import Throwable

class ApplicationErrorReport:
    CREATOR: ClassVar[Any]
    TYPE_ANR: ClassVar[int]
    TYPE_BATTERY: ClassVar[int]
    TYPE_CRASH: ClassVar[int]
    TYPE_NONE: ClassVar[int]
    TYPE_RUNNING_SERVICE: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    anrInfo: Any
    batteryInfo: Any
    crashInfo: Any
    installerPackageName: str
    packageName: str
    processName: str
    runningServiceInfo: Any
    systemApp: bool
    time: int
    type: int
    def __init__(self) -> None: ...
    @staticmethod
    def getErrorReportReceiver(p0: Context, p1: str, p2: int) -> ComponentName: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def readFromParcel(self, p0: Parcel) -> None: ...
    def dump(self, p0: Printer, p1: str) -> None: ...

    class RunningServiceInfo:
        durationMillis: int
        serviceDetails: str
        @overload
        def __init__(self, p0: Parcel) -> None: ...
        @overload
        def __init__(self) -> None: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
        def dump(self, p0: Printer, p1: str) -> None: ...

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
        def __init__(self, p0: Parcel) -> None: ...
        @overload
        def __init__(self, p0: Throwable) -> None: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
        def dump(self, p0: Printer, p1: str) -> None: ...

    class BatteryInfo:
        checkinDetails: str
        durationMicros: int
        usageDetails: str
        usagePercent: int
        @overload
        def __init__(self, p0: Parcel) -> None: ...
        @overload
        def __init__(self) -> None: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
        def dump(self, p0: Printer, p1: str) -> None: ...

    class AnrInfo:
        activity: str
        cause: str
        info: str
        @overload
        def __init__(self, p0: Parcel) -> None: ...
        @overload
        def __init__(self) -> None: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
        def dump(self, p0: Printer, p1: str) -> None: ...
