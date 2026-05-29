from typing import Any, ClassVar, overload
from android.net.Uri import Uri
from android.os.PersistableBundle import PersistableBundle

class EventUrlProvider:
    def createEventTrackingUrlWithRedirect(self, p0: PersistableBundle, p1: Uri) -> Uri: ...
    def createEventTrackingUrlWithResponse(self, p0: PersistableBundle, p1: Any, p2: str) -> Uri: ...
