from typing import Any, ClassVar, overload
from android.adservices.ondevicepersonalization.SurfacePackageToken import SurfacePackageToken
from android.content.ComponentName import ComponentName
from android.os.IBinder import IBinder
from android.os.OutcomeReceiver import OutcomeReceiver
from android.os.PersistableBundle import PersistableBundle
from java.util.concurrent.Executor import Executor

class OnDevicePersonalizationManager:
    def execute(self, arg0: ComponentName, arg1: PersistableBundle, arg2: Executor, arg3: OutcomeReceiver) -> None: ...
    def requestSurfacePackage(self, arg0: SurfacePackageToken, arg1: IBinder, arg2: int, arg3: int, arg4: int, arg5: Executor, arg6: OutcomeReceiver) -> None: ...

    class ExecuteResult:
        def getSurfacePackageToken(self) -> SurfacePackageToken: ...
        def getOutputData(self) -> list[int]: ...
