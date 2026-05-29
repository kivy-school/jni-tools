from typing import Any, ClassVar, overload
from android.adservices.ondevicepersonalization.ExecuteInIsolatedServiceRequest import ExecuteInIsolatedServiceRequest
from android.adservices.ondevicepersonalization.SurfacePackageToken import SurfacePackageToken
from android.content.ComponentName import ComponentName
from android.os.IBinder import IBinder
from android.os.OutcomeReceiver import OutcomeReceiver
from android.os.PersistableBundle import PersistableBundle
from java.util.concurrent.Executor import Executor

class OnDevicePersonalizationManager:
    def executeInIsolatedService(self, p0: ExecuteInIsolatedServiceRequest, p1: Executor, p2: OutcomeReceiver) -> None: ...
    def requestSurfacePackage(self, p0: SurfacePackageToken, p1: IBinder, p2: int, p3: int, p4: int, p5: Executor, p6: OutcomeReceiver) -> None: ...
    def execute(self, p0: ComponentName, p1: PersistableBundle, p2: Executor, p3: OutcomeReceiver) -> None: ...

    class ExecuteResult:
        def getOutputData(self) -> Any: ...
        def getSurfacePackageToken(self) -> SurfacePackageToken: ...
