from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from android.appwidget.AppWidgetHostView import AppWidgetHostView
from android.appwidget.AppWidgetProviderInfo import AppWidgetProviderInfo
from android.content.Context import Context
from android.os.Bundle import Bundle

class AppWidgetHost:
    def __init__(self, p0: Context, p1: int) -> None: ...
    def createView(self, p0: Context, p1: int, p2: AppWidgetProviderInfo) -> AppWidgetHostView: ...
    def allocateAppWidgetId(self) -> int: ...
    @staticmethod
    def deleteAllHosts() -> None: ...
    def deleteAppWidgetId(self, p0: int) -> None: ...
    def deleteHost(self) -> None: ...
    def getAppWidgetIds(self) -> Any: ...
    def onAppWidgetRemoved(self, p0: int) -> None: ...
    def startAppWidgetConfigureActivityForResult(self, p0: Activity, p1: int, p2: int, p3: int, p4: Bundle) -> None: ...
    def startListening(self) -> None: ...
    def stopListening(self) -> None: ...

from typing import Any, ClassVar, overload
from android.appwidget.AppWidgetProviderInfo import AppWidgetProviderInfo
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.graphics.Rect import Rect
from android.os.Bundle import Bundle
from android.util.AttributeSet import AttributeSet
from android.util.Property import Property
from android.util.SparseIntArray import SparseIntArray
from android.widget.RemoteViews import RemoteViews
from java.util.concurrent.Executor import Executor

class AppWidgetHostView:
    FOCUS_AFTER_DESCENDANTS: ClassVar[int]
    FOCUS_BEFORE_DESCENDANTS: ClassVar[int]
    FOCUS_BLOCK_DESCENDANTS: ClassVar[int]
    LAYOUT_MODE_CLIP_BOUNDS: ClassVar[int]
    LAYOUT_MODE_OPTICAL_BOUNDS: ClassVar[int]
    PERSISTENT_ALL_CACHES: ClassVar[int]
    PERSISTENT_ANIMATION_CACHE: ClassVar[int]
    PERSISTENT_NO_CACHE: ClassVar[int]
    PERSISTENT_SCROLLING_CACHE: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_AUTO: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_NO: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_YES: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_ASSERTIVE: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_NONE: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_POLITE: ClassVar[int]
    ALPHA: ClassVar[Property]
    AUTOFILL_FLAG_INCLUDE_NOT_IMPORTANT_VIEWS: ClassVar[int]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DATE: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DAY: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_MONTH: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_YEAR: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_NUMBER: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_SECURITY_CODE: ClassVar[str]
    AUTOFILL_HINT_EMAIL_ADDRESS: ClassVar[str]
    AUTOFILL_HINT_NAME: ClassVar[str]
    AUTOFILL_HINT_PASSWORD: ClassVar[str]
    AUTOFILL_HINT_PHONE: ClassVar[str]
    AUTOFILL_HINT_POSTAL_ADDRESS: ClassVar[str]
    AUTOFILL_HINT_POSTAL_CODE: ClassVar[str]
    AUTOFILL_HINT_USERNAME: ClassVar[str]
    AUTOFILL_TYPE_DATE: ClassVar[int]
    AUTOFILL_TYPE_LIST: ClassVar[int]
    AUTOFILL_TYPE_NONE: ClassVar[int]
    AUTOFILL_TYPE_TEXT: ClassVar[int]
    AUTOFILL_TYPE_TOGGLE: ClassVar[int]
    CONTENT_SENSITIVITY_AUTO: ClassVar[int]
    CONTENT_SENSITIVITY_NOT_SENSITIVE: ClassVar[int]
    CONTENT_SENSITIVITY_SENSITIVE: ClassVar[int]
    DRAG_FLAG_ACCESSIBILITY_ACTION: ClassVar[int]
    DRAG_FLAG_GLOBAL: ClassVar[int]
    DRAG_FLAG_GLOBAL_PERSISTABLE_URI_PERMISSION: ClassVar[int]
    DRAG_FLAG_GLOBAL_PREFIX_URI_PERMISSION: ClassVar[int]
    DRAG_FLAG_GLOBAL_SAME_APPLICATION: ClassVar[int]
    DRAG_FLAG_GLOBAL_URI_READ: ClassVar[int]
    DRAG_FLAG_GLOBAL_URI_WRITE: ClassVar[int]
    DRAG_FLAG_HIDE_CALLING_TASK_ON_DRAG_START: ClassVar[int]
    DRAG_FLAG_OPAQUE: ClassVar[int]
    DRAG_FLAG_START_INTENT_SENDER_ON_UNHANDLED_DRAG: ClassVar[int]
    DRAWING_CACHE_QUALITY_AUTO: ClassVar[int]
    DRAWING_CACHE_QUALITY_HIGH: ClassVar[int]
    DRAWING_CACHE_QUALITY_LOW: ClassVar[int]
    FIND_VIEWS_WITH_CONTENT_DESCRIPTION: ClassVar[int]
    FIND_VIEWS_WITH_TEXT: ClassVar[int]
    FOCUSABLE: ClassVar[int]
    FOCUSABLES_ALL: ClassVar[int]
    FOCUSABLES_TOUCH_MODE: ClassVar[int]
    FOCUSABLE_AUTO: ClassVar[int]
    FOCUS_BACKWARD: ClassVar[int]
    FOCUS_DOWN: ClassVar[int]
    FOCUS_FORWARD: ClassVar[int]
    FOCUS_LEFT: ClassVar[int]
    FOCUS_RIGHT: ClassVar[int]
    FOCUS_UP: ClassVar[int]
    GONE: ClassVar[int]
    HAPTIC_FEEDBACK_ENABLED: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_AUTO: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_NO: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_NO_HIDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_YES: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_AUTO: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_NO: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_NO_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_YES: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_YES_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_AUTO: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_NO: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_NO_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_YES: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_YES_EXCLUDE_DESCENDANTS: ClassVar[int]
    INVISIBLE: ClassVar[int]
    KEEP_SCREEN_ON: ClassVar[int]
    LAYER_TYPE_HARDWARE: ClassVar[int]
    LAYER_TYPE_NONE: ClassVar[int]
    LAYER_TYPE_SOFTWARE: ClassVar[int]
    LAYOUT_DIRECTION_INHERIT: ClassVar[int]
    LAYOUT_DIRECTION_LOCALE: ClassVar[int]
    LAYOUT_DIRECTION_LTR: ClassVar[int]
    LAYOUT_DIRECTION_RTL: ClassVar[int]
    MEASURED_HEIGHT_STATE_SHIFT: ClassVar[int]
    MEASURED_SIZE_MASK: ClassVar[int]
    MEASURED_STATE_MASK: ClassVar[int]
    MEASURED_STATE_TOO_SMALL: ClassVar[int]
    NOT_FOCUSABLE: ClassVar[int]
    NO_ID: ClassVar[int]
    OVER_SCROLL_ALWAYS: ClassVar[int]
    OVER_SCROLL_IF_CONTENT_SCROLLS: ClassVar[int]
    OVER_SCROLL_NEVER: ClassVar[int]
    REQUESTED_FRAME_RATE_CATEGORY_DEFAULT: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_HIGH: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_LOW: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_NORMAL: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_NO_PREFERENCE: ClassVar[float]
    ROTATION: ClassVar[Property]
    ROTATION_X: ClassVar[Property]
    ROTATION_Y: ClassVar[Property]
    SCALE_X: ClassVar[Property]
    SCALE_Y: ClassVar[Property]
    SCREEN_STATE_OFF: ClassVar[int]
    SCREEN_STATE_ON: ClassVar[int]
    SCROLLBARS_INSIDE_INSET: ClassVar[int]
    SCROLLBARS_INSIDE_OVERLAY: ClassVar[int]
    SCROLLBARS_OUTSIDE_INSET: ClassVar[int]
    SCROLLBARS_OUTSIDE_OVERLAY: ClassVar[int]
    SCROLLBAR_POSITION_DEFAULT: ClassVar[int]
    SCROLLBAR_POSITION_LEFT: ClassVar[int]
    SCROLLBAR_POSITION_RIGHT: ClassVar[int]
    SCROLL_AXIS_HORIZONTAL: ClassVar[int]
    SCROLL_AXIS_NONE: ClassVar[int]
    SCROLL_AXIS_VERTICAL: ClassVar[int]
    SCROLL_CAPTURE_HINT_AUTO: ClassVar[int]
    SCROLL_CAPTURE_HINT_EXCLUDE: ClassVar[int]
    SCROLL_CAPTURE_HINT_EXCLUDE_DESCENDANTS: ClassVar[int]
    SCROLL_CAPTURE_HINT_INCLUDE: ClassVar[int]
    SCROLL_INDICATOR_BOTTOM: ClassVar[int]
    SCROLL_INDICATOR_END: ClassVar[int]
    SCROLL_INDICATOR_LEFT: ClassVar[int]
    SCROLL_INDICATOR_RIGHT: ClassVar[int]
    SCROLL_INDICATOR_START: ClassVar[int]
    SCROLL_INDICATOR_TOP: ClassVar[int]
    SOUND_EFFECTS_ENABLED: ClassVar[int]
    STATUS_BAR_HIDDEN: ClassVar[int]
    STATUS_BAR_VISIBLE: ClassVar[int]
    SYSTEM_UI_FLAG_FULLSCREEN: ClassVar[int]
    SYSTEM_UI_FLAG_HIDE_NAVIGATION: ClassVar[int]
    SYSTEM_UI_FLAG_IMMERSIVE: ClassVar[int]
    SYSTEM_UI_FLAG_IMMERSIVE_STICKY: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_STABLE: ClassVar[int]
    SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR: ClassVar[int]
    SYSTEM_UI_FLAG_LIGHT_STATUS_BAR: ClassVar[int]
    SYSTEM_UI_FLAG_LOW_PROFILE: ClassVar[int]
    SYSTEM_UI_FLAG_VISIBLE: ClassVar[int]
    SYSTEM_UI_LAYOUT_FLAGS: ClassVar[int]
    TEXT_ALIGNMENT_CENTER: ClassVar[int]
    TEXT_ALIGNMENT_GRAVITY: ClassVar[int]
    TEXT_ALIGNMENT_INHERIT: ClassVar[int]
    TEXT_ALIGNMENT_TEXT_END: ClassVar[int]
    TEXT_ALIGNMENT_TEXT_START: ClassVar[int]
    TEXT_ALIGNMENT_VIEW_END: ClassVar[int]
    TEXT_ALIGNMENT_VIEW_START: ClassVar[int]
    TEXT_DIRECTION_ANY_RTL: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG_LTR: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG_RTL: ClassVar[int]
    TEXT_DIRECTION_INHERIT: ClassVar[int]
    TEXT_DIRECTION_LOCALE: ClassVar[int]
    TEXT_DIRECTION_LTR: ClassVar[int]
    TEXT_DIRECTION_RTL: ClassVar[int]
    TRANSLATION_X: ClassVar[Property]
    TRANSLATION_Y: ClassVar[Property]
    TRANSLATION_Z: ClassVar[Property]
    VISIBLE: ClassVar[int]
    X: ClassVar[Property]
    Y: ClassVar[Property]
    Z: ClassVar[Property]
    @overload
    def __init__(self, p0: Context, p1: int, p2: int) -> None: ...
    @overload
    def __init__(self, p0: Context) -> None: ...
    @staticmethod
    def getDefaultPaddingForWidget(p0: Context, p1: ComponentName, p2: Rect) -> Rect: ...
    def getAppWidgetId(self) -> int: ...
    def getAppWidgetInfo(self) -> AppWidgetProviderInfo: ...
    def resetColorResources(self) -> None: ...
    def setAppWidget(self, p0: int, p1: AppWidgetProviderInfo) -> None: ...
    def setColorResources(self, p0: SparseIntArray) -> None: ...
    def setExecutor(self, p0: Executor) -> None: ...
    def setOnLightBackground(self, p0: bool) -> None: ...
    def updateAppWidget(self, p0: RemoteViews) -> None: ...
    def updateAppWidgetOptions(self, p0: Bundle) -> None: ...
    @overload
    def updateAppWidgetSize(self, p0: Bundle, p1: list) -> None: ...
    @overload
    def updateAppWidgetSize(self, p0: Bundle, p1: int, p2: int, p3: int, p4: int) -> None: ...
    def onWindowFocusChanged(self, p0: bool) -> None: ...
    @overload
    def generateLayoutParams(self, p0: AttributeSet) -> Any: ...
    @overload
    def generateLayoutParams(self, p0: AttributeSet) -> Any: ...

from typing import Any, ClassVar, overload
from android.app.PendingIntent import PendingIntent
from android.appwidget.AppWidgetProviderInfo import AppWidgetProviderInfo
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.os.Bundle import Bundle
from android.os.UserHandle import UserHandle
from android.widget.RemoteViews import RemoteViews

class AppWidgetManager:
    ACTION_APPWIDGET_BIND: ClassVar[str]
    ACTION_APPWIDGET_CONFIGURE: ClassVar[str]
    ACTION_APPWIDGET_DELETED: ClassVar[str]
    ACTION_APPWIDGET_DISABLED: ClassVar[str]
    ACTION_APPWIDGET_ENABLED: ClassVar[str]
    ACTION_APPWIDGET_HOST_RESTORED: ClassVar[str]
    ACTION_APPWIDGET_OPTIONS_CHANGED: ClassVar[str]
    ACTION_APPWIDGET_PICK: ClassVar[str]
    ACTION_APPWIDGET_RESTORED: ClassVar[str]
    ACTION_APPWIDGET_UPDATE: ClassVar[str]
    EXTRA_APPWIDGET_ID: ClassVar[str]
    EXTRA_APPWIDGET_IDS: ClassVar[str]
    EXTRA_APPWIDGET_OLD_IDS: ClassVar[str]
    EXTRA_APPWIDGET_OPTIONS: ClassVar[str]
    EXTRA_APPWIDGET_PREVIEW: ClassVar[str]
    EXTRA_APPWIDGET_PROVIDER: ClassVar[str]
    EXTRA_APPWIDGET_PROVIDER_PROFILE: ClassVar[str]
    EXTRA_CUSTOM_EXTRAS: ClassVar[str]
    EXTRA_CUSTOM_INFO: ClassVar[str]
    EXTRA_HOST_ID: ClassVar[str]
    INVALID_APPWIDGET_ID: ClassVar[int]
    META_DATA_APPWIDGET_PROVIDER: ClassVar[str]
    OPTION_APPWIDGET_HOST_CATEGORY: ClassVar[str]
    OPTION_APPWIDGET_MAX_HEIGHT: ClassVar[str]
    OPTION_APPWIDGET_MAX_WIDTH: ClassVar[str]
    OPTION_APPWIDGET_MIN_HEIGHT: ClassVar[str]
    OPTION_APPWIDGET_MIN_WIDTH: ClassVar[str]
    OPTION_APPWIDGET_RESTORE_COMPLETED: ClassVar[str]
    OPTION_APPWIDGET_SIZES: ClassVar[str]
    def getAppWidgetIds(self, p0: ComponentName) -> Any: ...
    def getAppWidgetInfo(self, p0: int) -> AppWidgetProviderInfo: ...
    @overload
    def updateAppWidget(self, p0: Any, p1: RemoteViews) -> None: ...
    @overload
    def updateAppWidget(self, p0: ComponentName, p1: RemoteViews) -> None: ...
    @overload
    def updateAppWidget(self, p0: int, p1: RemoteViews) -> None: ...
    def updateAppWidgetOptions(self, p0: int, p1: Bundle) -> None: ...
    @overload
    def bindAppWidgetIdIfAllowed(self, p0: int, p1: UserHandle, p2: ComponentName, p3: Bundle) -> bool: ...
    @overload
    def bindAppWidgetIdIfAllowed(self, p0: int, p1: ComponentName) -> bool: ...
    @overload
    def bindAppWidgetIdIfAllowed(self, p0: int, p1: ComponentName, p2: Bundle) -> bool: ...
    def getAppWidgetOptions(self, p0: int) -> Bundle: ...
    def getInstalledProviders(self) -> list: ...
    def getInstalledProvidersForPackage(self, p0: str, p1: UserHandle) -> list: ...
    def getInstalledProvidersForProfile(self, p0: UserHandle) -> list: ...
    def getWidgetPreview(self, p0: ComponentName, p1: UserHandle, p2: int) -> RemoteViews: ...
    def isRequestPinAppWidgetSupported(self) -> bool: ...
    @overload
    def notifyAppWidgetViewDataChanged(self, p0: int, p1: int) -> None: ...
    @overload
    def notifyAppWidgetViewDataChanged(self, p0: Any, p1: int) -> None: ...
    @overload
    def partiallyUpdateAppWidget(self, p0: Any, p1: RemoteViews) -> None: ...
    @overload
    def partiallyUpdateAppWidget(self, p0: int, p1: RemoteViews) -> None: ...
    def removeWidgetPreview(self, p0: ComponentName, p1: int) -> None: ...
    def requestPinAppWidget(self, p0: ComponentName, p1: Bundle, p2: PendingIntent) -> bool: ...
    def setWidgetPreview(self, p0: ComponentName, p1: int, p2: RemoteViews) -> bool: ...
    def updateAppWidgetProviderInfo(self, p0: ComponentName, p1: str) -> None: ...
    @staticmethod
    def getInstance(p0: Context) -> "AppWidgetManager": ...

from typing import Any, ClassVar, overload
from android.appwidget.AppWidgetManager import AppWidgetManager
from android.content.Context import Context
from android.content.Intent import Intent
from android.os.Bundle import Bundle

class AppWidgetProvider:
    def __init__(self) -> None: ...
    def onReceive(self, p0: Context, p1: Intent) -> None: ...
    def onUpdate(self, p0: Context, p1: AppWidgetManager, p2: Any) -> None: ...
    def onDeleted(self, p0: Context, p1: Any) -> None: ...
    def onAppWidgetOptionsChanged(self, p0: Context, p1: AppWidgetManager, p2: int, p3: Bundle) -> None: ...
    def onRestored(self, p0: Context, p1: Any, p2: Any) -> None: ...
    def onDisabled(self, p0: Context) -> None: ...
    def onEnabled(self, p0: Context) -> None: ...

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
    WIDGET_CATEGORY_NOT_KEYGUARD: ClassVar[int]
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
    def getProfile(self) -> UserHandle: ...
    def loadPreviewImage(self, p0: Context, p1: int) -> Drawable: ...
    def loadIcon(self, p0: Context, p1: int) -> Drawable: ...
    def loadLabel(self, p0: PackageManager) -> str: ...
    def loadDescription(self, p0: Context) -> str: ...
    def getActivityInfo(self) -> ActivityInfo: ...
    def toString(self) -> str: ...
    @overload
    def clone(self) -> Any: ...
    @overload
    def clone(self) -> "AppWidgetProviderInfo": ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

