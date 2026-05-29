from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HealthStats"]

class HealthStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/health/HealthStats"
    hasMeasurements = JavaMethod("(I)Z")
    getMeasurements = JavaMethod("(I)Ljava/util/Map;")
    getMeasurementKeyAt = JavaMethod("(I)I")
    getMeasurementKeyCount = JavaMethod("()I")
    getMeasurementsKeyAt = JavaMethod("(I)I")
    getMeasurementsKeyCount = JavaMethod("()I")
    getStats = JavaMethod("(I)Ljava/util/Map;")
    getStatsKeyAt = JavaMethod("(I)I")
    getStatsKeyCount = JavaMethod("()I")
    getTimer = JavaMethod("(I)Landroid/os/health/TimerStat;")
    getTimerCount = JavaMethod("(I)I")
    getTimerKeyAt = JavaMethod("(I)I")
    getTimerKeyCount = JavaMethod("()I")
    getTimerTime = JavaMethod("(I)J")
    getTimers = JavaMethod("(I)Ljava/util/Map;")
    getTimersKeyAt = JavaMethod("(I)I")
    getTimersKeyCount = JavaMethod("()I")
    hasMeasurement = JavaMethod("(I)Z")
    hasStats = JavaMethod("(I)Z")
    hasTimer = JavaMethod("(I)Z")
    hasTimers = JavaMethod("(I)Z")
    getDataType = JavaMethod("()Ljava/lang/String;")
    getMeasurement = JavaMethod("(I)J")