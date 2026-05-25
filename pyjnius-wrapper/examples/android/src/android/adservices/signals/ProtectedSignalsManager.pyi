from typing import Any, ClassVar, overload
from android.adservices.signals.UpdateSignalsRequest import UpdateSignalsRequest
from android.content.Context import Context
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

class ProtectedSignalsManager:
    @staticmethod
    def get(arg0: Context) -> "ProtectedSignalsManager": ...
    def updateSignals(self, arg0: UpdateSignalsRequest, arg1: Executor, arg2: OutcomeReceiver) -> None: ...
