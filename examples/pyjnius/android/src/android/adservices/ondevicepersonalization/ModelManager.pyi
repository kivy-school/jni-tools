from typing import Any, ClassVar, overload
from android.adservices.ondevicepersonalization.InferenceInput import InferenceInput
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

class ModelManager:
    def run(self, p0: InferenceInput, p1: Executor, p2: OutcomeReceiver) -> None: ...
