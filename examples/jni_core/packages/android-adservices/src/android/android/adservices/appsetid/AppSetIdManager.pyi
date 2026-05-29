from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

class AppSetIdManager:
    @staticmethod
    def get(p0: Context) -> "AppSetIdManager": ...
    def getAppSetId(self, p0: Executor, p1: OutcomeReceiver) -> None: ...
