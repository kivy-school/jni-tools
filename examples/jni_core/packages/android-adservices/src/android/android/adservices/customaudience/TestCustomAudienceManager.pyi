from typing import Any, ClassVar, overload
from android.adservices.customaudience.AddCustomAudienceOverrideRequest import AddCustomAudienceOverrideRequest
from android.adservices.customaudience.RemoveCustomAudienceOverrideRequest import RemoveCustomAudienceOverrideRequest
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

class TestCustomAudienceManager:
    def overrideCustomAudienceRemoteInfo(self, p0: AddCustomAudienceOverrideRequest, p1: Executor, p2: OutcomeReceiver) -> None: ...
    def removeCustomAudienceRemoteInfoOverride(self, p0: RemoveCustomAudienceOverrideRequest, p1: Executor, p2: OutcomeReceiver) -> None: ...
    def resetAllCustomAudienceOverrides(self, p0: Executor, p1: OutcomeReceiver) -> None: ...
