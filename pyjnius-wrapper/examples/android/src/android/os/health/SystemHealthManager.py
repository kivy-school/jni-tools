from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SystemHealthManager"]

class SystemHealthManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/health/SystemHealthManager"
    takeUidSnapshot = JavaMethod("(I)Landroid/os/health/HealthStats;")
    takeMyUidSnapshot = JavaMethod("()Landroid/os/health/HealthStats;")
    takeUidSnapshots = JavaMethod("([I)[Landroid/os/health/HealthStats;")
    getSupportedPowerMonitors = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getPowerMonitorReadings = JavaMethod("(Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")