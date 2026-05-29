from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkStats"]

class NetworkStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/NetworkStats"
    hasNextBucket = JavaMethod("()Z")
    getNextBucket = JavaMethod("(Landroid/app/usage/NetworkStats$Bucket;)Z")
    close = JavaMethod("()V")

    class Bucket(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/usage/NetworkStats$Bucket"
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
        getDefaultNetworkStatus = JavaMethod("()I")
        getEndTimeStamp = JavaMethod("()J")
        getMetered = JavaMethod("()I")
        getRoaming = JavaMethod("()I")
        getRxBytes = JavaMethod("()J")
        getRxPackets = JavaMethod("()J")
        getStartTimeStamp = JavaMethod("()J")
        getTxBytes = JavaMethod("()J")
        getTxPackets = JavaMethod("()J")
        getState = JavaMethod("()I")
        getUid = JavaMethod("()I")
        getTag = JavaMethod("()I")