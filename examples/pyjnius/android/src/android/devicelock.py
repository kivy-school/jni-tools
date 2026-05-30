from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class DeviceLockManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/devicelock/DeviceLockManager"
    DEVICE_LOCK_ROLE_FINANCING = JavaStaticField("I")
    isDeviceLocked = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getKioskApps = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    lockDevice = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    unlockDevice = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getDeviceId = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")

class DeviceId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/devicelock/DeviceId"
    DEVICE_ID_TYPE_IMEI = JavaStaticField("I")
    DEVICE_ID_TYPE_MEID = JavaStaticField("I")
    getId = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")