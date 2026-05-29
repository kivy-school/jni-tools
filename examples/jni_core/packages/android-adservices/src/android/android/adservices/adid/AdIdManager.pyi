from typing import Any, ClassVar, overload
from android.adservices.common.AdServicesOutcomeReceiver import AdServicesOutcomeReceiver
from android.content.Context import Context
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

class AdIdManager:
    @overload
    def getAdId(self, p0: Executor, p1: AdServicesOutcomeReceiver) -> None: ...
    @overload
    def getAdId(self, p0: Executor, p1: OutcomeReceiver) -> None: ...
    @staticmethod
    def get(p0: Context) -> "AdIdManager": ...
