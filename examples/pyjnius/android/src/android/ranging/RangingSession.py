from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangingSession"]

class RangingSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/RangingSession"
    toString = JavaMethod("()Ljava/lang/String;")
    close = JavaMethod("()V")
    start = JavaMethod("(Landroid/ranging/RangingPreference;)Landroid/os/CancellationSignal;")
    addDeviceToRangingSession = JavaMethod("(Landroid/ranging/RangingConfig;)V")
    reconfigureRangingInterval = JavaMethod("(I)V")
    removeDeviceFromRangingSession = JavaMethod("(Landroid/ranging/RangingDevice;)V")
    stop = JavaMethod("()V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/RangingSession$Callback"
        REASON_LOCAL_REQUEST = JavaStaticField("I")
        REASON_NO_PEERS_FOUND = JavaStaticField("I")
        REASON_REMOTE_REQUEST = JavaStaticField("I")
        REASON_SYSTEM_POLICY = JavaStaticField("I")
        REASON_UNKNOWN = JavaStaticField("I")
        REASON_UNSUPPORTED = JavaStaticField("I")
        onClosed = JavaMethod("(I)V")
        onOpenFailed = JavaMethod("(I)V")
        onOpened = JavaMethod("()V")
        onStarted = JavaMethod("(Landroid/ranging/RangingDevice;I)V")
        onStopped = JavaMethod("(Landroid/ranging/RangingDevice;I)V")
        onResults = JavaMethod("(Landroid/ranging/RangingDevice;Landroid/ranging/RangingData;)V")