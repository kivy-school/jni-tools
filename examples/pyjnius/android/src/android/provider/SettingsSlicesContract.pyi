from typing import Any, ClassVar, overload
from android.net.Uri import Uri

class SettingsSlicesContract:
    AUTHORITY: ClassVar[str]
    BASE_URI: ClassVar[Uri]
    KEY_AIRPLANE_MODE: ClassVar[str]
    KEY_BATTERY_SAVER: ClassVar[str]
    KEY_BLUETOOTH: ClassVar[str]
    KEY_LOCATION: ClassVar[str]
    KEY_WIFI: ClassVar[str]
    PATH_SETTING_ACTION: ClassVar[str]
    PATH_SETTING_INTENT: ClassVar[str]
