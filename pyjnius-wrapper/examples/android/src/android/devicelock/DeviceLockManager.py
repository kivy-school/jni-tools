from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeviceLockManager"]

class DeviceLockManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/devicelock/DeviceLockManager"
    DEVICE_LOCK_ROLE_FINANCING = JavaStaticField("I")
    lockDevice = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    unlockDevice = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    isDeviceLocked = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getDeviceId = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getKioskApps = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")