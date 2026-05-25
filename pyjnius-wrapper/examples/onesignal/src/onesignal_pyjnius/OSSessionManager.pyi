from typing import Any, ClassVar, overload
from OSLogger import OSLogger
from influence.data.OSTrackerFactory import OSTrackerFactory

class OSSessionManager:
    trackerFactory: OSTrackerFactory
    def __init__(self, arg0: "SessionListener", arg1: OSTrackerFactory, arg2: OSLogger) -> None: ...

    class SessionListener:
        def onSessionEnding(self, arg0: list) -> None: ...
