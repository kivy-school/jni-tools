from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.telephony.mbms.MbmsStreamingSessionCallback import MbmsStreamingSessionCallback
from android.telephony.mbms.StreamingService import StreamingService
from android.telephony.mbms.StreamingServiceCallback import StreamingServiceCallback
from android.telephony.mbms.StreamingServiceInfo import StreamingServiceInfo
from java.util.concurrent.Executor import Executor

class MbmsStreamingSession:
    def startStreaming(self, p0: StreamingServiceInfo, p1: Executor, p2: StreamingServiceCallback) -> StreamingService: ...
    def requestUpdateStreamingServices(self, p0: list) -> None: ...
    def close(self) -> None: ...
    @overload
    @staticmethod
    def create(p0: Context, p1: Executor, p2: MbmsStreamingSessionCallback) -> "MbmsStreamingSession": ...
    @overload
    @staticmethod
    def create(p0: Context, p1: Executor, p2: int, p3: MbmsStreamingSessionCallback) -> "MbmsStreamingSession": ...
