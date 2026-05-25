from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.pm.PackageManager import PackageManager
from android.os.Parcel import Parcel
from android.util.Printer import Printer
from java.util.UUID import UUID

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

class ApplicationInfo:
    CATEGORY_ACCESSIBILITY: ClassVar[int]
    CATEGORY_AUDIO: ClassVar[int]
    CATEGORY_GAME: ClassVar[int]
    CATEGORY_IMAGE: ClassVar[int]
    CATEGORY_MAPS: ClassVar[int]
    CATEGORY_NEWS: ClassVar[int]
    CATEGORY_PRODUCTIVITY: ClassVar[int]
    CATEGORY_SOCIAL: ClassVar[int]
    CATEGORY_UNDEFINED: ClassVar[int]
    CATEGORY_VIDEO: ClassVar[int]
    CREATOR: ClassVar[Creator]
    FLAG_ALLOW_BACKUP: ClassVar[int]
    FLAG_ALLOW_CLEAR_USER_DATA: ClassVar[int]
    FLAG_ALLOW_TASK_REPARENTING: ClassVar[int]
    FLAG_DEBUGGABLE: ClassVar[int]
    FLAG_EXTERNAL_STORAGE: ClassVar[int]
    FLAG_EXTRACT_NATIVE_LIBS: ClassVar[int]
    FLAG_FACTORY_TEST: ClassVar[int]
    FLAG_FULL_BACKUP_ONLY: ClassVar[int]
    FLAG_HARDWARE_ACCELERATED: ClassVar[int]
    FLAG_HAS_CODE: ClassVar[int]
    FLAG_INSTALLED: ClassVar[int]
    FLAG_IS_DATA_ONLY: ClassVar[int]
    FLAG_IS_GAME: ClassVar[int]
    FLAG_KILL_AFTER_RESTORE: ClassVar[int]
    FLAG_LARGE_HEAP: ClassVar[int]
    FLAG_MULTIARCH: ClassVar[int]
    FLAG_PERSISTENT: ClassVar[int]
    FLAG_RESIZEABLE_FOR_SCREENS: ClassVar[int]
    FLAG_RESTORE_ANY_VERSION: ClassVar[int]
    FLAG_STOPPED: ClassVar[int]
    FLAG_SUPPORTS_LARGE_SCREENS: ClassVar[int]
    FLAG_SUPPORTS_NORMAL_SCREENS: ClassVar[int]
    FLAG_SUPPORTS_RTL: ClassVar[int]
    FLAG_SUPPORTS_SCREEN_DENSITIES: ClassVar[int]
    FLAG_SUPPORTS_SMALL_SCREENS: ClassVar[int]
    FLAG_SUPPORTS_XLARGE_SCREENS: ClassVar[int]
    FLAG_SUSPENDED: ClassVar[int]
    FLAG_SYSTEM: ClassVar[int]
    FLAG_TEST_ONLY: ClassVar[int]
    FLAG_UPDATED_SYSTEM_APP: ClassVar[int]
    FLAG_USES_CLEARTEXT_TRAFFIC: ClassVar[int]
    FLAG_VM_SAFE_MODE: ClassVar[int]
    GWP_ASAN_ALWAYS: ClassVar[int]
    GWP_ASAN_DEFAULT: ClassVar[int]
    GWP_ASAN_NEVER: ClassVar[int]
    MEMTAG_ASYNC: ClassVar[int]
    MEMTAG_DEFAULT: ClassVar[int]
    MEMTAG_OFF: ClassVar[int]
    MEMTAG_SYNC: ClassVar[int]
    RAW_EXTERNAL_STORAGE_ACCESS_DEFAULT: ClassVar[int]
    RAW_EXTERNAL_STORAGE_ACCESS_NOT_REQUESTED: ClassVar[int]
    RAW_EXTERNAL_STORAGE_ACCESS_REQUESTED: ClassVar[int]
    ZEROINIT_DEFAULT: ClassVar[int]
    ZEROINIT_DISABLED: ClassVar[int]
    ZEROINIT_ENABLED: ClassVar[int]
    appComponentFactory: str
    backupAgentName: str
    category: int
    className: str
    compatibleWidthLimitDp: int
    compileSdkVersion: int
    compileSdkVersionCodename: str
    dataDir: str
    descriptionRes: int
    deviceProtectedDataDir: str
    enabled: bool
    flags: int
    largestWidthLimitDp: int
    manageSpaceActivityName: str
    minSdkVersion: int
    nativeLibraryDir: str
    permission: str
    processName: str
    publicSourceDir: str
    requiresSmallestWidthDp: int
    sharedLibraryFiles: list[str]
    sourceDir: str
    splitNames: list[str]
    splitPublicSourceDirs: list[str]
    splitSourceDirs: list[str]
    storageUuid: UUID
    targetSdkVersion: int
    taskAffinity: str
    theme: int
    uiOptions: int
    uid: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: "ApplicationInfo") -> None: ...
    @staticmethod
    def getCategoryTitle(arg0: Context, arg1: int) -> str: ...
    def dump(self, arg0: Printer, arg1: str) -> None: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def loadDescription(self, arg0: PackageManager) -> str: ...
    def getRequestRawExternalStorageAccess(self) -> int: ...
    def isVirtualPreload(self) -> bool: ...
    def isProfileableByShell(self) -> bool: ...
    def isProfileable(self) -> bool: ...
    def areAttributionsUserVisible(self) -> bool: ...
    def isResourceOverlay(self) -> bool: ...
    def getGwpAsanMode(self) -> int: ...
    def getMemtagMode(self) -> int: ...
    def getNativeHeapZeroInitialized(self) -> int: ...
    def getKnownActivityEmbeddingCerts(self) -> set: ...

    class DisplayNameComparator:
        def __init__(self, arg0: PackageManager) -> None: ...
        def compare(self, arg0: "ApplicationInfo", arg1: "ApplicationInfo") -> int: ...
