from typing import Any, ClassVar, overload
from android.graphics.drawable.Icon import Icon

class CustomPrinterIconCallback:
    def onCustomPrinterIconLoaded(self, p0: Icon) -> bool: ...
