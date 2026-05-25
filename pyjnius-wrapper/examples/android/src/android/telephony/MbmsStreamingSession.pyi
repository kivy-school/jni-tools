from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.telephony.mbms.MbmsStreamingSessionCallback import MbmsStreamingSessionCallback
from android.telephony.mbms.StreamingService import StreamingService
from android.telephony.mbms.StreamingServiceCallback import StreamingServiceCallback
from android.telephony.mbms.StreamingServiceInfo import StreamingServiceInfo
from java.util.concurrent.Executor import Executor

class MbmsStreamingSession:
    @overload
    @staticmethod
    def create(arg0: Context, arg1: Executor, arg2: int, arg3: MbmsStreamingSessionCallback) -> "MbmsStreamingSession": ...
    @overload
    @staticmethod
    def create(arg0: Context, arg1: Executor, arg2: MbmsStreamingSessionCallback) -> "MbmsStreamingSession": ...
    def close(self) -> None: ...
    def requestUpdateStreamingServices(self, arg0: list) -> None: ...
    def startStreaming(self, arg0: StreamingServiceInfo, arg1: Executor, arg2: StreamingServiceCallback) -> StreamingService: ...
