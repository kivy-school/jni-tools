from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle

class OutOfContextTestingActivity:
    CLASS_NAME: ClassVar[str]
    AD_UNIT_KEY: ClassVar[str]
    def __init__(self) -> None: ...
    def onCreate(self, arg0: Bundle) -> None: ...
