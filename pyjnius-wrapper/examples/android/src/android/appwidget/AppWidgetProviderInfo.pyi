from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.content.pm.ActivityInfo import ActivityInfo
from android.content.pm.PackageManager import PackageManager
from android.graphics.drawable.Drawable import Drawable
from android.os.Parcel import Parcel
from android.os.UserHandle import UserHandle

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

class AppWidgetProviderInfo:
    CREATOR: ClassVar[Creator]
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
    def __init__(self, arg0: Parcel) -> None: ...
    def loadLabel(self, arg0: PackageManager) -> str: ...
    def loadIcon(self, arg0: Context, arg1: int) -> Drawable: ...
    def loadPreviewImage(self, arg0: Context, arg1: int) -> Drawable: ...
    def loadDescription(self, arg0: Context) -> str: ...
    def getProfile(self) -> UserHandle: ...
    def getActivityInfo(self) -> ActivityInfo: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def clone(self) -> "AppWidgetProviderInfo": ...
    def describeContents(self) -> int: ...
    def toString(self) -> str: ...
