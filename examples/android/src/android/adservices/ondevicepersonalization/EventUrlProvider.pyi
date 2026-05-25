from typing import Any, ClassVar, overload
from android.net.Uri import Uri
from android.os.PersistableBundle import PersistableBundle

class EventUrlProvider:
    def createEventTrackingUrlWithResponse(self, arg0: PersistableBundle, arg1: list[int], arg2: str) -> Uri: ...
    def createEventTrackingUrlWithRedirect(self, arg0: PersistableBundle, arg1: Uri) -> Uri: ...
