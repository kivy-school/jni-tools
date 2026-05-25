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
    def removeViewImmediate(self, p0: View) -> None: ...
    def getCurrentWindowMetrics(self) -> WindowMetrics: ...
    def getMaximumWindowMetrics(self) -> WindowMetrics: ...
    def isCrossWindowBlurEnabled(self) -> bool: ...
    @overload
    def addCrossWindowBlurEnabledListener(self, p0: Executor, p1: Consumer) -> None: ...
    @overload
    def addCrossWindowBlurEnabledListener(self, p0: Consumer) -> None: ...
    def removeCrossWindowBlurEnabledListener(self, p0: Consumer) -> None: ...
    def addProposedRotationListener(self, p0: Executor, p1: IntConsumer) -> None: ...
    def removeProposedRotationListener(self, p0: IntConsumer) -> None: ...
    def registerTrustedPresentationListener(self, p0: IBinder, p1: TrustedPresentationThresholds, p2: Executor, p3: Consumer) -> None: ...
    def unregisterTrustedPresentationListener(self, p0: Consumer) -> None: ...
    def registerBatchedSurfaceControlInputReceiver(self, p0: InputTransferToken, p1: SurfaceControl, p2: Choreographer, p3: SurfaceControlInputReceiver) -> InputTransferToken: ...
    def registerUnbatchedSurfaceControlInputReceiver(self, p0: InputTransferToken, p1: SurfaceControl, p2: Looper, p3: SurfaceControlInputReceiver) -> InputTransferToken: ...
    def unregisterSurfaceControlInputReceiver(self, p0: SurfaceControl) -> None: ...
    def transferTouchGesture(self, p0: InputTransferToken, p1: InputTransferToken) -> bool: ...
    def addScreenRecordingCallback(self, p0: Executor, p1: Consumer) -> int: ...
    def removeScreenRecordingCallback(self, p0: Consumer) -> None: ...

    class LayoutParams:
        ALPHA_CHANGED: ClassVar[int]
        ANIMATION_CHANGED: ClassVar[int]
        BRIGHTNESS_OVERRIDE_FULL: ClassVar[float]
        BRIGHTNESS_OVERRIDE_NONE: ClassVar[float]
        BRIGHTNESS_OVERRIDE_OFF: ClassVar[float]
        CREATOR: ClassVar[Any]
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
        CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
        PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
        FILL_PARENT: ClassVar[int]
        MATCH_PARENT: ClassVar[int]
        WRAP_CONTENT: ClassVar[int]
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
        height: int
        layoutAnimationParameters: Any
        width: int
        @overload
        def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
        @overload
        def __init__(self, p0: int, p1: int, p2: int) -> None: ...
        @overload
        def __init__(self, p0: int, p1: int) -> None: ...
        @overload
        def __init__(self, p0: int) -> None: ...
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, p0: Parcel) -> None: ...
        @overload
        def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int) -> None: ...
        @staticmethod
        def mayUseInputMethod(p0: int) -> bool: ...
        def setFitInsetsTypes(self, p0: int) -> None: ...
        def setFitInsetsSides(self, p0: int) -> None: ...
        def setFitInsetsIgnoringVisibility(self, p0: bool) -> None: ...
        def setWallpaperTouchEventsEnabled(self, p0: bool) -> None: ...
        def areWallpaperTouchEventsEnabled(self) -> bool: ...
        def setCanPlayMoveAnimation(self, p0: bool) -> None: ...
        def canPlayMoveAnimation(self) -> bool: ...
        def getFitInsetsTypes(self) -> int: ...
        def getFitInsetsSides(self) -> int: ...
        def isFitInsetsIgnoringVisibility(self) -> bool: ...
        def isHdrConversionEnabled(self) -> bool: ...
        def setHdrConversionEnabled(self, p0: bool) -> None: ...
        def setBlurBehindRadius(self, p0: int) -> None: ...
        def getBlurBehindRadius(self) -> int: ...
        def setColorMode(self, p0: int) -> None: ...
        def getDesiredHdrHeadroom(self) -> float: ...
        def setFrameRateBoostOnTouchEnabled(self, p0: bool) -> None: ...
        def getFrameRateBoostOnTouchEnabled(self) -> bool: ...
        def setFrameRatePowerSavingsBalanced(self, p0: bool) -> None: ...
        def isFrameRatePowerSavingsBalanced(self) -> bool: ...
        def getColorMode(self) -> int: ...
        def describeContents(self) -> int: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
        def getTitle(self) -> str: ...
        def setTitle(self, p0: str) -> None: ...
        def copyFrom(self, p0: Any) -> int: ...
        def setDesiredHdrHeadroom(self, p0: float) -> None: ...
        def toString(self) -> str: ...
        def debug(self, p0: str) -> str: ...

    class InvalidDisplayException:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, p0: str) -> None: ...

    class BadTokenException:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, p0: str) -> None: ...
