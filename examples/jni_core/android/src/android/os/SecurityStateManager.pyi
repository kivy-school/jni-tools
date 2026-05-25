from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle

class SecurityStateManager:
    KEY_KERNEL_VERSION: ClassVar[str]
    KEY_SYSTEM_SPL: ClassVar[str]
    KEY_VENDOR_SPL: ClassVar[str]
    def getGlobalSecurityState(self) -> Bundle: ...
