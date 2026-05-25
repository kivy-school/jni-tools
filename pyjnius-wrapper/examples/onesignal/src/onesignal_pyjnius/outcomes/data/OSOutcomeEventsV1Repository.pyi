from typing import Any, ClassVar, overload
from OSLogger import OSLogger
from OneSignalApiResponseHandler import OneSignalApiResponseHandler
from outcomes.data.OSOutcomeEventsCache import OSOutcomeEventsCache
from outcomes.data.OutcomeEventsService import OutcomeEventsService
from outcomes.domain.OSOutcomeEventParams import OSOutcomeEventParams

class OSOutcomeEventsV1Repository:
    def __init__(self, arg0: OSLogger, arg1: OSOutcomeEventsCache, arg2: OutcomeEventsService) -> None: ...
    def requestMeasureOutcomeEvent(self, arg0: str, arg1: int, arg2: OSOutcomeEventParams, arg3: OneSignalApiResponseHandler) -> None: ...

    class WhenMappings:
        ...
