from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.content.pm.ActivityInfo import ActivityInfo
from android.content.pm.PackageManager import PackageManager
from android.graphics.drawable.Drawable import Drawable
from android.os.Parcel import Parcel
from android.os.UserHandle import UserHandle

class AppWidgetProviderInfo:
    CREATOR: ClassVar[Any]
    RESIZE_BOTH: ClassVar[int]
    RESIZE_HORIZONTAL: ClassVar[int]
    RESIZE_NONE: ClassVar[int]
    RESIZE_VERTICAL: ClassVar[int]
    WIDGET_CATEGORY_HOME_SCREEN: ClassVar[int]
    WIDGET_CATEGORY_KEYGUARD: ClassVar[int]
    WIDGET_CATEGORY_SEARCHBOX: ClassVar[int]
    WIDGET_FEATURE_CONFIGURATION_OPTIONAL: ClassVar[int]
    WIDGET_FEATURE_HIDE_FROM_PICKER: ClassVar[int]
    WIDGET_FEATURE_RECONFIGURABLE: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    autoAdvanceViewId: int
    configure: ComponentName
    descriptionRes: int
    generatedPreviewCategories: int
    icon: int
    initialKeyguardLayout: int
    initialLayout: int
    label: str
    maxResizeHeight: int
    maxResizeWidth: int
    minHeight: int
    minResizeHeight: int
    minResizeWidth: int
    minWidth: int
    previewImage: int
    previewLayout: int
    provider: ComponentName
    resizeMode: int
    targetCellHeight: int
    targetCellWidth: int
    updatePeriodMillis: int
    widgetCategory: int
    widgetFeatures: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: Parcel) -> None: ...
    def toString(self) -> str: ...
    @overload
    def clone(self) -> "AppWidgetProviderInfo": ...
    @overload
    def clone(self) -> Any: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def loadLabel(self, p0: PackageManager) -> str: ...
    def loadIcon(self, p0: Context, p1: int) -> Drawable: ...
    def getActivityInfo(self) -> ActivityInfo: ...
    def loadPreviewImage(self, p0: Context, p1: int) -> Drawable: ...
    def getProfile(self) -> UserHandle: ...
    def loadDescription(self, p0: Context) -> str: ...
