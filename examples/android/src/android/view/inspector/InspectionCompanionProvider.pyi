from typing import Any, ClassVar, overload
from android.view.inspector.InspectionCompanion import InspectionCompanion

class InspectionCompanionProvider:
    def provide(self, arg0: type) -> InspectionCompanion: ...
