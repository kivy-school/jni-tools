from typing import Any, ClassVar, overload
from android.adservices.common.AdServicesOutcomeReceiver import AdServicesOutcomeReceiver
from android.content.Context import Context
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

class AdIdManager:
    @staticmethod
    def get(arg0: Context) -> "AdIdManager": ...
    @overload
    def getAdId(self, arg0: Executor, arg1: OutcomeReceiver) -> None: ...
    @overload
    def getAdId(self, arg0: Executor, arg1: AdServicesOutcomeReceiver) -> None: ...
