from typing import Any, ClassVar, overload
from android.os.IBinder import IBinder

class IInterface:
    def asBinder(self) -> IBinder: ...
