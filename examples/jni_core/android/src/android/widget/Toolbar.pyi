from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.graphics.drawable.Drawable import Drawable
from android.util.AttributeSet import AttributeSet
from android.util.Property import Property
from android.view.Menu import Menu
from android.view.MenuItem import MenuItem
from android.view.MotionEvent import MotionEvent

class Toolbar:
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
    def __init__(self, p0: Context, p1: AttributeSet, p2: int, p3: int) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: AttributeSet, p2: int) -> None: ...
    def onTouchEvent(self, p0: MotionEvent) -> bool: ...
    def onRtlPropertiesChanged(self, p0: int) -> None: ...
    def setPopupTheme(self, p0: int) -> None: ...
    def getPopupTheme(self) -> int: ...
    def setTitleMargin(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
    def getTitleMarginStart(self) -> int: ...
    def setTitleMarginStart(self, p0: int) -> None: ...
    def getTitleMarginTop(self) -> int: ...
    def setTitleMarginTop(self, p0: int) -> None: ...
    def getTitleMarginEnd(self) -> int: ...
    def setTitleMarginEnd(self, p0: int) -> None: ...
    def getTitleMarginBottom(self) -> int: ...
    def setTitleMarginBottom(self, p0: int) -> None: ...
    @overload
    def setLogo(self, p0: int) -> None: ...
    @overload
    def setLogo(self, p0: Drawable) -> None: ...
    def isOverflowMenuShowing(self) -> bool: ...
    def showOverflowMenu(self) -> bool: ...
    def hideOverflowMenu(self) -> bool: ...
    def dismissPopupMenus(self) -> None: ...
    def getLogo(self) -> Drawable: ...
    @overload
    def setLogoDescription(self, p0: int) -> None: ...
    @overload
    def setLogoDescription(self, p0: str) -> None: ...
    def getLogoDescription(self) -> str: ...
    def hasExpandedActionView(self) -> bool: ...
    def collapseActionView(self) -> None: ...
    def getTitle(self) -> str: ...
    @overload
    def setTitle(self, p0: str) -> None: ...
    @overload
    def setTitle(self, p0: int) -> None: ...
    def getSubtitle(self) -> str: ...
    @overload
    def setSubtitle(self, p0: int) -> None: ...
    @overload
    def setSubtitle(self, p0: str) -> None: ...
    def setTitleTextAppearance(self, p0: Context, p1: int) -> None: ...
    def setSubtitleTextAppearance(self, p0: Context, p1: int) -> None: ...
    def setTitleTextColor(self, p0: int) -> None: ...
    def setSubtitleTextColor(self, p0: int) -> None: ...
    def getNavigationContentDescription(self) -> str: ...
    @overload
    def setNavigationContentDescription(self, p0: int) -> None: ...
    @overload
    def setNavigationContentDescription(self, p0: str) -> None: ...
    @overload
    def setNavigationIcon(self, p0: int) -> None: ...
    @overload
    def setNavigationIcon(self, p0: Drawable) -> None: ...
    def getNavigationIcon(self) -> Drawable: ...
    def setNavigationOnClickListener(self, p0: Any) -> None: ...
    def getCollapseContentDescription(self) -> str: ...
    @overload
    def setCollapseContentDescription(self, p0: str) -> None: ...
    @overload
    def setCollapseContentDescription(self, p0: int) -> None: ...
    def getCollapseIcon(self) -> Drawable: ...
    @overload
    def setCollapseIcon(self, p0: int) -> None: ...
    @overload
    def setCollapseIcon(self, p0: Drawable) -> None: ...
    def getMenu(self) -> Menu: ...
    def setOverflowIcon(self, p0: Drawable) -> None: ...
    def getOverflowIcon(self) -> Drawable: ...
    def inflateMenu(self, p0: int) -> None: ...
    def setOnMenuItemClickListener(self, p0: Any) -> None: ...
    def setContentInsetsRelative(self, p0: int, p1: int) -> None: ...
    def getContentInsetStart(self) -> int: ...
    def getContentInsetEnd(self) -> int: ...
    def setContentInsetsAbsolute(self, p0: int, p1: int) -> None: ...
    def getContentInsetLeft(self) -> int: ...
    def getContentInsetRight(self) -> int: ...
    def getContentInsetStartWithNavigation(self) -> int: ...
    def setContentInsetStartWithNavigation(self, p0: int) -> None: ...
    def getContentInsetEndWithActions(self) -> int: ...
    def setContentInsetEndWithActions(self, p0: int) -> None: ...
    def getCurrentContentInsetStart(self) -> int: ...
    def getCurrentContentInsetEnd(self) -> int: ...
    def getCurrentContentInsetLeft(self) -> int: ...
    def getCurrentContentInsetRight(self) -> int: ...
    @overload
    def generateLayoutParams(self, p0: AttributeSet) -> Any: ...
    @overload
    def generateLayoutParams(self, p0: AttributeSet) -> Any: ...

    class LayoutParams:
        FILL_PARENT: ClassVar[int]
        MATCH_PARENT: ClassVar[int]
        WRAP_CONTENT: ClassVar[int]
        gravity: int
        bottomMargin: int
        leftMargin: int
        rightMargin: int
        topMargin: int
        height: int
        layoutAnimationParameters: Any
        width: int
        @overload
        def __init__(self, p0: Any) -> None: ...
        @overload
        def __init__(self, p0: Any) -> None: ...
        @overload
        def __init__(self, p0: Any) -> None: ...
        @overload
        def __init__(self, p0: Any) -> None: ...
        @overload
        def __init__(self, p0: Context, p1: AttributeSet) -> None: ...
        @overload
        def __init__(self, p0: int, p1: int) -> None: ...
        @overload
        def __init__(self, p0: int, p1: int, p2: int) -> None: ...
        @overload
        def __init__(self, p0: int) -> None: ...

    class OnMenuItemClickListener:
        def onMenuItemClick(self, p0: MenuItem) -> bool: ...
