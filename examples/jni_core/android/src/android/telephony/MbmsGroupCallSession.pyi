from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.telephony.mbms.GroupCall import GroupCall
from android.telephony.mbms.GroupCallCallback import GroupCallCallback
from android.telephony.mbms.MbmsGroupCallSessionCallback import MbmsGroupCallSessionCallback
from java.util.concurrent.Executor import Executor

class MbmsGroupCallSession:
    def startGroupCall(self, p0: int, p1: list, p2: list, p3: Executor, p4: GroupCallCallback) -> GroupCall: ...
    @overload
    @staticmethod
    def create(p0: Context, p1: Executor, p2: MbmsGroupCallSessionCallback) -> "MbmsGroupCallSession": ...
    @overload
    @staticmethod
    def create(p0: Context, p1: int, p2: Executor, p3: MbmsGroupCallSessionCallback) -> "MbmsGroupCallSession": ...
    def close(self) -> None: ...
