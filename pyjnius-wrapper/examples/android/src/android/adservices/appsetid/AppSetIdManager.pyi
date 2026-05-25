from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

class AppSetIdManager:
    @staticmethod
    def get(arg0: Context) -> "AppSetIdManager": ...
    def getAppSetId(self, arg0: Executor, arg1: OutcomeReceiver) -> None: ...
