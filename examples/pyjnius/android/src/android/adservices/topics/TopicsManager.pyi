from typing import Any, ClassVar, overload
from android.adservices.topics.GetTopicsRequest import GetTopicsRequest
from android.content.Context import Context
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

class TopicsManager:
    def getTopics(self, p0: GetTopicsRequest, p1: Executor, p2: OutcomeReceiver) -> None: ...
    @staticmethod
    def get(p0: Context) -> "TopicsManager": ...
