from typing import Any, ClassVar, overload
from android.os.IBinder import IBinder
from android.os.Looper import Looper
from android.os.Parcel import Parcel
from android.view.Choreographer import Choreographer
from android.view.Display import Display
from android.view.SurfaceControl import SurfaceControl
from android.view.SurfaceControlInputReceiver import SurfaceControlInputReceiver
from android.view.View import View
from android.view.WindowMetrics import WindowMetrics
from android.window.InputTransferToken import InputTransferToken
from android.window.TrustedPresentationThresholds import TrustedPresentationThresholds
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer
from java.util.function.IntConsumer import IntConsumer

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

class WindowManager:
    COMPAT_SMALL_COVER_SCREEN_OPT_IN: ClassVar[int]
    PROPERTY_ACTIVITY_EMBEDDING_ALLOW_SYSTEM_OVERRIDE: ClassVar[str]
    PROPERTY_ACTIVITY_EMBEDDING_SPLITS_ENABLED: ClassVar[str]
    PROPERTY_CAMERA_COMPAT_ALLOW_FORCE_ROTATION: ClassVar[str]
    PROPERTY_CAMERA_COMPAT_ALLOW_REFRESH: ClassVar[str]
    PROPERTY_CAMERA_COMPAT_ENABLE_REFRESH_VIA_PAUSE: ClassVar[str]
    PROPERTY_COMPAT_ALLOW_DISPLAY_ORIENTATION_OVERRIDE: ClassVar[str]
    PROPERTY_COMPAT_ALLOW_IGNORING_ORIENTATION_REQUEST_WHEN_LOOP_DETECTED: ClassVar[str]
    PROPERTY_COMPAT_ALLOW_MIN_ASPECT_RATIO_OVERRIDE: ClassVar[str]
    PROPERTY_COMPAT_ALLOW_ORIENTATION_OVERRIDE: ClassVar[str]
    PROPERTY_COMPAT_ALLOW_RESIZEABLE_ACTIVITY_OVERRIDES: ClassVar[str]
    PROPERTY_COMPAT_ALLOW_SANDBOXING_VIEW_BOUNDS_APIS: ClassVar[str]
    PROPERTY_COMPAT_ALLOW_SMALL_COVER_SCREEN: ClassVar[str]
    PROPERTY_COMPAT_ALLOW_USER_ASPECT_RATIO_FULLSCREEN_OVERRIDE: ClassVar[str]
    PROPERTY_COMPAT_ALLOW_USER_ASPECT_RATIO_OVERRIDE: ClassVar[str]
    PROPERTY_COMPAT_ENABLE_FAKE_FOCUS: ClassVar[str]
    PROPERTY_COMPAT_IGNORE_REQUESTED_ORIENTATION: ClassVar[str]
    PROPERTY_SUPPORTS_MULTI_INSTANCE_SYSTEM_UI: ClassVar[str]
    SCREEN_RECORDING_STATE_NOT_VISIBLE: ClassVar[int]
    SCREEN_RECORDING_STATE_VISIBLE: ClassVar[int]
    def getDefaultDisplay(self) -> Display: ...
    def removeViewImmediate(self, arg0: View) -> None: ...
    def getCurrentWindowMetrics(self) -> WindowMetrics: ...
    def getMaximumWindowMetrics(self) -> WindowMetrics: ...
    def isCrossWindowBlurEnabled(self) -> bool: ...
    @overload
    def addCrossWindowBlurEnabledListener(self, arg0: Consumer) -> None: ...
    @overload
    def addCrossWindowBlurEnabledListener(self, arg0: Executor, arg1: Consumer) -> None: ...
    def removeCrossWindowBlurEnabledListener(self, arg0: Consumer) -> None: ...
    def addProposedRotationListener(self, arg0: Executor, arg1: IntConsumer) -> None: ...
    def removeProposedRotationListener(self, arg0: IntConsumer) -> None: ...
    def registerTrustedPresentationListener(self, arg0: IBinder, arg1: TrustedPresentationThresholds, arg2: Executor, arg3: Consumer) -> None: ...
    def unregisterTrustedPresentationListener(self, arg0: Consumer) -> None: ...
    def registerBatchedSurfaceControlInputReceiver(self, arg0: InputTransferToken, arg1: SurfaceControl, arg2: Choreographer, arg3: SurfaceControlInputReceiver) -> InputTransferToken: ...
    def registerUnbatchedSurfaceControlInputReceiver(self, arg0: InputTransferToken, arg1: SurfaceControl, arg2: Looper, arg3: SurfaceControlInputReceiver) -> InputTransferToken: ...
    def unregisterSurfaceControlInputReceiver(self, arg0: SurfaceControl) -> None: ...
    def transferTouchGesture(self, arg0: InputTransferToken, arg1: InputTransferToken) -> bool: ...
    def addScreenRecordingCallback(self, arg0: Executor, arg1: Consumer) -> int: ...
    def removeScreenRecordingCallback(self, arg0: Consumer) -> None: ...

    class BadTokenException:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: str) -> None: ...

    class InvalidDisplayException:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: str) -> None: ...

    class LayoutParams:
        ALPHA_CHANGED: ClassVar[int]
        ANIMATION_CHANGED: ClassVar[int]
        BRIGHTNESS_OVERRIDE_FULL: ClassVar[float]
        BRIGHTNESS_OVERRIDE_NONE: ClassVar[float]
        BRIGHTNESS_OVERRIDE_OFF: ClassVar[float]
        CREATOR: ClassVar[Creator]
        DIM_AMOUNT_CHANGED: ClassVar[int]
        DISPLAY_FLAG_DISABLE_HDR_CONVERSION: ClassVar[int]
        FIRST_APPLICATION_WINDOW: ClassVar[int]
        FIRST_SUB_WINDOW: ClassVar[int]
        FIRST_SYSTEM_WINDOW: ClassVar[int]
        FLAGS_CHANGED: ClassVar[int]
        FLAG_ALLOW_LOCK_WHILE_SCREEN_ON: ClassVar[int]
        FLAG_ALT_FOCUSABLE_IM: ClassVar[int]
        FLAG_BLUR_BEHIND: ClassVar[int]
        FLAG_DIM_BEHIND: ClassVar[int]
        FLAG_DISMISS_KEYGUARD: ClassVar[int]
        FLAG_DITHER: ClassVar[int]
        FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS: ClassVar[int]
        FLAG_FORCE_NOT_FULLSCREEN: ClassVar[int]
        FLAG_FULLSCREEN: ClassVar[int]
        FLAG_HARDWARE_ACCELERATED: ClassVar[int]
        FLAG_IGNORE_CHEEK_PRESSES: ClassVar[int]
        FLAG_KEEP_SCREEN_ON: ClassVar[int]
        FLAG_LAYOUT_ATTACHED_IN_DECOR: ClassVar[int]
        FLAG_LAYOUT_INSET_DECOR: ClassVar[int]
        FLAG_LAYOUT_IN_OVERSCAN: ClassVar[int]
        FLAG_LAYOUT_IN_SCREEN: ClassVar[int]
        FLAG_LAYOUT_NO_LIMITS: ClassVar[int]
        FLAG_LOCAL_FOCUS_MODE: ClassVar[int]
        FLAG_NOT_FOCUSABLE: ClassVar[int]
        FLAG_NOT_TOUCHABLE: ClassVar[int]
        FLAG_NOT_TOUCH_MODAL: ClassVar[int]
        FLAG_SCALED: ClassVar[int]
        FLAG_SECURE: ClassVar[int]
        FLAG_SHOW_WALLPAPER: ClassVar[int]
        FLAG_SHOW_WHEN_LOCKED: ClassVar[int]
        FLAG_SPLIT_TOUCH: ClassVar[int]
        FLAG_TOUCHABLE_WHEN_WAKING: ClassVar[int]
        FLAG_TRANSLUCENT_NAVIGATION: ClassVar[int]
        FLAG_TRANSLUCENT_STATUS: ClassVar[int]
        FLAG_TURN_SCREEN_ON: ClassVar[int]
        FLAG_WATCH_OUTSIDE_TOUCH: ClassVar[int]
        FORMAT_CHANGED: ClassVar[int]
        LAST_APPLICATION_WINDOW: ClassVar[int]
        LAST_SUB_WINDOW: ClassVar[int]
        LAST_SYSTEM_WINDOW: ClassVar[int]
        LAYOUT_CHANGED: ClassVar[int]
        LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS: ClassVar[int]
        LAYOUT_IN_DISPLAY_CUTOUT_MODE_DEFAULT: ClassVar[int]
        LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER: ClassVar[int]
        LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES: ClassVar[int]
        MEMORY_TYPE_CHANGED: ClassVar[int]
        MEMORY_TYPE_GPU: ClassVar[int]
        MEMORY_TYPE_HARDWARE: ClassVar[int]
        MEMORY_TYPE_NORMAL: ClassVar[int]
        MEMORY_TYPE_PUSH_BUFFERS: ClassVar[int]
        ROTATION_ANIMATION_CHANGED: ClassVar[int]
        ROTATION_ANIMATION_CROSSFADE: ClassVar[int]
        ROTATION_ANIMATION_JUMPCUT: ClassVar[int]
        ROTATION_ANIMATION_ROTATE: ClassVar[int]
        ROTATION_ANIMATION_SEAMLESS: ClassVar[int]
        SCREEN_BRIGHTNESS_CHANGED: ClassVar[int]
        SCREEN_ORIENTATION_CHANGED: ClassVar[int]
        SOFT_INPUT_ADJUST_NOTHING: ClassVar[int]
        SOFT_INPUT_ADJUST_PAN: ClassVar[int]
        SOFT_INPUT_ADJUST_RESIZE: ClassVar[int]
        SOFT_INPUT_ADJUST_UNSPECIFIED: ClassVar[int]
        SOFT_INPUT_IS_FORWARD_NAVIGATION: ClassVar[int]
        SOFT_INPUT_MASK_ADJUST: ClassVar[int]
        SOFT_INPUT_MASK_STATE: ClassVar[int]
        SOFT_INPUT_MODE_CHANGED: ClassVar[int]
        SOFT_INPUT_STATE_ALWAYS_HIDDEN: ClassVar[int]
        SOFT_INPUT_STATE_ALWAYS_VISIBLE: ClassVar[int]
        SOFT_INPUT_STATE_HIDDEN: ClassVar[int]
        SOFT_INPUT_STATE_UNCHANGED: ClassVar[int]
        SOFT_INPUT_STATE_UNSPECIFIED: ClassVar[int]
        SOFT_INPUT_STATE_VISIBLE: ClassVar[int]
        TITLE_CHANGED: ClassVar[int]
        TYPE_ACCESSIBILITY_OVERLAY: ClassVar[int]
        TYPE_APPLICATION: ClassVar[int]
        TYPE_APPLICATION_ATTACHED_DIALOG: ClassVar[int]
        TYPE_APPLICATION_MEDIA: ClassVar[int]
        TYPE_APPLICATION_OVERLAY: ClassVar[int]
        TYPE_APPLICATION_PANEL: ClassVar[int]
        TYPE_APPLICATION_STARTING: ClassVar[int]
        TYPE_APPLICATION_SUB_PANEL: ClassVar[int]
        TYPE_BASE_APPLICATION: ClassVar[int]
        TYPE_CHANGED: ClassVar[int]
        TYPE_DRAWN_APPLICATION: ClassVar[int]
        TYPE_INPUT_METHOD: ClassVar[int]
        TYPE_INPUT_METHOD_DIALOG: ClassVar[int]
        TYPE_KEYGUARD_DIALOG: ClassVar[int]
        TYPE_PHONE: ClassVar[int]
        TYPE_PRIORITY_PHONE: ClassVar[int]
        TYPE_PRIVATE_PRESENTATION: ClassVar[int]
        TYPE_SEARCH_BAR: ClassVar[int]
        TYPE_STATUS_BAR: ClassVar[int]
        TYPE_SYSTEM_ALERT: ClassVar[int]
        TYPE_SYSTEM_DIALOG: ClassVar[int]
        TYPE_SYSTEM_ERROR: ClassVar[int]
        TYPE_SYSTEM_OVERLAY: ClassVar[int]
        TYPE_TOAST: ClassVar[int]
        TYPE_WALLPAPER: ClassVar[int]
        alpha: float
        buttonBrightness: float
        dimAmount: float
        flags: int
        format: int
        gravity: int
        horizontalMargin: float
        horizontalWeight: float
        layoutInDisplayCutoutMode: int
        memoryType: int
        packageName: str
        preferMinimalPostProcessing: bool
        preferredDisplayModeId: int
        preferredRefreshRate: float
        rotationAnimation: int
        screenBrightness: float
        screenOrientation: int
        softInputMode: int
        systemUiVisibility: int
        token: IBinder
        type: int
        verticalMargin: float
        verticalWeight: float
        windowAnimations: int
        x: int
        y: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: int) -> None: ...
        @overload
        def __init__(self, arg0: int, arg1: int) -> None: ...
        @overload
        def __init__(self, arg0: int, arg1: int, arg2: int) -> None: ...
        @overload
        def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
        @overload
        def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> None: ...
        @overload
        def __init__(self, arg0: Parcel) -> None: ...
        @staticmethod
        def mayUseInputMethod(arg0: int) -> bool: ...
        def setFitInsetsTypes(self, arg0: int) -> None: ...
        def setFitInsetsSides(self, arg0: int) -> None: ...
        def setFitInsetsIgnoringVisibility(self, arg0: bool) -> None: ...
        def setWallpaperTouchEventsEnabled(self, arg0: bool) -> None: ...
        def areWallpaperTouchEventsEnabled(self) -> bool: ...
        def setCanPlayMoveAnimation(self, arg0: bool) -> None: ...
        def canPlayMoveAnimation(self) -> bool: ...
        def getFitInsetsTypes(self) -> int: ...
        def getFitInsetsSides(self) -> int: ...
        def isFitInsetsIgnoringVisibility(self) -> bool: ...
        def setTitle(self, arg0: str) -> None: ...
        def getTitle(self) -> str: ...
        def isHdrConversionEnabled(self) -> bool: ...
        def setHdrConversionEnabled(self, arg0: bool) -> None: ...
        def setColorMode(self, arg0: int) -> None: ...
        def getColorMode(self) -> int: ...
        def setDesiredHdrHeadroom(self, arg0: float) -> None: ...
        def getDesiredHdrHeadroom(self) -> float: ...
        def setFrameRateBoostOnTouchEnabled(self, arg0: bool) -> None: ...
        def getFrameRateBoostOnTouchEnabled(self) -> bool: ...
        def setFrameRatePowerSavingsBalanced(self, arg0: bool) -> None: ...
        def isFrameRatePowerSavingsBalanced(self) -> bool: ...
        def setBlurBehindRadius(self, arg0: int) -> None: ...
        def getBlurBehindRadius(self) -> int: ...
        def describeContents(self) -> int: ...
        def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
        def copyFrom(self, arg0: "LayoutParams") -> int: ...
        def debug(self, arg0: str) -> str: ...
        def toString(self) -> str: ...
