from typing import Any, ClassVar, overload
from android.view.inspector.PropertyMapper import PropertyMapper
from android.view.inspector.PropertyReader import PropertyReader

class InspectionCompanion:
    def mapProperties(self, arg0: PropertyMapper) -> None: ...
    def readProperties(self, arg0: Any, arg1: PropertyReader) -> None: ...

    class UninitializedPropertyMapException:
        def __init__(self) -> None: ...
