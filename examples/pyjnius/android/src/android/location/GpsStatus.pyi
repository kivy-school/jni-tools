from typing import Any, ClassVar, overload
from android.location.GnssStatus import GnssStatus
from java.lang.Iterable import Iterable

class GpsStatus:
    GPS_EVENT_FIRST_FIX: ClassVar[int]
    GPS_EVENT_SATELLITE_STATUS: ClassVar[int]
    GPS_EVENT_STARTED: ClassVar[int]
    GPS_EVENT_STOPPED: ClassVar[int]
    @staticmethod
    def create(p0: GnssStatus, p1: int) -> "GpsStatus": ...
    def getMaxSatellites(self) -> int: ...
    def getSatellites(self) -> Iterable: ...
    def getTimeToFirstFix(self) -> int: ...

    class NmeaListener:
        def onNmeaReceived(self, p0: int, p1: str) -> None: ...

    class Listener:
        def onGpsStatusChanged(self, p0: int) -> None: ...
