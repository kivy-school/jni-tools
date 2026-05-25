from typing import Any, ClassVar, overload
from android.view.inspector.InspectionCompanion import InspectionCompanion

class InspectionCompanionProvider:
    def provide(self, p0: type) -> InspectionCompanion: ...
