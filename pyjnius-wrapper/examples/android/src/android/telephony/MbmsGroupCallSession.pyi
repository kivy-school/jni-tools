from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.telephony.mbms.GroupCall import GroupCall
from android.telephony.mbms.GroupCallCallback import GroupCallCallback
from android.telephony.mbms.MbmsGroupCallSessionCallback import MbmsGroupCallSessionCallback
from java.util.concurrent.Executor import Executor

class MbmsGroupCallSession:
    @overload
    @staticmethod
    def create(arg0: Context, arg1: int, arg2: Executor, arg3: MbmsGroupCallSessionCallback) -> "MbmsGroupCallSession": ...
    @overload
    @staticmethod
    def create(arg0: Context, arg1: Executor, arg2: MbmsGroupCallSessionCallback) -> "MbmsGroupCallSession": ...
    def close(self) -> None: ...
    def startGroupCall(self, arg0: int, arg1: list, arg2: list, arg3: Executor, arg4: GroupCallCallback) -> GroupCall: ...
