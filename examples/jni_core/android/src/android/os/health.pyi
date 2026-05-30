from typing import Any, ClassVar, overload

class UidHealthStats:
    MEASUREMENT_BLUETOOTH_IDLE_MS: ClassVar[int]
    MEASUREMENT_BLUETOOTH_POWER_MAMS: ClassVar[int]
    MEASUREMENT_BLUETOOTH_RX_BYTES: ClassVar[int]
    MEASUREMENT_BLUETOOTH_RX_MS: ClassVar[int]
    MEASUREMENT_BLUETOOTH_RX_PACKETS: ClassVar[int]
    MEASUREMENT_BLUETOOTH_TX_BYTES: ClassVar[int]
    MEASUREMENT_BLUETOOTH_TX_MS: ClassVar[int]
    MEASUREMENT_BLUETOOTH_TX_PACKETS: ClassVar[int]
    MEASUREMENT_BUTTON_USER_ACTIVITY_COUNT: ClassVar[int]
    MEASUREMENT_CPU_POWER_MAMS: ClassVar[int]
    MEASUREMENT_MOBILE_IDLE_MS: ClassVar[int]
    MEASUREMENT_MOBILE_POWER_MAMS: ClassVar[int]
    MEASUREMENT_MOBILE_RX_BYTES: ClassVar[int]
    MEASUREMENT_MOBILE_RX_MS: ClassVar[int]
    MEASUREMENT_MOBILE_RX_PACKETS: ClassVar[int]
    MEASUREMENT_MOBILE_TX_BYTES: ClassVar[int]
    MEASUREMENT_MOBILE_TX_MS: ClassVar[int]
    MEASUREMENT_MOBILE_TX_PACKETS: ClassVar[int]
    MEASUREMENT_OTHER_USER_ACTIVITY_COUNT: ClassVar[int]
    MEASUREMENT_REALTIME_BATTERY_MS: ClassVar[int]
    MEASUREMENT_REALTIME_SCREEN_OFF_BATTERY_MS: ClassVar[int]
    MEASUREMENT_SYSTEM_CPU_TIME_MS: ClassVar[int]
    MEASUREMENT_TOUCH_USER_ACTIVITY_COUNT: ClassVar[int]
    MEASUREMENT_UPTIME_BATTERY_MS: ClassVar[int]
    MEASUREMENT_UPTIME_SCREEN_OFF_BATTERY_MS: ClassVar[int]
    MEASUREMENT_USER_CPU_TIME_MS: ClassVar[int]
    MEASUREMENT_WIFI_FULL_LOCK_MS: ClassVar[int]
    MEASUREMENT_WIFI_IDLE_MS: ClassVar[int]
    MEASUREMENT_WIFI_MULTICAST_MS: ClassVar[int]
    MEASUREMENT_WIFI_POWER_MAMS: ClassVar[int]
    MEASUREMENT_WIFI_RUNNING_MS: ClassVar[int]
    MEASUREMENT_WIFI_RX_BYTES: ClassVar[int]
    MEASUREMENT_WIFI_RX_MS: ClassVar[int]
    MEASUREMENT_WIFI_RX_PACKETS: ClassVar[int]
    MEASUREMENT_WIFI_TX_BYTES: ClassVar[int]
    MEASUREMENT_WIFI_TX_MS: ClassVar[int]
    MEASUREMENT_WIFI_TX_PACKETS: ClassVar[int]
    STATS_PACKAGES: ClassVar[int]
    STATS_PIDS: ClassVar[int]
    STATS_PROCESSES: ClassVar[int]
    TIMERS_JOBS: ClassVar[int]
    TIMERS_SENSORS: ClassVar[int]
    TIMERS_SYNCS: ClassVar[int]
    TIMERS_WAKELOCKS_DRAW: ClassVar[int]
    TIMERS_WAKELOCKS_FULL: ClassVar[int]
    TIMERS_WAKELOCKS_PARTIAL: ClassVar[int]
    TIMERS_WAKELOCKS_WINDOW: ClassVar[int]
    TIMER_AUDIO: ClassVar[int]
    TIMER_BLUETOOTH_SCAN: ClassVar[int]
    TIMER_CAMERA: ClassVar[int]
    TIMER_FLASHLIGHT: ClassVar[int]
    TIMER_FOREGROUND_ACTIVITY: ClassVar[int]
    TIMER_GPS_SENSOR: ClassVar[int]
    TIMER_MOBILE_RADIO_ACTIVE: ClassVar[int]
    TIMER_PROCESS_STATE_BACKGROUND_MS: ClassVar[int]
    TIMER_PROCESS_STATE_CACHED_MS: ClassVar[int]
    TIMER_PROCESS_STATE_FOREGROUND_MS: ClassVar[int]
    TIMER_PROCESS_STATE_FOREGROUND_SERVICE_MS: ClassVar[int]
    TIMER_PROCESS_STATE_TOP_MS: ClassVar[int]
    TIMER_PROCESS_STATE_TOP_SLEEPING_MS: ClassVar[int]
    TIMER_VIBRATOR: ClassVar[int]
    TIMER_VIDEO: ClassVar[int]
    TIMER_WIFI_SCAN: ClassVar[int]

from typing import Any, ClassVar, overload

class PackageHealthStats:
    MEASUREMENTS_WAKEUP_ALARMS_COUNT: ClassVar[int]
    STATS_SERVICES: ClassVar[int]

from typing import Any, ClassVar, overload

class ServiceHealthStats:
    MEASUREMENT_LAUNCH_COUNT: ClassVar[int]
    MEASUREMENT_START_SERVICE_COUNT: ClassVar[int]

from typing import Any, ClassVar, overload

class PidHealthStats:
    MEASUREMENT_WAKE_NESTING_COUNT: ClassVar[int]
    MEASUREMENT_WAKE_START_MS: ClassVar[int]
    MEASUREMENT_WAKE_SUM_MS: ClassVar[int]

from typing import Any, ClassVar, overload

class ProcessHealthStats:
    MEASUREMENT_ANR_COUNT: ClassVar[int]
    MEASUREMENT_CRASHES_COUNT: ClassVar[int]
    MEASUREMENT_FOREGROUND_MS: ClassVar[int]
    MEASUREMENT_STARTS_COUNT: ClassVar[int]
    MEASUREMENT_SYSTEM_TIME_MS: ClassVar[int]
    MEASUREMENT_USER_TIME_MS: ClassVar[int]

from typing import Any, ClassVar, overload
from android.os.health.TimerStat import TimerStat

class HealthStats:
    def hasMeasurements(self, p0: int) -> bool: ...
    def getMeasurementsKeyCount(self) -> int: ...
    def getMeasurementKeyCount(self) -> int: ...
    def getMeasurementKeyAt(self, p0: int) -> int: ...
    def getMeasurementsKeyAt(self, p0: int) -> int: ...
    def getStats(self, p0: int) -> dict: ...
    def getStatsKeyAt(self, p0: int) -> int: ...
    def getStatsKeyCount(self) -> int: ...
    def getTimer(self, p0: int) -> TimerStat: ...
    def getTimerCount(self, p0: int) -> int: ...
    def getTimerKeyAt(self, p0: int) -> int: ...
    def getTimerKeyCount(self) -> int: ...
    def getTimerTime(self, p0: int) -> int: ...
    def getTimers(self, p0: int) -> dict: ...
    def getTimersKeyAt(self, p0: int) -> int: ...
    def getTimersKeyCount(self) -> int: ...
    def hasMeasurement(self, p0: int) -> bool: ...
    def hasStats(self, p0: int) -> bool: ...
    def hasTimer(self, p0: int) -> bool: ...
    def hasTimers(self, p0: int) -> bool: ...
    def getDataType(self) -> str: ...
    def getMeasurements(self, p0: int) -> dict: ...
    def getMeasurement(self, p0: int) -> int: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class TimerStat:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self, p0: int, p1: int) -> None: ...
    @overload
    def __init__(self, p0: Parcel) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def setCount(self, p0: int) -> None: ...
    def getCount(self) -> int: ...
    def setTime(self, p0: int) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getTime(self) -> int: ...

from typing import Any, ClassVar, overload
from android.os.CpuHeadroomParams import CpuHeadroomParams
from android.os.GpuHeadroomParams import GpuHeadroomParams
from android.os.OutcomeReceiver import OutcomeReceiver
from android.os.health.HealthStats import HealthStats
from android.util.Pair import Pair
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class SystemHealthManager:
    def getCpuHeadroomCalculationWindowRange(self) -> Pair: ...
    def getGpuHeadroom(self, p0: GpuHeadroomParams) -> float: ...
    def getCpuHeadroom(self, p0: CpuHeadroomParams) -> float: ...
    def getCpuHeadroomMinIntervalMillis(self) -> int: ...
    def getGpuHeadroomCalculationWindowRange(self) -> Pair: ...
    def getGpuHeadroomMinIntervalMillis(self) -> int: ...
    def getMaxCpuHeadroomTidsSize(self) -> int: ...
    def getPowerMonitorReadings(self, p0: list, p1: Executor, p2: OutcomeReceiver) -> None: ...
    def getSupportedPowerMonitors(self, p0: Executor, p1: Consumer) -> None: ...
    def takeMyUidSnapshot(self) -> HealthStats: ...
    def takeUidSnapshot(self, p0: int) -> HealthStats: ...
    def takeUidSnapshots(self, p0: Any) -> Any: ...

