from typing import Any, ClassVar, overload
from android.location.GnssStatus import GnssStatus
from java.lang.Iterable import Iterable

class GpsStatus:
    GPS_EVENT_FIRST_FIX: ClassVar[int]
    GPS_EVENT_SATELLITE_STATUS: ClassVar[int]
    GPS_EVENT_STARTED: ClassVar[int]
    GPS_EVENT_STOPPED: ClassVar[int]
    @staticmethod
    def create(arg0: GnssStatus, arg1: int) -> "GpsStatus": ...
    def getTimeToFirstFix(self) -> int: ...
    def getSatellites(self) -> Iterable: ...
    def getMaxSatellites(self) -> int: ...

    class Listener:
        def onGpsStatusChanged(self, arg0: int) -> None: ...

    class NmeaListener:
        def onNmeaReceived(self, arg0: int, arg1: str) -> None: ...
