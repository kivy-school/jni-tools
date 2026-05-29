from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangingManager"]

class RangingManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/RangingManager"
    BLE_CS = JavaStaticField("I")
    BLE_RSSI = JavaStaticField("I")
    UWB = JavaStaticField("I")
    WIFI_NAN_RTT = JavaStaticField("I")
    createRangingSession = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/ranging/RangingSession$Callback;)Landroid/ranging/RangingSession;")
    registerCapabilitiesCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/ranging/RangingManager$RangingCapabilitiesCallback;)V")
    unregisterCapabilitiesCallback = JavaMethod("(Landroid/ranging/RangingManager$RangingCapabilitiesCallback;)V")

    class RangingCapabilitiesCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/RangingManager$RangingCapabilitiesCallback"
        onRangingCapabilities = JavaMethod("(Landroid/ranging/RangingCapabilities;)V")