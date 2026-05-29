from typing import Any, ClassVar, overload
from android.view.inspector.PropertyMapper import PropertyMapper
from android.view.inspector.PropertyReader import PropertyReader

class InspectionCompanion:
    def mapProperties(self, p0: PropertyMapper) -> None: ...
    def readProperties(self, p0: Any, p1: PropertyReader) -> None: ...

    class UninitializedPropertyMapException:
        def __init__(self) -> None: ...
