from typing import Any, ClassVar, overload
from android.adservices.topics.GetTopicsRequest import GetTopicsRequest
from android.content.Context import Context
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

class TopicsManager:
    @staticmethod
    def get(arg0: Context) -> "TopicsManager": ...
    def getTopics(self, arg0: GetTopicsRequest, arg1: Executor, arg2: OutcomeReceiver) -> None: ...
