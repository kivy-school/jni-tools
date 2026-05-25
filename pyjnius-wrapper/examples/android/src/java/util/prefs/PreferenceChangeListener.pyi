from typing import Any, ClassVar, overload
from java.util.prefs.PreferenceChangeEvent import PreferenceChangeEvent

class PreferenceChangeListener:
    def preferenceChange(self, arg0: PreferenceChangeEvent) -> None: ...
