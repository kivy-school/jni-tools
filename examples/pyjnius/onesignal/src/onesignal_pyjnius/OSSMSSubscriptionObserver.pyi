from typing import Any, ClassVar, overload
from OSSMSSubscriptionStateChanges import OSSMSSubscriptionStateChanges

class OSSMSSubscriptionObserver:
    def onSMSSubscriptionChanged(self, arg0: OSSMSSubscriptionStateChanges) -> None: ...
