from typing import Any, ClassVar, overload
from android.content.pm.verify.domain.DomainVerificationUserState import DomainVerificationUserState

class DomainVerificationManager:
    def getDomainVerificationUserState(self, arg0: str) -> DomainVerificationUserState: ...
