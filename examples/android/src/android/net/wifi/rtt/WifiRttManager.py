from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiRttManager"]

class WifiRttManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/rtt/WifiRttManager"
    ACTION_WIFI_RTT_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    CHARACTERISTICS_KEY_BOOLEAN_LCI = JavaStaticField("Ljava/lang/String;")
    CHARACTERISTICS_KEY_BOOLEAN_LCR = JavaStaticField("Ljava/lang/String;")
    CHARACTERISTICS_KEY_BOOLEAN_NTB_INITIATOR = JavaStaticField("Ljava/lang/String;")
    CHARACTERISTICS_KEY_BOOLEAN_ONE_SIDED_RTT = JavaStaticField("Ljava/lang/String;")
    CHARACTERISTICS_KEY_BOOLEAN_STA_RESPONDER = JavaStaticField("Ljava/lang/String;")
    isAvailable = JavaMethod("()Z")
    startRanging = JavaMethod("(Landroid/net/wifi/rtt/RangingRequest;Ljava/util/concurrent/Executor;Landroid/net/wifi/rtt/RangingResultCallback;)V")
    getRttCharacteristics = JavaMethod("()Landroid/os/Bundle;")