from typing import Any, ClassVar, overload
from OSEmailSubscriptionStateChanges import OSEmailSubscriptionStateChanges

class OSEmailSubscriptionObserver:
    def onOSEmailSubscriptionChanged(self, arg0: OSEmailSubscriptionStateChanges) -> None: ...
