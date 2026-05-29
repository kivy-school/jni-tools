from typing import Any, ClassVar, overload
from android.content.pm.ApplicationInfo import ApplicationInfo
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from android.util.Printer import Printer

class ActivityInfo:
    COLOR_MODE_DEFAULT: ClassVar[int]
    COLOR_MODE_HDR: ClassVar[int]
    COLOR_MODE_WIDE_COLOR_GAMUT: ClassVar[int]
    CONFIG_ASSETS_PATHS: ClassVar[int]
    CONFIG_COLOR_MODE: ClassVar[int]
    CONFIG_DENSITY: ClassVar[int]
    CONFIG_FONT_SCALE: ClassVar[int]
    CONFIG_FONT_WEIGHT_ADJUSTMENT: ClassVar[int]
    CONFIG_GRAMMATICAL_GENDER: ClassVar[int]
    CONFIG_KEYBOARD: ClassVar[int]
    CONFIG_KEYBOARD_HIDDEN: ClassVar[int]
    CONFIG_LAYOUT_DIRECTION: ClassVar[int]
    CONFIG_LOCALE: ClassVar[int]
    CONFIG_MCC: ClassVar[int]
    CONFIG_MNC: ClassVar[int]
    CONFIG_NAVIGATION: ClassVar[int]
    CONFIG_ORIENTATION: ClassVar[int]
    CONFIG_RESOURCES_UNUSED: ClassVar[int]
    CONFIG_SCREEN_LAYOUT: ClassVar[int]
    CONFIG_SCREEN_SIZE: ClassVar[int]
    CONFIG_SMALLEST_SCREEN_SIZE: ClassVar[int]
    CONFIG_TOUCHSCREEN: ClassVar[int]
    CONFIG_UI_MODE: ClassVar[int]
    CREATOR: ClassVar[Any]
    DOCUMENT_LAUNCH_ALWAYS: ClassVar[int]
    DOCUMENT_LAUNCH_INTO_EXISTING: ClassVar[int]
    DOCUMENT_LAUNCH_NEVER: ClassVar[int]
    DOCUMENT_LAUNCH_NONE: ClassVar[int]
    FLAG_ALLOW_TASK_REPARENTING: ClassVar[int]
    FLAG_ALLOW_UNTRUSTED_ACTIVITY_EMBEDDING: ClassVar[int]
    FLAG_ALWAYS_RETAIN_TASK_STATE: ClassVar[int]
    FLAG_AUTO_REMOVE_FROM_RECENTS: ClassVar[int]
    FLAG_CLEAR_TASK_ON_LAUNCH: ClassVar[int]
    FLAG_ENABLE_VR_MODE: ClassVar[int]
    FLAG_EXCLUDE_FROM_RECENTS: ClassVar[int]
    FLAG_FINISH_ON_CLOSE_SYSTEM_DIALOGS: ClassVar[int]
    FLAG_FINISH_ON_TASK_LAUNCH: ClassVar[int]
    FLAG_HARDWARE_ACCELERATED: ClassVar[int]
    FLAG_IMMERSIVE: ClassVar[int]
    FLAG_MULTIPROCESS: ClassVar[int]
    FLAG_NO_HISTORY: ClassVar[int]
    FLAG_PREFER_MINIMAL_POST_PROCESSING: ClassVar[int]
    FLAG_RELINQUISH_TASK_IDENTITY: ClassVar[int]
    FLAG_RESUME_WHILE_PAUSING: ClassVar[int]
    FLAG_SINGLE_USER: ClassVar[int]
    FLAG_STATE_NOT_NEEDED: ClassVar[int]
    LAUNCH_MULTIPLE: ClassVar[int]
    LAUNCH_SINGLE_INSTANCE: ClassVar[int]
    LAUNCH_SINGLE_INSTANCE_PER_TASK: ClassVar[int]
    LAUNCH_SINGLE_TASK: ClassVar[int]
    LAUNCH_SINGLE_TOP: ClassVar[int]
    PERSIST_ACROSS_REBOOTS: ClassVar[int]
    PERSIST_NEVER: ClassVar[int]
    PERSIST_ROOT_ONLY: ClassVar[int]
    SCREEN_ORIENTATION_BEHIND: ClassVar[int]
    SCREEN_ORIENTATION_FULL_SENSOR: ClassVar[int]
    SCREEN_ORIENTATION_FULL_USER: ClassVar[int]
    SCREEN_ORIENTATION_LANDSCAPE: ClassVar[int]
    SCREEN_ORIENTATION_LOCKED: ClassVar[int]
    SCREEN_ORIENTATION_NOSENSOR: ClassVar[int]
    SCREEN_ORIENTATION_PORTRAIT: ClassVar[int]
    SCREEN_ORIENTATION_REVERSE_LANDSCAPE: ClassVar[int]
    SCREEN_ORIENTATION_REVERSE_PORTRAIT: ClassVar[int]
    SCREEN_ORIENTATION_SENSOR: ClassVar[int]
    SCREEN_ORIENTATION_SENSOR_LANDSCAPE: ClassVar[int]
    SCREEN_ORIENTATION_SENSOR_PORTRAIT: ClassVar[int]
    SCREEN_ORIENTATION_UNSPECIFIED: ClassVar[int]
    SCREEN_ORIENTATION_USER: ClassVar[int]
    SCREEN_ORIENTATION_USER_LANDSCAPE: ClassVar[int]
    SCREEN_ORIENTATION_USER_PORTRAIT: ClassVar[int]
    UIOPTION_SPLIT_ACTION_BAR_WHEN_NARROW: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    colorMode: int
    configChanges: int
    documentLaunchMode: int
    flags: int
    launchMode: int
    maxRecents: int
    parentActivityName: str
    permission: str
    persistableMode: int
    requiredDisplayCategory: str
    screenOrientation: int
    softInputMode: int
    targetActivity: str
    taskAffinity: str
    theme: int
    uiOptions: int
    windowLayout: Any
    applicationInfo: ApplicationInfo
    attributionTags: Any
    descriptionRes: int
    directBootAware: bool
    enabled: bool
    exported: bool
    processName: str
    splitName: str
    banner: int
    icon: int
    isArchived: bool
    labelRes: int
    logo: int
    metaData: Bundle
    name: str
    nonLocalizedLabel: str
    packageName: str
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: "ActivityInfo") -> None: ...
    def toString(self) -> str: ...
    def dump(self, p0: Printer, p1: str) -> None: ...
    def getKnownActivityEmbeddingCerts(self) -> set: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
    def getThemeResource(self) -> int: ...

    class WindowLayout:
        gravity: int
        height: int
        heightFraction: float
        minHeight: int
        minWidth: int
        width: int
        widthFraction: float
        def __init__(self, p0: int, p1: float, p2: int, p3: float, p4: int, p5: int, p6: int) -> None: ...
