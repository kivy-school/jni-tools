from typing import Any, ClassVar, overload
from android.app.admin.PolicyUpdateResult import PolicyUpdateResult
from android.app.admin.TargetUser import TargetUser
from android.content.Context import Context
from android.content.Intent import Intent
from android.os.Bundle import Bundle

class PolicyUpdateReceiver:
    ACTION_DEVICE_POLICY_CHANGED: ClassVar[str]
    ACTION_DEVICE_POLICY_SET_RESULT: ClassVar[str]
    EXTRA_ACCOUNT_TYPE: ClassVar[str]
    EXTRA_INTENT_FILTER: ClassVar[str]
    EXTRA_PACKAGE_NAME: ClassVar[str]
    EXTRA_PERMISSION_NAME: ClassVar[str]
    def __init__(self) -> None: ...
    def onReceive(self, arg0: Context, arg1: Intent) -> None: ...
    def onPolicySetResult(self, arg0: Context, arg1: str, arg2: Bundle, arg3: TargetUser, arg4: PolicyUpdateResult) -> None: ...
    def onPolicyChanged(self, arg0: Context, arg1: str, arg2: Bundle, arg3: TargetUser, arg4: PolicyUpdateResult) -> None: ...
