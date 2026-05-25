from typing import Any, ClassVar, overload
from OSSubscriptionStateChanges import OSSubscriptionStateChanges

class OSSubscriptionObserver:
    def onOSSubscriptionChanged(self, arg0: OSSubscriptionStateChanges) -> None: ...
