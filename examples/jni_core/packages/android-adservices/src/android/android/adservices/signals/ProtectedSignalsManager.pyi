from typing import Any, ClassVar, overload
from android.adservices.signals.UpdateSignalsRequest import UpdateSignalsRequest
from android.content.Context import Context
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

class ProtectedSignalsManager:
    def updateSignals(self, p0: UpdateSignalsRequest, p1: Executor, p2: OutcomeReceiver) -> None: ...
    @staticmethod
    def get(p0: Context) -> "ProtectedSignalsManager": ...
