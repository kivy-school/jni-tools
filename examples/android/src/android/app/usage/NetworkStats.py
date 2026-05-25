from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkStats"]

class NetworkStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/NetworkStats"
    finalize = JavaMethod("()V")
    getNextBucket = JavaMethod("(Landroid/app/usage/NetworkStats$Bucket;)Z")
    hasNextBucket = JavaMethod("()Z")
    close = JavaMethod("()V")

    class Bucket(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/usage/NetworkStats/Bucket"
        __javaconstructor__ = [("()V", False)]
        DEFAULT_NETWORK_ALL = JavaStaticField("I")
        DEFAULT_NETWORK_NO = JavaStaticField("I")
        DEFAULT_NETWORK_YES = JavaStaticField("I")
        METERED_ALL = JavaStaticField("I")
        METERED_NO = JavaStaticField("I")
        METERED_YES = JavaStaticField("I")
        ROAMING_ALL = JavaStaticField("I")
        ROAMING_NO = JavaStaticField("I")
        ROAMING_YES = JavaStaticField("I")
        STATE_ALL = JavaStaticField("I")
        STATE_DEFAULT = JavaStaticField("I")
        STATE_FOREGROUND = JavaStaticField("I")
        TAG_NONE = JavaStaticField("I")
        UID_ALL = JavaStaticField("I")
        UID_REMOVED = JavaStaticField("I")
        UID_TETHERING = JavaStaticField("I")
        getUid = JavaMethod("()I")
        getTag = JavaMethod("()I")
        getState = JavaMethod("()I")
        getMetered = JavaMethod("()I")
        getRoaming = JavaMethod("()I")
        getDefaultNetworkStatus = JavaMethod("()I")
        getStartTimeStamp = JavaMethod("()J")
        getEndTimeStamp = JavaMethod("()J")
        getRxBytes = JavaMethod("()J")
        getTxBytes = JavaMethod("()J")
        getRxPackets = JavaMethod("()J")
        getTxPackets = JavaMethod("()J")