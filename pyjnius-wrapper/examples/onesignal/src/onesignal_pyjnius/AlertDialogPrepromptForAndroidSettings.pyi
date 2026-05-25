from typing import Any, ClassVar, overload
from android.app.Activity import Activity

class AlertDialogPrepromptForAndroidSettings:
    INSTANCE: ClassVar["AlertDialogPrepromptForAndroidSettings"]
    def show(self, arg0: Activity, arg1: str, arg2: str, arg3: "Callback") -> None: ...

    class Callback:
        def onAccept(self) -> None: ...
        def onDecline(self) -> None: ...
