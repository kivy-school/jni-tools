from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HealthStats"]

class HealthStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/health/HealthStats"
    getDataType = JavaMethod("()Ljava/lang/String;")
    hasTimer = JavaMethod("(I)Z")
    getTimer = JavaMethod("(I)Landroid/os/health/TimerStat;")
    getTimerCount = JavaMethod("(I)I")
    getTimerTime = JavaMethod("(I)J")
    getTimerKeyCount = JavaMethod("()I")
    getTimerKeyAt = JavaMethod("(I)I")
    hasMeasurement = JavaMethod("(I)Z")
    getMeasurement = JavaMethod("(I)J")
    getMeasurementKeyCount = JavaMethod("()I")
    getMeasurementKeyAt = JavaMethod("(I)I")
    hasStats = JavaMethod("(I)Z")
    getStats = JavaMethod("(I)Ljava/util/Map;")
    getStatsKeyCount = JavaMethod("()I")
    getStatsKeyAt = JavaMethod("(I)I")
    hasTimers = JavaMethod("(I)Z")
    getTimers = JavaMethod("(I)Ljava/util/Map;")
    getTimersKeyCount = JavaMethod("()I")
    getTimersKeyAt = JavaMethod("(I)I")
    hasMeasurements = JavaMethod("(I)Z")
    getMeasurements = JavaMethod("(I)Ljava/util/Map;")
    getMeasurementsKeyCount = JavaMethod("()I")
    getMeasurementsKeyAt = JavaMethod("(I)I")