from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SystemHealthManager"]

class SystemHealthManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/health/SystemHealthManager"
    takeUidSnapshots = JavaMethod("([I)[Landroid/os/health/HealthStats;")
    getGpuHeadroom = JavaMethod("(Landroid/os/GpuHeadroomParams;)F")
    takeUidSnapshot = JavaMethod("(I)Landroid/os/health/HealthStats;")
    takeMyUidSnapshot = JavaMethod("()Landroid/os/health/HealthStats;")
    getCpuHeadroomCalculationWindowRange = JavaMethod("()Landroid/util/Pair;")
    getCpuHeadroomMinIntervalMillis = JavaMethod("()J")
    getGpuHeadroomCalculationWindowRange = JavaMethod("()Landroid/util/Pair;")
    getGpuHeadroomMinIntervalMillis = JavaMethod("()J")
    getCpuHeadroom = JavaMethod("(Landroid/os/CpuHeadroomParams;)F")
    getMaxCpuHeadroomTidsSize = JavaMethod("()I")
    getPowerMonitorReadings = JavaMethod("(Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getSupportedPowerMonitors = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")