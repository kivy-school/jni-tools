from typing import Any, ClassVar, overload
from android.app.appfunctions.ExecuteAppFunctionRequest import ExecuteAppFunctionRequest
from android.os.CancellationSignal import CancellationSignal
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

class AppFunctionManager:
    APP_FUNCTION_STATE_DEFAULT: ClassVar[int]
    APP_FUNCTION_STATE_DISABLED: ClassVar[int]
    APP_FUNCTION_STATE_ENABLED: ClassVar[int]
    def executeAppFunction(self, p0: ExecuteAppFunctionRequest, p1: Executor, p2: CancellationSignal, p3: OutcomeReceiver) -> None: ...
    @overload
    def isAppFunctionEnabled(self, p0: str, p1: str, p2: Executor, p3: OutcomeReceiver) -> None: ...
    @overload
    def isAppFunctionEnabled(self, p0: str, p1: Executor, p2: OutcomeReceiver) -> None: ...
    def setAppFunctionEnabled(self, p0: str, p1: int, p2: Executor, p3: OutcomeReceiver) -> None: ...
