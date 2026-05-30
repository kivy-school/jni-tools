from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.util.AttributeSet import AttributeSet
from android.util.Property import Property
from android.view.inputmethod.ExtractedText import ExtractedText

class ExtractEditText:
    AUTO_SIZE_TEXT_TYPE_NONE: ClassVar[int]
    AUTO_SIZE_TEXT_TYPE_UNIFORM: ClassVar[int]
    FOCUSED_SEARCH_RESULT_INDEX_NONE: ClassVar[int]
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
    def __init__(self, p0: Context) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: AttributeSet) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: AttributeSet, p2: int) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: AttributeSet, p2: int, p3: int) -> None: ...
    def finishInternalChanges(self) -> None: ...
    def hasVerticalScrollBar(self) -> bool: ...
    def startInternalChanges(self) -> None: ...
    def isInputMethodTarget(self) -> bool: ...
    def onTextContextMenuItem(self, p0: int) -> bool: ...
    def setExtractedText(self, p0: ExtractedText) -> None: ...
    def hasWindowFocus(self) -> bool: ...
    def isFocused(self) -> bool: ...
    def performClick(self) -> bool: ...
    def hasFocus(self) -> bool: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.res.Resources import Resources
from android.content.res.XmlResourceParser import XmlResourceParser
from android.graphics.drawable.Drawable import Drawable

class Keyboard:
    EDGE_BOTTOM: ClassVar[int]
    EDGE_LEFT: ClassVar[int]
    EDGE_RIGHT: ClassVar[int]
    EDGE_TOP: ClassVar[int]
    KEYCODE_ALT: ClassVar[int]
    KEYCODE_CANCEL: ClassVar[int]
    KEYCODE_DELETE: ClassVar[int]
    KEYCODE_DONE: ClassVar[int]
    KEYCODE_MODE_CHANGE: ClassVar[int]
    KEYCODE_SHIFT: ClassVar[int]
    @overload
    def __init__(self, p0: Context, p1: int, p2: int) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: int, p2: str, p3: int, p4: int) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: int) -> None: ...
    def getModifierKeys(self) -> list: ...
    def getNearestKeys(self, p0: int, p1: int) -> Any: ...
    def getShiftKeyIndex(self) -> int: ...
    def isShifted(self) -> bool: ...
    def setShifted(self, p0: bool) -> bool: ...
    def getMinWidth(self) -> int: ...
    def getHeight(self) -> int: ...
    def getKeys(self) -> list: ...

    class Row:
        defaultHeight: int
        defaultHorizontalGap: int
        defaultWidth: int
        mode: int
        rowEdgeFlags: int
        verticalGap: int
        @overload
        def __init__(self, p0: Resources, p1: "Keyboard", p2: XmlResourceParser) -> None: ...
        @overload
        def __init__(self, p0: "Keyboard") -> None: ...

    class Key:
        codes: Any
        edgeFlags: int
        gap: int
        height: int
        icon: Drawable
        iconPreview: Drawable
        label: str
        modifier: bool
        on: bool
        popupCharacters: str
        popupResId: int
        pressed: bool
        repeatable: bool
        sticky: bool
        text: str
        width: int
        x: int
        y: int
        @overload
        def __init__(self, p0: Any) -> None: ...
        @overload
        def __init__(self, p0: Resources, p1: Any, p2: int, p3: int, p4: XmlResourceParser) -> None: ...
        def getCurrentDrawableState(self) -> Any: ...
        def isInside(self, p0: int, p1: int) -> bool: ...
        def onPressed(self) -> None: ...
        def onReleased(self, p0: bool) -> None: ...
        def squaredDistanceFrom(self, p0: int, p1: int) -> int: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.graphics.Canvas import Canvas
from android.inputmethodservice.Keyboard import Keyboard
from android.util.AttributeSet import AttributeSet
from android.util.Property import Property
from android.view.MotionEvent import MotionEvent
from android.view.View import View

class KeyboardView:
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
    def __init__(self, p0: Context, p1: AttributeSet, p2: int, p3: int) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: AttributeSet, p2: int) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: AttributeSet) -> None: ...
    def isShifted(self) -> bool: ...
    def setShifted(self, p0: bool) -> bool: ...
    def isProximityCorrectionEnabled(self) -> bool: ...
    def invalidateAllKeys(self) -> None: ...
    def handleBack(self) -> bool: ...
    def getKeyboard(self) -> Keyboard: ...
    def setKeyboard(self, p0: Keyboard) -> None: ...
    def setOnKeyboardActionListener(self, p0: Any) -> None: ...
    def setPopupOffset(self, p0: int, p1: int) -> None: ...
    def setPopupParent(self, p0: View) -> None: ...
    def setPreviewEnabled(self, p0: bool) -> None: ...
    def setProximityCorrectionEnabled(self, p0: bool) -> None: ...
    def setVerticalCorrection(self, p0: int) -> None: ...
    def closing(self) -> None: ...
    def onClick(self, p0: View) -> None: ...
    def onTouchEvent(self, p0: MotionEvent) -> bool: ...
    def onHoverEvent(self, p0: MotionEvent) -> bool: ...
    def onSizeChanged(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
    def onDetachedFromWindow(self) -> None: ...
    def onDraw(self, p0: Canvas) -> None: ...
    def onMeasure(self, p0: int, p1: int) -> None: ...
    def invalidateKey(self, p0: int) -> None: ...
    def isPreviewEnabled(self) -> bool: ...

    class OnKeyboardActionListener:
        def onText(self, p0: str) -> None: ...
        def onPress(self, p0: int) -> None: ...
        def swipeDown(self) -> None: ...
        def swipeLeft(self) -> None: ...
        def swipeRight(self) -> None: ...
        def swipeUp(self) -> None: ...
        def onRelease(self, p0: int) -> None: ...
        def onKey(self, p0: int, p1: Any) -> None: ...

from typing import Any, ClassVar, overload
from android.content.ComponentCallbacks import ComponentCallbacks
from android.content.Intent import Intent
from android.content.res.Configuration import Configuration
from android.os.IBinder import IBinder
from android.view.KeyEvent import KeyEvent
from android.view.MotionEvent import MotionEvent
from android.view.inputmethod.InputMethodSession import InputMethodSession

class AbstractInputMethodService:
    START_CONTINUATION_MASK: ClassVar[int]
    START_FLAG_REDELIVERY: ClassVar[int]
    START_FLAG_RETRY: ClassVar[int]
    START_NOT_STICKY: ClassVar[int]
    START_REDELIVER_INTENT: ClassVar[int]
    START_STICKY: ClassVar[int]
    START_STICKY_COMPATIBILITY: ClassVar[int]
    STOP_FOREGROUND_DETACH: ClassVar[int]
    STOP_FOREGROUND_LEGACY: ClassVar[int]
    STOP_FOREGROUND_REMOVE: ClassVar[int]
    TRIM_MEMORY_BACKGROUND: ClassVar[int]
    TRIM_MEMORY_COMPLETE: ClassVar[int]
    TRIM_MEMORY_MODERATE: ClassVar[int]
    TRIM_MEMORY_RUNNING_CRITICAL: ClassVar[int]
    TRIM_MEMORY_RUNNING_LOW: ClassVar[int]
    TRIM_MEMORY_RUNNING_MODERATE: ClassVar[int]
    TRIM_MEMORY_UI_HIDDEN: ClassVar[int]
    ACCESSIBILITY_SERVICE: ClassVar[str]
    ACCOUNT_SERVICE: ClassVar[str]
    ACTIVITY_SERVICE: ClassVar[str]
    ADVANCED_PROTECTION_SERVICE: ClassVar[str]
    ALARM_SERVICE: ClassVar[str]
    APPWIDGET_SERVICE: ClassVar[str]
    APP_FUNCTION_SERVICE: ClassVar[str]
    APP_OPS_SERVICE: ClassVar[str]
    APP_SEARCH_SERVICE: ClassVar[str]
    AUDIO_SERVICE: ClassVar[str]
    BATTERY_SERVICE: ClassVar[str]
    BIND_ABOVE_CLIENT: ClassVar[int]
    BIND_ADJUST_WITH_ACTIVITY: ClassVar[int]
    BIND_ALLOW_ACTIVITY_STARTS: ClassVar[int]
    BIND_ALLOW_OOM_MANAGEMENT: ClassVar[int]
    BIND_AUTO_CREATE: ClassVar[int]
    BIND_DEBUG_UNBIND: ClassVar[int]
    BIND_EXTERNAL_SERVICE: ClassVar[int]
    BIND_EXTERNAL_SERVICE_LONG: ClassVar[int]
    BIND_IMPORTANT: ClassVar[int]
    BIND_INCLUDE_CAPABILITIES: ClassVar[int]
    BIND_NOT_FOREGROUND: ClassVar[int]
    BIND_NOT_PERCEPTIBLE: ClassVar[int]
    BIND_PACKAGE_ISOLATED_PROCESS: ClassVar[int]
    BIND_SHARED_ISOLATED_PROCESS: ClassVar[int]
    BIND_WAIVE_PRIORITY: ClassVar[int]
    BIOMETRIC_SERVICE: ClassVar[str]
    BLOB_STORE_SERVICE: ClassVar[str]
    BLUETOOTH_SERVICE: ClassVar[str]
    BUGREPORT_SERVICE: ClassVar[str]
    CAMERA_SERVICE: ClassVar[str]
    CAPTIONING_SERVICE: ClassVar[str]
    CARRIER_CONFIG_SERVICE: ClassVar[str]
    CLIPBOARD_SERVICE: ClassVar[str]
    COMPANION_DEVICE_SERVICE: ClassVar[str]
    CONNECTIVITY_DIAGNOSTICS_SERVICE: ClassVar[str]
    CONNECTIVITY_SERVICE: ClassVar[str]
    CONSUMER_IR_SERVICE: ClassVar[str]
    CONTACT_KEYS_SERVICE: ClassVar[str]
    CONTEXT_IGNORE_SECURITY: ClassVar[int]
    CONTEXT_INCLUDE_CODE: ClassVar[int]
    CONTEXT_RESTRICTED: ClassVar[int]
    CREDENTIAL_SERVICE: ClassVar[str]
    CROSS_PROFILE_APPS_SERVICE: ClassVar[str]
    DEVICE_ID_DEFAULT: ClassVar[int]
    DEVICE_ID_INVALID: ClassVar[int]
    DEVICE_LOCK_SERVICE: ClassVar[str]
    DEVICE_POLICY_SERVICE: ClassVar[str]
    DISPLAY_HASH_SERVICE: ClassVar[str]
    DISPLAY_SERVICE: ClassVar[str]
    DOMAIN_VERIFICATION_SERVICE: ClassVar[str]
    DOWNLOAD_SERVICE: ClassVar[str]
    DROPBOX_SERVICE: ClassVar[str]
    EUICC_SERVICE: ClassVar[str]
    FILE_INTEGRITY_SERVICE: ClassVar[str]
    FINGERPRINT_SERVICE: ClassVar[str]
    GAME_SERVICE: ClassVar[str]
    GRAMMATICAL_INFLECTION_SERVICE: ClassVar[str]
    HARDWARE_PROPERTIES_SERVICE: ClassVar[str]
    HEALTHCONNECT_SERVICE: ClassVar[str]
    INPUT_METHOD_SERVICE: ClassVar[str]
    INPUT_SERVICE: ClassVar[str]
    IPSEC_SERVICE: ClassVar[str]
    JOB_SCHEDULER_SERVICE: ClassVar[str]
    KEYGUARD_SERVICE: ClassVar[str]
    KEYSTORE_SERVICE: ClassVar[str]
    LAUNCHER_APPS_SERVICE: ClassVar[str]
    LAYOUT_INFLATER_SERVICE: ClassVar[str]
    LOCALE_SERVICE: ClassVar[str]
    LOCATION_SERVICE: ClassVar[str]
    MEDIA_COMMUNICATION_SERVICE: ClassVar[str]
    MEDIA_METRICS_SERVICE: ClassVar[str]
    MEDIA_PROJECTION_SERVICE: ClassVar[str]
    MEDIA_QUALITY_SERVICE: ClassVar[str]
    MEDIA_ROUTER_SERVICE: ClassVar[str]
    MEDIA_SESSION_SERVICE: ClassVar[str]
    MIDI_SERVICE: ClassVar[str]
    MODE_APPEND: ClassVar[int]
    MODE_ENABLE_WRITE_AHEAD_LOGGING: ClassVar[int]
    MODE_MULTI_PROCESS: ClassVar[int]
    MODE_NO_LOCALIZED_COLLATORS: ClassVar[int]
    MODE_PRIVATE: ClassVar[int]
    MODE_WORLD_READABLE: ClassVar[int]
    MODE_WORLD_WRITEABLE: ClassVar[int]
    NETWORK_STATS_SERVICE: ClassVar[str]
    NFC_SERVICE: ClassVar[str]
    NOTIFICATION_SERVICE: ClassVar[str]
    NSD_SERVICE: ClassVar[str]
    OVERLAY_SERVICE: ClassVar[str]
    PEOPLE_SERVICE: ClassVar[str]
    PERFORMANCE_HINT_SERVICE: ClassVar[str]
    PERSISTENT_DATA_BLOCK_SERVICE: ClassVar[str]
    POWER_SERVICE: ClassVar[str]
    PRINT_SERVICE: ClassVar[str]
    PROFILING_SERVICE: ClassVar[str]
    RECEIVER_EXPORTED: ClassVar[int]
    RECEIVER_NOT_EXPORTED: ClassVar[int]
    RECEIVER_VISIBLE_TO_INSTANT_APPS: ClassVar[int]
    RESTRICTIONS_SERVICE: ClassVar[str]
    ROLE_SERVICE: ClassVar[str]
    SATELLITE_SERVICE: ClassVar[str]
    SEARCH_SERVICE: ClassVar[str]
    SECURITY_STATE_SERVICE: ClassVar[str]
    SENSOR_SERVICE: ClassVar[str]
    SHORTCUT_SERVICE: ClassVar[str]
    STATUS_BAR_SERVICE: ClassVar[str]
    STORAGE_SERVICE: ClassVar[str]
    STORAGE_STATS_SERVICE: ClassVar[str]
    SYSTEM_HEALTH_SERVICE: ClassVar[str]
    TELECOM_SERVICE: ClassVar[str]
    TELEPHONY_IMS_SERVICE: ClassVar[str]
    TELEPHONY_SERVICE: ClassVar[str]
    TELEPHONY_SUBSCRIPTION_SERVICE: ClassVar[str]
    TETHERING_SERVICE: ClassVar[str]
    TEXT_CLASSIFICATION_SERVICE: ClassVar[str]
    TEXT_SERVICES_MANAGER_SERVICE: ClassVar[str]
    TV_AD_SERVICE: ClassVar[str]
    TV_INPUT_SERVICE: ClassVar[str]
    TV_INTERACTIVE_APP_SERVICE: ClassVar[str]
    UI_MODE_SERVICE: ClassVar[str]
    USAGE_STATS_SERVICE: ClassVar[str]
    USB_SERVICE: ClassVar[str]
    USER_SERVICE: ClassVar[str]
    VIBRATOR_MANAGER_SERVICE: ClassVar[str]
    VIBRATOR_SERVICE: ClassVar[str]
    VIRTUAL_DEVICE_SERVICE: ClassVar[str]
    VPN_MANAGEMENT_SERVICE: ClassVar[str]
    WALLPAPER_SERVICE: ClassVar[str]
    WIFI_AWARE_SERVICE: ClassVar[str]
    WIFI_P2P_SERVICE: ClassVar[str]
    WIFI_RTT_RANGING_SERVICE: ClassVar[str]
    WIFI_SERVICE: ClassVar[str]
    WINDOW_SERVICE: ClassVar[str]
    def __init__(self) -> None: ...
    def onCreateInputMethodSessionInterface(self) -> Any: ...
    def onCreateInputMethodInterface(self) -> Any: ...
    def onShouldVerifyKeyEvent(self, p0: KeyEvent) -> bool: ...
    def onBind(self, p0: Intent) -> IBinder: ...
    def onDestroy(self) -> None: ...
    def getKeyDispatcherState(self) -> Any: ...
    def onGenericMotionEvent(self, p0: MotionEvent) -> bool: ...
    def onTrackballEvent(self, p0: MotionEvent) -> bool: ...
    def onConfigurationChanged(self, p0: Configuration) -> None: ...
    def onLowMemory(self) -> None: ...
    def onTrimMemory(self, p0: int) -> None: ...
    def getSystemService(self, p0: str) -> Any: ...
    def registerComponentCallbacks(self, p0: ComponentCallbacks) -> None: ...
    def unregisterComponentCallbacks(self, p0: ComponentCallbacks) -> None: ...

    class AbstractInputMethodSessionImpl:
        def __init__(self, p0: "AbstractInputMethodService") -> None: ...
        def onShouldVerifyKeyEvent(self, p0: KeyEvent) -> bool: ...
        def revokeSelf(self) -> None: ...
        def isRevoked(self) -> bool: ...
        def isEnabled(self) -> bool: ...
        def setEnabled(self, p0: bool) -> None: ...
        def dispatchGenericMotionEvent(self, p0: int, p1: MotionEvent, p2: Any) -> None: ...
        def dispatchKeyEvent(self, p0: int, p1: KeyEvent, p2: Any) -> None: ...
        def dispatchTrackballEvent(self, p0: int, p1: MotionEvent, p2: Any) -> None: ...

    class AbstractInputMethodImpl:
        SERVICE_INTERFACE: ClassVar[str]
        SERVICE_META_DATA: ClassVar[str]
        SHOW_EXPLICIT: ClassVar[int]
        SHOW_FORCED: ClassVar[int]
        def __init__(self, p0: "AbstractInputMethodService") -> None: ...
        def revokeSession(self, p0: InputMethodSession) -> None: ...
        def setSessionEnabled(self, p0: InputMethodSession, p1: bool) -> None: ...
        def createSession(self, p0: Any) -> None: ...

from typing import Any, ClassVar, overload
from android.app.Dialog import Dialog
from android.content.res.Configuration import Configuration
from android.graphics.Rect import Rect
from android.graphics.Region import Region
from android.os.Bundle import Bundle
from android.os.IBinder import IBinder
from android.os.ResultReceiver import ResultReceiver
from android.view.KeyEvent import KeyEvent
from android.view.LayoutInflater import LayoutInflater
from android.view.MotionEvent import MotionEvent
from android.view.View import View
from android.view.Window import Window
from android.view.inputmethod.CursorAnchorInfo import CursorAnchorInfo
from android.view.inputmethod.EditorInfo import EditorInfo
from android.view.inputmethod.ExtractedText import ExtractedText
from android.view.inputmethod.InlineSuggestionsRequest import InlineSuggestionsRequest
from android.view.inputmethod.InlineSuggestionsResponse import InlineSuggestionsResponse
from android.view.inputmethod.InputBinding import InputBinding
from android.view.inputmethod.InputConnection import InputConnection
from android.view.inputmethod.InputMethodSubtype import InputMethodSubtype
from java.time.Duration import Duration

class InputMethodService:
    BACK_DISPOSITION_ADJUST_NOTHING: ClassVar[int]
    BACK_DISPOSITION_DEFAULT: ClassVar[int]
    BACK_DISPOSITION_WILL_DISMISS: ClassVar[int]
    BACK_DISPOSITION_WILL_NOT_DISMISS: ClassVar[int]
    START_CONTINUATION_MASK: ClassVar[int]
    START_FLAG_REDELIVERY: ClassVar[int]
    START_FLAG_RETRY: ClassVar[int]
    START_NOT_STICKY: ClassVar[int]
    START_REDELIVER_INTENT: ClassVar[int]
    START_STICKY: ClassVar[int]
    START_STICKY_COMPATIBILITY: ClassVar[int]
    STOP_FOREGROUND_DETACH: ClassVar[int]
    STOP_FOREGROUND_LEGACY: ClassVar[int]
    STOP_FOREGROUND_REMOVE: ClassVar[int]
    TRIM_MEMORY_BACKGROUND: ClassVar[int]
    TRIM_MEMORY_COMPLETE: ClassVar[int]
    TRIM_MEMORY_MODERATE: ClassVar[int]
    TRIM_MEMORY_RUNNING_CRITICAL: ClassVar[int]
    TRIM_MEMORY_RUNNING_LOW: ClassVar[int]
    TRIM_MEMORY_RUNNING_MODERATE: ClassVar[int]
    TRIM_MEMORY_UI_HIDDEN: ClassVar[int]
    ACCESSIBILITY_SERVICE: ClassVar[str]
    ACCOUNT_SERVICE: ClassVar[str]
    ACTIVITY_SERVICE: ClassVar[str]
    ADVANCED_PROTECTION_SERVICE: ClassVar[str]
    ALARM_SERVICE: ClassVar[str]
    APPWIDGET_SERVICE: ClassVar[str]
    APP_FUNCTION_SERVICE: ClassVar[str]
    APP_OPS_SERVICE: ClassVar[str]
    APP_SEARCH_SERVICE: ClassVar[str]
    AUDIO_SERVICE: ClassVar[str]
    BATTERY_SERVICE: ClassVar[str]
    BIND_ABOVE_CLIENT: ClassVar[int]
    BIND_ADJUST_WITH_ACTIVITY: ClassVar[int]
    BIND_ALLOW_ACTIVITY_STARTS: ClassVar[int]
    BIND_ALLOW_OOM_MANAGEMENT: ClassVar[int]
    BIND_AUTO_CREATE: ClassVar[int]
    BIND_DEBUG_UNBIND: ClassVar[int]
    BIND_EXTERNAL_SERVICE: ClassVar[int]
    BIND_EXTERNAL_SERVICE_LONG: ClassVar[int]
    BIND_IMPORTANT: ClassVar[int]
    BIND_INCLUDE_CAPABILITIES: ClassVar[int]
    BIND_NOT_FOREGROUND: ClassVar[int]
    BIND_NOT_PERCEPTIBLE: ClassVar[int]
    BIND_PACKAGE_ISOLATED_PROCESS: ClassVar[int]
    BIND_SHARED_ISOLATED_PROCESS: ClassVar[int]
    BIND_WAIVE_PRIORITY: ClassVar[int]
    BIOMETRIC_SERVICE: ClassVar[str]
    BLOB_STORE_SERVICE: ClassVar[str]
    BLUETOOTH_SERVICE: ClassVar[str]
    BUGREPORT_SERVICE: ClassVar[str]
    CAMERA_SERVICE: ClassVar[str]
    CAPTIONING_SERVICE: ClassVar[str]
    CARRIER_CONFIG_SERVICE: ClassVar[str]
    CLIPBOARD_SERVICE: ClassVar[str]
    COMPANION_DEVICE_SERVICE: ClassVar[str]
    CONNECTIVITY_DIAGNOSTICS_SERVICE: ClassVar[str]
    CONNECTIVITY_SERVICE: ClassVar[str]
    CONSUMER_IR_SERVICE: ClassVar[str]
    CONTACT_KEYS_SERVICE: ClassVar[str]
    CONTEXT_IGNORE_SECURITY: ClassVar[int]
    CONTEXT_INCLUDE_CODE: ClassVar[int]
    CONTEXT_RESTRICTED: ClassVar[int]
    CREDENTIAL_SERVICE: ClassVar[str]
    CROSS_PROFILE_APPS_SERVICE: ClassVar[str]
    DEVICE_ID_DEFAULT: ClassVar[int]
    DEVICE_ID_INVALID: ClassVar[int]
    DEVICE_LOCK_SERVICE: ClassVar[str]
    DEVICE_POLICY_SERVICE: ClassVar[str]
    DISPLAY_HASH_SERVICE: ClassVar[str]
    DISPLAY_SERVICE: ClassVar[str]
    DOMAIN_VERIFICATION_SERVICE: ClassVar[str]
    DOWNLOAD_SERVICE: ClassVar[str]
    DROPBOX_SERVICE: ClassVar[str]
    EUICC_SERVICE: ClassVar[str]
    FILE_INTEGRITY_SERVICE: ClassVar[str]
    FINGERPRINT_SERVICE: ClassVar[str]
    GAME_SERVICE: ClassVar[str]
    GRAMMATICAL_INFLECTION_SERVICE: ClassVar[str]
    HARDWARE_PROPERTIES_SERVICE: ClassVar[str]
    HEALTHCONNECT_SERVICE: ClassVar[str]
    INPUT_METHOD_SERVICE: ClassVar[str]
    INPUT_SERVICE: ClassVar[str]
    IPSEC_SERVICE: ClassVar[str]
    JOB_SCHEDULER_SERVICE: ClassVar[str]
    KEYGUARD_SERVICE: ClassVar[str]
    KEYSTORE_SERVICE: ClassVar[str]
    LAUNCHER_APPS_SERVICE: ClassVar[str]
    LAYOUT_INFLATER_SERVICE: ClassVar[str]
    LOCALE_SERVICE: ClassVar[str]
    LOCATION_SERVICE: ClassVar[str]
    MEDIA_COMMUNICATION_SERVICE: ClassVar[str]
    MEDIA_METRICS_SERVICE: ClassVar[str]
    MEDIA_PROJECTION_SERVICE: ClassVar[str]
    MEDIA_QUALITY_SERVICE: ClassVar[str]
    MEDIA_ROUTER_SERVICE: ClassVar[str]
    MEDIA_SESSION_SERVICE: ClassVar[str]
    MIDI_SERVICE: ClassVar[str]
    MODE_APPEND: ClassVar[int]
    MODE_ENABLE_WRITE_AHEAD_LOGGING: ClassVar[int]
    MODE_MULTI_PROCESS: ClassVar[int]
    MODE_NO_LOCALIZED_COLLATORS: ClassVar[int]
    MODE_PRIVATE: ClassVar[int]
    MODE_WORLD_READABLE: ClassVar[int]
    MODE_WORLD_WRITEABLE: ClassVar[int]
    NETWORK_STATS_SERVICE: ClassVar[str]
    NFC_SERVICE: ClassVar[str]
    NOTIFICATION_SERVICE: ClassVar[str]
    NSD_SERVICE: ClassVar[str]
    OVERLAY_SERVICE: ClassVar[str]
    PEOPLE_SERVICE: ClassVar[str]
    PERFORMANCE_HINT_SERVICE: ClassVar[str]
    PERSISTENT_DATA_BLOCK_SERVICE: ClassVar[str]
    POWER_SERVICE: ClassVar[str]
    PRINT_SERVICE: ClassVar[str]
    PROFILING_SERVICE: ClassVar[str]
    RECEIVER_EXPORTED: ClassVar[int]
    RECEIVER_NOT_EXPORTED: ClassVar[int]
    RECEIVER_VISIBLE_TO_INSTANT_APPS: ClassVar[int]
    RESTRICTIONS_SERVICE: ClassVar[str]
    ROLE_SERVICE: ClassVar[str]
    SATELLITE_SERVICE: ClassVar[str]
    SEARCH_SERVICE: ClassVar[str]
    SECURITY_STATE_SERVICE: ClassVar[str]
    SENSOR_SERVICE: ClassVar[str]
    SHORTCUT_SERVICE: ClassVar[str]
    STATUS_BAR_SERVICE: ClassVar[str]
    STORAGE_SERVICE: ClassVar[str]
    STORAGE_STATS_SERVICE: ClassVar[str]
    SYSTEM_HEALTH_SERVICE: ClassVar[str]
    TELECOM_SERVICE: ClassVar[str]
    TELEPHONY_IMS_SERVICE: ClassVar[str]
    TELEPHONY_SERVICE: ClassVar[str]
    TELEPHONY_SUBSCRIPTION_SERVICE: ClassVar[str]
    TETHERING_SERVICE: ClassVar[str]
    TEXT_CLASSIFICATION_SERVICE: ClassVar[str]
    TEXT_SERVICES_MANAGER_SERVICE: ClassVar[str]
    TV_AD_SERVICE: ClassVar[str]
    TV_INPUT_SERVICE: ClassVar[str]
    TV_INTERACTIVE_APP_SERVICE: ClassVar[str]
    UI_MODE_SERVICE: ClassVar[str]
    USAGE_STATS_SERVICE: ClassVar[str]
    USB_SERVICE: ClassVar[str]
    USER_SERVICE: ClassVar[str]
    VIBRATOR_MANAGER_SERVICE: ClassVar[str]
    VIBRATOR_SERVICE: ClassVar[str]
    VIRTUAL_DEVICE_SERVICE: ClassVar[str]
    VPN_MANAGEMENT_SERVICE: ClassVar[str]
    WALLPAPER_SERVICE: ClassVar[str]
    WIFI_AWARE_SERVICE: ClassVar[str]
    WIFI_P2P_SERVICE: ClassVar[str]
    WIFI_RTT_RANGING_SERVICE: ClassVar[str]
    WIFI_SERVICE: ClassVar[str]
    WINDOW_SERVICE: ClassVar[str]
    def __init__(self) -> None: ...
    def hideStatusIcon(self) -> None: ...
    def isFullscreenMode(self) -> bool: ...
    def shouldOfferSwitchingToNextInputMethod(self) -> bool: ...
    def showStatusIcon(self, p0: int) -> None: ...
    def switchToNextInputMethod(self, p0: bool) -> bool: ...
    def onComputeInsets(self, p0: Any) -> None: ...
    @overload
    def switchInputMethod(self, p0: str) -> None: ...
    @overload
    def switchInputMethod(self, p0: str, p1: InputMethodSubtype) -> None: ...
    def onCreateInputMethodSessionInterface(self) -> Any: ...
    def onCreateInputMethodInterface(self) -> Any: ...
    def onShouldVerifyKeyEvent(self, p0: KeyEvent) -> bool: ...
    def getCurrentInputStarted(self) -> bool: ...
    def getCurrentInputBinding(self) -> InputBinding: ...
    def hideWindow(self) -> None: ...
    def getBackDisposition(self) -> int: ...
    def enableHardwareAcceleration(self) -> bool: ...
    def finishConnectionlessStylusHandwriting(self, p0: str) -> None: ...
    def finishStylusHandwriting(self) -> None: ...
    def getCandidatesHiddenVisibility(self) -> int: ...
    def getCurrentInputConnection(self) -> InputConnection: ...
    def getCurrentInputEditorInfo(self) -> EditorInfo: ...
    def getInputMethodWindowRecommendedHeight(self) -> int: ...
    @staticmethod
    def getStylusHandwritingIdleTimeoutMax() -> Duration: ...
    def getStylusHandwritingSessionTimeout(self) -> Duration: ...
    def getStylusHandwritingWindow(self) -> Window: ...
    def getTextForImeAction(self, p0: int) -> str: ...
    def isExtractViewShown(self) -> bool: ...
    def isInputViewShown(self) -> bool: ...
    def isShowInputRequested(self) -> bool: ...
    def onAppPrivateCommand(self, p0: str, p1: Bundle) -> None: ...
    def onBindInput(self) -> None: ...
    def onConfigureWindow(self, p0: Window, p1: bool, p2: bool) -> None: ...
    def onCreateCandidatesView(self) -> View: ...
    def onCreateExtractTextView(self) -> View: ...
    def onCreateInlineSuggestionsRequest(self, p0: Bundle) -> InlineSuggestionsRequest: ...
    def onCreateInputView(self) -> View: ...
    def onCustomImeSwitcherButtonRequestedVisible(self, p0: bool) -> None: ...
    def onDisplayCompletions(self, p0: Any) -> None: ...
    def onEvaluateFullscreenMode(self) -> bool: ...
    def onEvaluateInputViewShown(self) -> bool: ...
    def onExtractTextContextMenuItem(self, p0: int) -> bool: ...
    def onExtractedCursorMovement(self, p0: int, p1: int) -> None: ...
    def onExtractedSelectionChanged(self, p0: int, p1: int) -> None: ...
    def onExtractedTextClicked(self) -> None: ...
    def onExtractingInputChanged(self, p0: EditorInfo) -> None: ...
    def onFinishCandidatesView(self, p0: bool) -> None: ...
    def onFinishInput(self) -> None: ...
    def onFinishInputView(self, p0: bool) -> None: ...
    def onFinishStylusHandwriting(self) -> None: ...
    def onInitializeInterface(self) -> None: ...
    def onInlineSuggestionsResponse(self, p0: InlineSuggestionsResponse) -> bool: ...
    def onPrepareStylusHandwriting(self) -> None: ...
    def onShowInputRequested(self, p0: int, p1: bool) -> bool: ...
    def onStartCandidatesView(self, p0: EditorInfo, p1: bool) -> None: ...
    def onStartConnectionlessStylusHandwriting(self, p0: int, p1: CursorAnchorInfo) -> bool: ...
    def onStartInput(self, p0: EditorInfo, p1: bool) -> None: ...
    def onStartInputView(self, p0: EditorInfo, p1: bool) -> None: ...
    def onStartStylusHandwriting(self) -> bool: ...
    def onStylusHandwritingMotionEvent(self, p0: MotionEvent) -> None: ...
    def onUnbindInput(self) -> None: ...
    def onUpdateCursor(self, p0: Rect) -> None: ...
    def onUpdateCursorAnchorInfo(self, p0: CursorAnchorInfo) -> None: ...
    def onUpdateEditorToolType(self, p0: int) -> None: ...
    def onUpdateExtractedText(self, p0: int, p1: ExtractedText) -> None: ...
    def onUpdateExtractingViews(self, p0: EditorInfo) -> None: ...
    def onUpdateExtractingVisibility(self, p0: EditorInfo) -> None: ...
    def onUpdateSelection(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    def onViewClicked(self, p0: bool) -> None: ...
    def onWindowHidden(self) -> None: ...
    def onWindowShown(self) -> None: ...
    def requestHideSelf(self, p0: int) -> None: ...
    def requestShowSelf(self, p0: int) -> None: ...
    def sendDefaultEditorAction(self, p0: bool) -> bool: ...
    def sendDownUpKeyEvents(self, p0: int) -> None: ...
    def sendKeyChar(self, p0: str) -> None: ...
    def setBackDisposition(self, p0: int) -> None: ...
    def setCandidatesView(self, p0: View) -> None: ...
    def setCandidatesViewShown(self, p0: bool) -> None: ...
    def setExtractView(self, p0: View) -> None: ...
    def setExtractViewShown(self, p0: bool) -> None: ...
    def setInputView(self, p0: View) -> None: ...
    def setStylusHandwritingRegion(self, p0: Region) -> None: ...
    def setStylusHandwritingSessionTimeout(self, p0: Duration) -> None: ...
    def showWindow(self, p0: bool) -> None: ...
    def switchToPreviousInputMethod(self) -> bool: ...
    def updateFullscreenMode(self) -> None: ...
    def updateInputViewShown(self) -> None: ...
    def onCreate(self) -> None: ...
    def onDestroy(self) -> None: ...
    def getWindow(self) -> Dialog: ...
    def onKeyUp(self, p0: int, p1: KeyEvent) -> bool: ...
    def onGenericMotionEvent(self, p0: MotionEvent) -> bool: ...
    def onKeyDown(self, p0: int, p1: KeyEvent) -> bool: ...
    def onKeyLongPress(self, p0: int, p1: KeyEvent) -> bool: ...
    def onKeyMultiple(self, p0: int, p1: int, p2: KeyEvent) -> bool: ...
    def onTrackballEvent(self, p0: MotionEvent) -> bool: ...
    def onConfigurationChanged(self, p0: Configuration) -> None: ...
    def getLayoutInflater(self) -> LayoutInflater: ...
    def getMaxWidth(self) -> int: ...
    def getSystemService(self, p0: str) -> Any: ...
    def setTheme(self, p0: int) -> None: ...

    class Insets:
        TOUCHABLE_INSETS_CONTENT: ClassVar[int]
        TOUCHABLE_INSETS_FRAME: ClassVar[int]
        TOUCHABLE_INSETS_REGION: ClassVar[int]
        TOUCHABLE_INSETS_VISIBLE: ClassVar[int]
        contentTopInsets: int
        touchableInsets: int
        touchableRegion: Region
        visibleTopInsets: int
        def __init__(self) -> None: ...

    class InputMethodSessionImpl:
        def __init__(self, p0: "InputMethodService") -> None: ...
        def displayCompletions(self, p0: Any) -> None: ...
        def toggleSoftInput(self, p0: int, p1: int) -> None: ...
        def updateCursor(self, p0: Rect) -> None: ...
        def updateCursorAnchorInfo(self, p0: CursorAnchorInfo) -> None: ...
        def updateExtractedText(self, p0: int, p1: ExtractedText) -> None: ...
        def updateSelection(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
        def viewClicked(self, p0: bool) -> None: ...
        def appPrivateCommand(self, p0: str, p1: Bundle) -> None: ...
        def finishInput(self) -> None: ...

    class InputMethodImpl:
        SERVICE_INTERFACE: ClassVar[str]
        SERVICE_META_DATA: ClassVar[str]
        SHOW_EXPLICIT: ClassVar[int]
        SHOW_FORCED: ClassVar[int]
        def __init__(self, p0: "InputMethodService") -> None: ...
        def restartInput(self, p0: InputConnection, p1: EditorInfo) -> None: ...
        def showSoftInput(self, p0: int, p1: ResultReceiver) -> None: ...
        def attachToken(self, p0: IBinder) -> None: ...
        def bindInput(self, p0: InputBinding) -> None: ...
        def changeInputMethodSubtype(self, p0: InputMethodSubtype) -> None: ...
        def hideSoftInput(self, p0: int, p1: ResultReceiver) -> None: ...
        def startInput(self, p0: InputConnection, p1: EditorInfo) -> None: ...
        def unbindInput(self) -> None: ...

