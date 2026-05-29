from typing import Any, ClassVar, overload
from java.util.prefs.PreferenceChangeEvent import PreferenceChangeEvent

class PreferenceChangeListener:
    def preferenceChange(self, p0: PreferenceChangeEvent) -> None: ...
