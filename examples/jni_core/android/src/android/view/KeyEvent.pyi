from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.view.KeyCharacterMap import KeyCharacterMap

class KeyEvent:
    ACTION_DOWN: ClassVar[int]
    ACTION_MULTIPLE: ClassVar[int]
    ACTION_UP: ClassVar[int]
    CREATOR: ClassVar[Any]
    FLAG_CANCELED: ClassVar[int]
    FLAG_CANCELED_LONG_PRESS: ClassVar[int]
    FLAG_EDITOR_ACTION: ClassVar[int]
    FLAG_FALLBACK: ClassVar[int]
    FLAG_FROM_SYSTEM: ClassVar[int]
    FLAG_KEEP_TOUCH_MODE: ClassVar[int]
    FLAG_LONG_PRESS: ClassVar[int]
    FLAG_SOFT_KEYBOARD: ClassVar[int]
    FLAG_TRACKING: ClassVar[int]
    FLAG_VIRTUAL_HARD_KEY: ClassVar[int]
    FLAG_WOKE_HERE: ClassVar[int]
    KEYCODE_0: ClassVar[int]
    KEYCODE_1: ClassVar[int]
    KEYCODE_11: ClassVar[int]
    KEYCODE_12: ClassVar[int]
    KEYCODE_2: ClassVar[int]
    KEYCODE_3: ClassVar[int]
    KEYCODE_3D_MODE: ClassVar[int]
    KEYCODE_4: ClassVar[int]
    KEYCODE_5: ClassVar[int]
    KEYCODE_6: ClassVar[int]
    KEYCODE_7: ClassVar[int]
    KEYCODE_8: ClassVar[int]
    KEYCODE_9: ClassVar[int]
    KEYCODE_A: ClassVar[int]
    KEYCODE_ALL_APPS: ClassVar[int]
    KEYCODE_ALT_LEFT: ClassVar[int]
    KEYCODE_ALT_RIGHT: ClassVar[int]
    KEYCODE_APOSTROPHE: ClassVar[int]
    KEYCODE_APP_SWITCH: ClassVar[int]
    KEYCODE_ASSIST: ClassVar[int]
    KEYCODE_AT: ClassVar[int]
    KEYCODE_AVR_INPUT: ClassVar[int]
    KEYCODE_AVR_POWER: ClassVar[int]
    KEYCODE_B: ClassVar[int]
    KEYCODE_BACK: ClassVar[int]
    KEYCODE_BACKSLASH: ClassVar[int]
    KEYCODE_BOOKMARK: ClassVar[int]
    KEYCODE_BREAK: ClassVar[int]
    KEYCODE_BRIGHTNESS_DOWN: ClassVar[int]
    KEYCODE_BRIGHTNESS_UP: ClassVar[int]
    KEYCODE_BUTTON_1: ClassVar[int]
    KEYCODE_BUTTON_10: ClassVar[int]
    KEYCODE_BUTTON_11: ClassVar[int]
    KEYCODE_BUTTON_12: ClassVar[int]
    KEYCODE_BUTTON_13: ClassVar[int]
    KEYCODE_BUTTON_14: ClassVar[int]
    KEYCODE_BUTTON_15: ClassVar[int]
    KEYCODE_BUTTON_16: ClassVar[int]
    KEYCODE_BUTTON_2: ClassVar[int]
    KEYCODE_BUTTON_3: ClassVar[int]
    KEYCODE_BUTTON_4: ClassVar[int]
    KEYCODE_BUTTON_5: ClassVar[int]
    KEYCODE_BUTTON_6: ClassVar[int]
    KEYCODE_BUTTON_7: ClassVar[int]
    KEYCODE_BUTTON_8: ClassVar[int]
    KEYCODE_BUTTON_9: ClassVar[int]
    KEYCODE_BUTTON_A: ClassVar[int]
    KEYCODE_BUTTON_B: ClassVar[int]
    KEYCODE_BUTTON_C: ClassVar[int]
    KEYCODE_BUTTON_L1: ClassVar[int]
    KEYCODE_BUTTON_L2: ClassVar[int]
    KEYCODE_BUTTON_MODE: ClassVar[int]
    KEYCODE_BUTTON_R1: ClassVar[int]
    KEYCODE_BUTTON_R2: ClassVar[int]
    KEYCODE_BUTTON_SELECT: ClassVar[int]
    KEYCODE_BUTTON_START: ClassVar[int]
    KEYCODE_BUTTON_THUMBL: ClassVar[int]
    KEYCODE_BUTTON_THUMBR: ClassVar[int]
    KEYCODE_BUTTON_X: ClassVar[int]
    KEYCODE_BUTTON_Y: ClassVar[int]
    KEYCODE_BUTTON_Z: ClassVar[int]
    KEYCODE_C: ClassVar[int]
    KEYCODE_CALCULATOR: ClassVar[int]
    KEYCODE_CALENDAR: ClassVar[int]
    KEYCODE_CALL: ClassVar[int]
    KEYCODE_CAMERA: ClassVar[int]
    KEYCODE_CAPS_LOCK: ClassVar[int]
    KEYCODE_CAPTIONS: ClassVar[int]
    KEYCODE_CHANNEL_DOWN: ClassVar[int]
    KEYCODE_CHANNEL_UP: ClassVar[int]
    KEYCODE_CLEAR: ClassVar[int]
    KEYCODE_COMMA: ClassVar[int]
    KEYCODE_CONTACTS: ClassVar[int]
    KEYCODE_COPY: ClassVar[int]
    KEYCODE_CTRL_LEFT: ClassVar[int]
    KEYCODE_CTRL_RIGHT: ClassVar[int]
    KEYCODE_CUT: ClassVar[int]
    KEYCODE_D: ClassVar[int]
    KEYCODE_DEL: ClassVar[int]
    KEYCODE_DEMO_APP_1: ClassVar[int]
    KEYCODE_DEMO_APP_2: ClassVar[int]
    KEYCODE_DEMO_APP_3: ClassVar[int]
    KEYCODE_DEMO_APP_4: ClassVar[int]
    KEYCODE_DPAD_CENTER: ClassVar[int]
    KEYCODE_DPAD_DOWN: ClassVar[int]
    KEYCODE_DPAD_DOWN_LEFT: ClassVar[int]
    KEYCODE_DPAD_DOWN_RIGHT: ClassVar[int]
    KEYCODE_DPAD_LEFT: ClassVar[int]
    KEYCODE_DPAD_RIGHT: ClassVar[int]
    KEYCODE_DPAD_UP: ClassVar[int]
    KEYCODE_DPAD_UP_LEFT: ClassVar[int]
    KEYCODE_DPAD_UP_RIGHT: ClassVar[int]
    KEYCODE_DVR: ClassVar[int]
    KEYCODE_E: ClassVar[int]
    KEYCODE_EISU: ClassVar[int]
    KEYCODE_EMOJI_PICKER: ClassVar[int]
    KEYCODE_ENDCALL: ClassVar[int]
    KEYCODE_ENTER: ClassVar[int]
    KEYCODE_ENVELOPE: ClassVar[int]
    KEYCODE_EQUALS: ClassVar[int]
    KEYCODE_ESCAPE: ClassVar[int]
    KEYCODE_EXPLORER: ClassVar[int]
    KEYCODE_F: ClassVar[int]
    KEYCODE_F1: ClassVar[int]
    KEYCODE_F10: ClassVar[int]
    KEYCODE_F11: ClassVar[int]
    KEYCODE_F12: ClassVar[int]
    KEYCODE_F2: ClassVar[int]
    KEYCODE_F3: ClassVar[int]
    KEYCODE_F4: ClassVar[int]
    KEYCODE_F5: ClassVar[int]
    KEYCODE_F6: ClassVar[int]
    KEYCODE_F7: ClassVar[int]
    KEYCODE_F8: ClassVar[int]
    KEYCODE_F9: ClassVar[int]
    KEYCODE_FEATURED_APP_1: ClassVar[int]
    KEYCODE_FEATURED_APP_2: ClassVar[int]
    KEYCODE_FEATURED_APP_3: ClassVar[int]
    KEYCODE_FEATURED_APP_4: ClassVar[int]
    KEYCODE_FOCUS: ClassVar[int]
    KEYCODE_FORWARD: ClassVar[int]
    KEYCODE_FORWARD_DEL: ClassVar[int]
    KEYCODE_FUNCTION: ClassVar[int]
    KEYCODE_G: ClassVar[int]
    KEYCODE_GRAVE: ClassVar[int]
    KEYCODE_GUIDE: ClassVar[int]
    KEYCODE_H: ClassVar[int]
    KEYCODE_HEADSETHOOK: ClassVar[int]
    KEYCODE_HELP: ClassVar[int]
    KEYCODE_HENKAN: ClassVar[int]
    KEYCODE_HOME: ClassVar[int]
    KEYCODE_I: ClassVar[int]
    KEYCODE_INFO: ClassVar[int]
    KEYCODE_INSERT: ClassVar[int]
    KEYCODE_J: ClassVar[int]
    KEYCODE_K: ClassVar[int]
    KEYCODE_KANA: ClassVar[int]
    KEYCODE_KATAKANA_HIRAGANA: ClassVar[int]
    KEYCODE_KEYBOARD_BACKLIGHT_DOWN: ClassVar[int]
    KEYCODE_KEYBOARD_BACKLIGHT_TOGGLE: ClassVar[int]
    KEYCODE_KEYBOARD_BACKLIGHT_UP: ClassVar[int]
    KEYCODE_L: ClassVar[int]
    KEYCODE_LANGUAGE_SWITCH: ClassVar[int]
    KEYCODE_LAST_CHANNEL: ClassVar[int]
    KEYCODE_LEFT_BRACKET: ClassVar[int]
    KEYCODE_M: ClassVar[int]
    KEYCODE_MACRO_1: ClassVar[int]
    KEYCODE_MACRO_2: ClassVar[int]
    KEYCODE_MACRO_3: ClassVar[int]
    KEYCODE_MACRO_4: ClassVar[int]
    KEYCODE_MANNER_MODE: ClassVar[int]
    KEYCODE_MEDIA_AUDIO_TRACK: ClassVar[int]
    KEYCODE_MEDIA_CLOSE: ClassVar[int]
    KEYCODE_MEDIA_EJECT: ClassVar[int]
    KEYCODE_MEDIA_FAST_FORWARD: ClassVar[int]
    KEYCODE_MEDIA_NEXT: ClassVar[int]
    KEYCODE_MEDIA_PAUSE: ClassVar[int]
    KEYCODE_MEDIA_PLAY: ClassVar[int]
    KEYCODE_MEDIA_PLAY_PAUSE: ClassVar[int]
    KEYCODE_MEDIA_PREVIOUS: ClassVar[int]
    KEYCODE_MEDIA_RECORD: ClassVar[int]
    KEYCODE_MEDIA_REWIND: ClassVar[int]
    KEYCODE_MEDIA_SKIP_BACKWARD: ClassVar[int]
    KEYCODE_MEDIA_SKIP_FORWARD: ClassVar[int]
    KEYCODE_MEDIA_STEP_BACKWARD: ClassVar[int]
    KEYCODE_MEDIA_STEP_FORWARD: ClassVar[int]
    KEYCODE_MEDIA_STOP: ClassVar[int]
    KEYCODE_MEDIA_TOP_MENU: ClassVar[int]
    KEYCODE_MENU: ClassVar[int]
    KEYCODE_META_LEFT: ClassVar[int]
    KEYCODE_META_RIGHT: ClassVar[int]
    KEYCODE_MINUS: ClassVar[int]
    KEYCODE_MOVE_END: ClassVar[int]
    KEYCODE_MOVE_HOME: ClassVar[int]
    KEYCODE_MUHENKAN: ClassVar[int]
    KEYCODE_MUSIC: ClassVar[int]
    KEYCODE_MUTE: ClassVar[int]
    KEYCODE_N: ClassVar[int]
    KEYCODE_NAVIGATE_IN: ClassVar[int]
    KEYCODE_NAVIGATE_NEXT: ClassVar[int]
    KEYCODE_NAVIGATE_OUT: ClassVar[int]
    KEYCODE_NAVIGATE_PREVIOUS: ClassVar[int]
    KEYCODE_NOTIFICATION: ClassVar[int]
    KEYCODE_NUM: ClassVar[int]
    KEYCODE_NUMPAD_0: ClassVar[int]
    KEYCODE_NUMPAD_1: ClassVar[int]
    KEYCODE_NUMPAD_2: ClassVar[int]
    KEYCODE_NUMPAD_3: ClassVar[int]
    KEYCODE_NUMPAD_4: ClassVar[int]
    KEYCODE_NUMPAD_5: ClassVar[int]
    KEYCODE_NUMPAD_6: ClassVar[int]
    KEYCODE_NUMPAD_7: ClassVar[int]
    KEYCODE_NUMPAD_8: ClassVar[int]
    KEYCODE_NUMPAD_9: ClassVar[int]
    KEYCODE_NUMPAD_ADD: ClassVar[int]
    KEYCODE_NUMPAD_COMMA: ClassVar[int]
    KEYCODE_NUMPAD_DIVIDE: ClassVar[int]
    KEYCODE_NUMPAD_DOT: ClassVar[int]
    KEYCODE_NUMPAD_ENTER: ClassVar[int]
    KEYCODE_NUMPAD_EQUALS: ClassVar[int]
    KEYCODE_NUMPAD_LEFT_PAREN: ClassVar[int]
    KEYCODE_NUMPAD_MULTIPLY: ClassVar[int]
    KEYCODE_NUMPAD_RIGHT_PAREN: ClassVar[int]
    KEYCODE_NUMPAD_SUBTRACT: ClassVar[int]
    KEYCODE_NUM_LOCK: ClassVar[int]
    KEYCODE_O: ClassVar[int]
    KEYCODE_P: ClassVar[int]
    KEYCODE_PAGE_DOWN: ClassVar[int]
    KEYCODE_PAGE_UP: ClassVar[int]
    KEYCODE_PAIRING: ClassVar[int]
    KEYCODE_PASTE: ClassVar[int]
    KEYCODE_PERIOD: ClassVar[int]
    KEYCODE_PICTSYMBOLS: ClassVar[int]
    KEYCODE_PLUS: ClassVar[int]
    KEYCODE_POUND: ClassVar[int]
    KEYCODE_POWER: ClassVar[int]
    KEYCODE_PROFILE_SWITCH: ClassVar[int]
    KEYCODE_PROG_BLUE: ClassVar[int]
    KEYCODE_PROG_GREEN: ClassVar[int]
    KEYCODE_PROG_RED: ClassVar[int]
    KEYCODE_PROG_YELLOW: ClassVar[int]
    KEYCODE_Q: ClassVar[int]
    KEYCODE_R: ClassVar[int]
    KEYCODE_RECENT_APPS: ClassVar[int]
    KEYCODE_REFRESH: ClassVar[int]
    KEYCODE_RIGHT_BRACKET: ClassVar[int]
    KEYCODE_RO: ClassVar[int]
    KEYCODE_S: ClassVar[int]
    KEYCODE_SCREENSHOT: ClassVar[int]
    KEYCODE_SCROLL_LOCK: ClassVar[int]
    KEYCODE_SEARCH: ClassVar[int]
    KEYCODE_SEMICOLON: ClassVar[int]
    KEYCODE_SETTINGS: ClassVar[int]
    KEYCODE_SHIFT_LEFT: ClassVar[int]
    KEYCODE_SHIFT_RIGHT: ClassVar[int]
    KEYCODE_SLASH: ClassVar[int]
    KEYCODE_SLEEP: ClassVar[int]
    KEYCODE_SOFT_LEFT: ClassVar[int]
    KEYCODE_SOFT_RIGHT: ClassVar[int]
    KEYCODE_SOFT_SLEEP: ClassVar[int]
    KEYCODE_SPACE: ClassVar[int]
    KEYCODE_STAR: ClassVar[int]
    KEYCODE_STB_INPUT: ClassVar[int]
    KEYCODE_STB_POWER: ClassVar[int]
    KEYCODE_STEM_1: ClassVar[int]
    KEYCODE_STEM_2: ClassVar[int]
    KEYCODE_STEM_3: ClassVar[int]
    KEYCODE_STEM_PRIMARY: ClassVar[int]
    KEYCODE_STYLUS_BUTTON_PRIMARY: ClassVar[int]
    KEYCODE_STYLUS_BUTTON_SECONDARY: ClassVar[int]
    KEYCODE_STYLUS_BUTTON_TAIL: ClassVar[int]
    KEYCODE_STYLUS_BUTTON_TERTIARY: ClassVar[int]
    KEYCODE_SWITCH_CHARSET: ClassVar[int]
    KEYCODE_SYM: ClassVar[int]
    KEYCODE_SYSRQ: ClassVar[int]
    KEYCODE_SYSTEM_NAVIGATION_DOWN: ClassVar[int]
    KEYCODE_SYSTEM_NAVIGATION_LEFT: ClassVar[int]
    KEYCODE_SYSTEM_NAVIGATION_RIGHT: ClassVar[int]
    KEYCODE_SYSTEM_NAVIGATION_UP: ClassVar[int]
    KEYCODE_T: ClassVar[int]
    KEYCODE_TAB: ClassVar[int]
    KEYCODE_THUMBS_DOWN: ClassVar[int]
    KEYCODE_THUMBS_UP: ClassVar[int]
    KEYCODE_TV: ClassVar[int]
    KEYCODE_TV_ANTENNA_CABLE: ClassVar[int]
    KEYCODE_TV_AUDIO_DESCRIPTION: ClassVar[int]
    KEYCODE_TV_AUDIO_DESCRIPTION_MIX_DOWN: ClassVar[int]
    KEYCODE_TV_AUDIO_DESCRIPTION_MIX_UP: ClassVar[int]
    KEYCODE_TV_CONTENTS_MENU: ClassVar[int]
    KEYCODE_TV_DATA_SERVICE: ClassVar[int]
    KEYCODE_TV_INPUT: ClassVar[int]
    KEYCODE_TV_INPUT_COMPONENT_1: ClassVar[int]
    KEYCODE_TV_INPUT_COMPONENT_2: ClassVar[int]
    KEYCODE_TV_INPUT_COMPOSITE_1: ClassVar[int]
    KEYCODE_TV_INPUT_COMPOSITE_2: ClassVar[int]
    KEYCODE_TV_INPUT_HDMI_1: ClassVar[int]
    KEYCODE_TV_INPUT_HDMI_2: ClassVar[int]
    KEYCODE_TV_INPUT_HDMI_3: ClassVar[int]
    KEYCODE_TV_INPUT_HDMI_4: ClassVar[int]
    KEYCODE_TV_INPUT_VGA_1: ClassVar[int]
    KEYCODE_TV_MEDIA_CONTEXT_MENU: ClassVar[int]
    KEYCODE_TV_NETWORK: ClassVar[int]
    KEYCODE_TV_NUMBER_ENTRY: ClassVar[int]
    KEYCODE_TV_POWER: ClassVar[int]
    KEYCODE_TV_RADIO_SERVICE: ClassVar[int]
    KEYCODE_TV_SATELLITE: ClassVar[int]
    KEYCODE_TV_SATELLITE_BS: ClassVar[int]
    KEYCODE_TV_SATELLITE_CS: ClassVar[int]
    KEYCODE_TV_SATELLITE_SERVICE: ClassVar[int]
    KEYCODE_TV_TELETEXT: ClassVar[int]
    KEYCODE_TV_TERRESTRIAL_ANALOG: ClassVar[int]
    KEYCODE_TV_TERRESTRIAL_DIGITAL: ClassVar[int]
    KEYCODE_TV_TIMER_PROGRAMMING: ClassVar[int]
    KEYCODE_TV_ZOOM_MODE: ClassVar[int]
    KEYCODE_U: ClassVar[int]
    KEYCODE_UNKNOWN: ClassVar[int]
    KEYCODE_V: ClassVar[int]
    KEYCODE_VIDEO_APP_1: ClassVar[int]
    KEYCODE_VIDEO_APP_2: ClassVar[int]
    KEYCODE_VIDEO_APP_3: ClassVar[int]
    KEYCODE_VIDEO_APP_4: ClassVar[int]
    KEYCODE_VIDEO_APP_5: ClassVar[int]
    KEYCODE_VIDEO_APP_6: ClassVar[int]
    KEYCODE_VIDEO_APP_7: ClassVar[int]
    KEYCODE_VIDEO_APP_8: ClassVar[int]
    KEYCODE_VOICE_ASSIST: ClassVar[int]
    KEYCODE_VOLUME_DOWN: ClassVar[int]
    KEYCODE_VOLUME_MUTE: ClassVar[int]
    KEYCODE_VOLUME_UP: ClassVar[int]
    KEYCODE_W: ClassVar[int]
    KEYCODE_WAKEUP: ClassVar[int]
    KEYCODE_WINDOW: ClassVar[int]
    KEYCODE_X: ClassVar[int]
    KEYCODE_Y: ClassVar[int]
    KEYCODE_YEN: ClassVar[int]
    KEYCODE_Z: ClassVar[int]
    KEYCODE_ZENKAKU_HANKAKU: ClassVar[int]
    KEYCODE_ZOOM_IN: ClassVar[int]
    KEYCODE_ZOOM_OUT: ClassVar[int]
    MAX_KEYCODE: ClassVar[int]
    META_ALT_LEFT_ON: ClassVar[int]
    META_ALT_MASK: ClassVar[int]
    META_ALT_ON: ClassVar[int]
    META_ALT_RIGHT_ON: ClassVar[int]
    META_CAPS_LOCK_ON: ClassVar[int]
    META_CTRL_LEFT_ON: ClassVar[int]
    META_CTRL_MASK: ClassVar[int]
    META_CTRL_ON: ClassVar[int]
    META_CTRL_RIGHT_ON: ClassVar[int]
    META_FUNCTION_ON: ClassVar[int]
    META_META_LEFT_ON: ClassVar[int]
    META_META_MASK: ClassVar[int]
    META_META_ON: ClassVar[int]
    META_META_RIGHT_ON: ClassVar[int]
    META_NUM_LOCK_ON: ClassVar[int]
    META_SCROLL_LOCK_ON: ClassVar[int]
    META_SHIFT_LEFT_ON: ClassVar[int]
    META_SHIFT_MASK: ClassVar[int]
    META_SHIFT_ON: ClassVar[int]
    META_SHIFT_RIGHT_ON: ClassVar[int]
    META_SYM_ON: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    @overload
    def __init__(self, p0: int, p1: str, p2: int, p3: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    def __init__(self, p0: "KeyEvent", p1: int, p2: int) -> None: ...
    @overload
    def __init__(self, p0: "KeyEvent") -> None: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getSource(self) -> int: ...
    def setSource(self, p0: int) -> None: ...
    def getDownTime(self) -> int: ...
    def getEventTime(self) -> int: ...
    def getMetaState(self) -> int: ...
    @staticmethod
    def getMaxKeyCode() -> int: ...
    @staticmethod
    def getDeadChar(p0: int, p1: int) -> int: ...
    @overload
    @staticmethod
    def changeTimeRepeat(p0: "KeyEvent", p1: int, p2: int, p3: int) -> "KeyEvent": ...
    @overload
    @staticmethod
    def changeTimeRepeat(p0: "KeyEvent", p1: int, p2: int) -> "KeyEvent": ...
    @staticmethod
    def changeAction(p0: "KeyEvent", p1: int) -> "KeyEvent": ...
    @staticmethod
    def changeFlags(p0: "KeyEvent", p1: int) -> "KeyEvent": ...
    def isSystem(self) -> bool: ...
    @staticmethod
    def isGamepadButton(p0: int) -> bool: ...
    @staticmethod
    def isMediaSessionKey(p0: int) -> bool: ...
    @staticmethod
    def getModifierMetaStateMask() -> int: ...
    @staticmethod
    def isModifierKey(p0: int) -> bool: ...
    @staticmethod
    def normalizeMetaState(p0: int) -> int: ...
    @staticmethod
    def metaStateHasNoModifiers(p0: int) -> bool: ...
    @staticmethod
    def metaStateHasModifiers(p0: int, p1: int) -> bool: ...
    def hasNoModifiers(self) -> bool: ...
    def hasModifiers(self, p0: int) -> bool: ...
    def isAltPressed(self) -> bool: ...
    def isShiftPressed(self) -> bool: ...
    def isSymPressed(self) -> bool: ...
    def isCtrlPressed(self) -> bool: ...
    def isMetaPressed(self) -> bool: ...
    def isFunctionPressed(self) -> bool: ...
    def isCapsLockOn(self) -> bool: ...
    def isNumLockOn(self) -> bool: ...
    def isScrollLockOn(self) -> bool: ...
    def isCanceled(self) -> bool: ...
    def startTracking(self) -> None: ...
    def isTracking(self) -> bool: ...
    def isLongPress(self) -> bool: ...
    def getKeyCode(self) -> int: ...
    def getCharacters(self) -> str: ...
    def getScanCode(self) -> int: ...
    def getRepeatCount(self) -> int: ...
    def getKeyCharacterMap(self) -> KeyCharacterMap: ...
    def getDisplayLabel(self) -> str: ...
    @overload
    def getUnicodeChar(self, p0: int) -> int: ...
    @overload
    def getUnicodeChar(self) -> int: ...
    def getKeyData(self, p0: Any) -> bool: ...
    @overload
    def getMatch(self, p0: Any, p1: int) -> str: ...
    @overload
    def getMatch(self, p0: Any) -> str: ...
    def isPrintingKey(self) -> bool: ...
    @staticmethod
    def keyCodeToString(p0: int) -> str: ...
    @staticmethod
    def keyCodeFromString(p0: str) -> int: ...
    def getDeviceId(self) -> int: ...
    def getAction(self) -> int: ...
    def getFlags(self) -> int: ...
    def getNumber(self) -> str: ...
    @overload
    def dispatch(self, p0: Any) -> bool: ...
    @overload
    def dispatch(self, p0: Any, p1: Any, p2: Any) -> bool: ...
    def toString(self) -> str: ...
    def getModifiers(self) -> int: ...

    class DispatcherState:
        def __init__(self) -> None: ...
        def handleUpEvent(self, p0: "KeyEvent") -> None: ...
        def performedLongPress(self, p0: "KeyEvent") -> None: ...
        def startTracking(self, p0: "KeyEvent", p1: Any) -> None: ...
        def isTracking(self, p0: "KeyEvent") -> bool: ...
        @overload
        def reset(self, p0: Any) -> None: ...
        @overload
        def reset(self) -> None: ...

    class Callback:
        def onKeyDown(self, p0: int, p1: "KeyEvent") -> bool: ...
        def onKeyLongPress(self, p0: int, p1: "KeyEvent") -> bool: ...
        def onKeyMultiple(self, p0: int, p1: int, p2: "KeyEvent") -> bool: ...
        def onKeyUp(self, p0: int, p1: "KeyEvent") -> bool: ...
