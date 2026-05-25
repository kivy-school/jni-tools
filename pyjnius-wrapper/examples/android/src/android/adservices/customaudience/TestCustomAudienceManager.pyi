from typing import Any, ClassVar, overload
from android.adservices.customaudience.AddCustomAudienceOverrideRequest import AddCustomAudienceOverrideRequest
from android.adservices.customaudience.RemoveCustomAudienceOverrideRequest import RemoveCustomAudienceOverrideRequest
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

class TestCustomAudienceManager:
    def overrideCustomAudienceRemoteInfo(self, arg0: AddCustomAudienceOverrideRequest, arg1: Executor, arg2: OutcomeReceiver) -> None: ...
    def removeCustomAudienceRemoteInfoOverride(self, arg0: RemoveCustomAudienceOverrideRequest, arg1: Executor, arg2: OutcomeReceiver) -> None: ...
    def resetAllCustomAudienceOverrides(self, arg0: Executor, arg1: OutcomeReceiver) -> None: ...
