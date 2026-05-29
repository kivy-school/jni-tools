from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.CancellationSignal import CancellationSignal
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class ProfilingManager:
    PROFILING_TYPE_HEAP_PROFILE: ClassVar[int]
    PROFILING_TYPE_JAVA_HEAP_DUMP: ClassVar[int]
    PROFILING_TYPE_STACK_SAMPLING: ClassVar[int]
    PROFILING_TYPE_SYSTEM_TRACE: ClassVar[int]
    def requestProfiling(self, arg0: int, arg1: Bundle, arg2: str, arg3: CancellationSignal, arg4: Executor, arg5: Consumer) -> None: ...
    def registerForAllProfilingResults(self, arg0: Executor, arg1: Consumer) -> None: ...
    def unregisterForAllProfilingResults(self, arg0: Consumer) -> None: ...
