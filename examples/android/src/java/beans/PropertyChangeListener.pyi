from typing import Any, ClassVar, overload
from java.beans.PropertyChangeEvent import PropertyChangeEvent

class PropertyChangeListener:
    def propertyChange(self, arg0: PropertyChangeEvent) -> None: ...
