from typing import Any, ClassVar, overload
from OSLogger import OSLogger
from OSSharedPreferences import OSSharedPreferences
from OneSignalAPIClient import OneSignalAPIClient
from OneSignalDb import OneSignalDb
from outcomes.domain.OSOutcomeEventsRepository import OSOutcomeEventsRepository

class OSOutcomeEventsFactory:
    def __init__(self, arg0: OSLogger, arg1: OneSignalAPIClient, arg2: OneSignalDb, arg3: OSSharedPreferences) -> None: ...
    def getRepository(self) -> OSOutcomeEventsRepository: ...
