from typing import Any, ClassVar, overload
from android.os.LocaleList import LocaleList
from android.os.Parcel import Parcel
from java.util.Locale import Locale

class Configuration:
    COLOR_MODE_HDR_MASK: ClassVar[int]
    COLOR_MODE_HDR_NO: ClassVar[int]
    COLOR_MODE_HDR_SHIFT: ClassVar[int]
    COLOR_MODE_HDR_UNDEFINED: ClassVar[int]
    COLOR_MODE_HDR_YES: ClassVar[int]
    COLOR_MODE_UNDEFINED: ClassVar[int]
    COLOR_MODE_WIDE_COLOR_GAMUT_MASK: ClassVar[int]
    COLOR_MODE_WIDE_COLOR_GAMUT_NO: ClassVar[int]
    COLOR_MODE_WIDE_COLOR_GAMUT_UNDEFINED: ClassVar[int]
    COLOR_MODE_WIDE_COLOR_GAMUT_YES: ClassVar[int]
    CREATOR: ClassVar[Any]
    DENSITY_DPI_UNDEFINED: ClassVar[int]
    FONT_WEIGHT_ADJUSTMENT_UNDEFINED: ClassVar[int]
    GRAMMATICAL_GENDER_FEMININE: ClassVar[int]
    GRAMMATICAL_GENDER_MASCULINE: ClassVar[int]
    GRAMMATICAL_GENDER_NEUTRAL: ClassVar[int]
    GRAMMATICAL_GENDER_NOT_SPECIFIED: ClassVar[int]
    HARDKEYBOARDHIDDEN_NO: ClassVar[int]
    HARDKEYBOARDHIDDEN_UNDEFINED: ClassVar[int]
    HARDKEYBOARDHIDDEN_YES: ClassVar[int]
    KEYBOARDHIDDEN_NO: ClassVar[int]
    KEYBOARDHIDDEN_UNDEFINED: ClassVar[int]
    KEYBOARDHIDDEN_YES: ClassVar[int]
    KEYBOARD_12KEY: ClassVar[int]
    KEYBOARD_NOKEYS: ClassVar[int]
    KEYBOARD_QWERTY: ClassVar[int]
    KEYBOARD_UNDEFINED: ClassVar[int]
    MNC_ZERO: ClassVar[int]
    NAVIGATIONHIDDEN_NO: ClassVar[int]
    NAVIGATIONHIDDEN_UNDEFINED: ClassVar[int]
    NAVIGATIONHIDDEN_YES: ClassVar[int]
    NAVIGATION_DPAD: ClassVar[int]
    NAVIGATION_NONAV: ClassVar[int]
    NAVIGATION_TRACKBALL: ClassVar[int]
    NAVIGATION_UNDEFINED: ClassVar[int]
    NAVIGATION_WHEEL: ClassVar[int]
    ORIENTATION_LANDSCAPE: ClassVar[int]
    ORIENTATION_PORTRAIT: ClassVar[int]
    ORIENTATION_SQUARE: ClassVar[int]
    ORIENTATION_UNDEFINED: ClassVar[int]
    SCREENLAYOUT_LAYOUTDIR_LTR: ClassVar[int]
    SCREENLAYOUT_LAYOUTDIR_MASK: ClassVar[int]
    SCREENLAYOUT_LAYOUTDIR_RTL: ClassVar[int]
    SCREENLAYOUT_LAYOUTDIR_SHIFT: ClassVar[int]
    SCREENLAYOUT_LAYOUTDIR_UNDEFINED: ClassVar[int]
    SCREENLAYOUT_LONG_MASK: ClassVar[int]
    SCREENLAYOUT_LONG_NO: ClassVar[int]
    SCREENLAYOUT_LONG_UNDEFINED: ClassVar[int]
    SCREENLAYOUT_LONG_YES: ClassVar[int]
    SCREENLAYOUT_ROUND_MASK: ClassVar[int]
    SCREENLAYOUT_ROUND_NO: ClassVar[int]
    SCREENLAYOUT_ROUND_UNDEFINED: ClassVar[int]
    SCREENLAYOUT_ROUND_YES: ClassVar[int]
    SCREENLAYOUT_SIZE_LARGE: ClassVar[int]
    SCREENLAYOUT_SIZE_MASK: ClassVar[int]
    SCREENLAYOUT_SIZE_NORMAL: ClassVar[int]
    SCREENLAYOUT_SIZE_SMALL: ClassVar[int]
    SCREENLAYOUT_SIZE_UNDEFINED: ClassVar[int]
    SCREENLAYOUT_SIZE_XLARGE: ClassVar[int]
    SCREENLAYOUT_UNDEFINED: ClassVar[int]
    SCREEN_HEIGHT_DP_UNDEFINED: ClassVar[int]
    SCREEN_WIDTH_DP_UNDEFINED: ClassVar[int]
    SMALLEST_SCREEN_WIDTH_DP_UNDEFINED: ClassVar[int]
    TOUCHSCREEN_FINGER: ClassVar[int]
    TOUCHSCREEN_NOTOUCH: ClassVar[int]
    TOUCHSCREEN_STYLUS: ClassVar[int]
    TOUCHSCREEN_UNDEFINED: ClassVar[int]
    UI_MODE_NIGHT_MASK: ClassVar[int]
    UI_MODE_NIGHT_NO: ClassVar[int]
    UI_MODE_NIGHT_UNDEFINED: ClassVar[int]
    UI_MODE_NIGHT_YES: ClassVar[int]
    UI_MODE_TYPE_APPLIANCE: ClassVar[int]
    UI_MODE_TYPE_CAR: ClassVar[int]
    UI_MODE_TYPE_DESK: ClassVar[int]
    UI_MODE_TYPE_MASK: ClassVar[int]
    UI_MODE_TYPE_NORMAL: ClassVar[int]
    UI_MODE_TYPE_TELEVISION: ClassVar[int]
    UI_MODE_TYPE_UNDEFINED: ClassVar[int]
    UI_MODE_TYPE_VR_HEADSET: ClassVar[int]
    UI_MODE_TYPE_WATCH: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    colorMode: int
    densityDpi: int
    fontScale: float
    fontWeightAdjustment: int
    hardKeyboardHidden: int
    keyboard: int
    keyboardHidden: int
    locale: Locale
    mcc: int
    mnc: int
    navigation: int
    navigationHidden: int
    orientation: int
    screenHeightDp: int
    screenLayout: int
    screenWidthDp: int
    smallestScreenWidthDp: int
    touchscreen: int
    uiMode: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: "Configuration") -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def readFromParcel(self, p0: Parcel) -> None: ...
    def setLayoutDirection(self, p0: Locale) -> None: ...
    def getLayoutDirection(self) -> int: ...
    def diff(self, p0: "Configuration") -> int: ...
    def setTo(self, p0: "Configuration") -> None: ...
    def isLayoutSizeAtLeast(self, p0: int) -> bool: ...
    def setToDefaults(self) -> None: ...
    def updateFrom(self, p0: "Configuration") -> int: ...
    @staticmethod
    def needNewResources(p0: int, p1: int) -> bool: ...
    def isNightModeActive(self) -> bool: ...
    def getGrammaticalGender(self) -> int: ...
    def getLocales(self) -> LocaleList: ...
    def setLocales(self, p0: LocaleList) -> None: ...
    def setLocale(self, p0: Locale) -> None: ...
    def isScreenRound(self) -> bool: ...
    def isScreenWideColorGamut(self) -> bool: ...
    def isScreenHdr(self) -> bool: ...
    @staticmethod
    def generateDelta(p0: "Configuration", p1: "Configuration") -> "Configuration": ...
    @overload
    def equals(self, p0: "Configuration") -> bool: ...
    @overload
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    @overload
    def compareTo(self, p0: Any) -> int: ...
    @overload
    def compareTo(self, p0: "Configuration") -> int: ...
