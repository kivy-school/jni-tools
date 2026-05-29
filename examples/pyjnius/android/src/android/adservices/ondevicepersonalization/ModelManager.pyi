from typing import Any, ClassVar, overload
from android.adservices.ondevicepersonalization.InferenceInput import InferenceInput
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

class ModelManager:
    def run(self, arg0: InferenceInput, arg1: Executor, arg2: OutcomeReceiver) -> None: ...
