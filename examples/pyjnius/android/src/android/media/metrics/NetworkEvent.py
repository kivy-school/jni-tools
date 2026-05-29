from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkEvent"]

class NetworkEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/metrics/NetworkEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    NETWORK_TYPE_2G = JavaStaticField("I")
    NETWORK_TYPE_3G = JavaStaticField("I")
    NETWORK_TYPE_4G = JavaStaticField("I")
    NETWORK_TYPE_5G_NSA = JavaStaticField("I")
    NETWORK_TYPE_5G_SA = JavaStaticField("I")
    NETWORK_TYPE_ETHERNET = JavaStaticField("I")
    NETWORK_TYPE_OFFLINE = JavaStaticField("I")
    NETWORK_TYPE_OTHER = JavaStaticField("I")
    NETWORK_TYPE_UNKNOWN = JavaStaticField("I")
    NETWORK_TYPE_WIFI = JavaStaticField("I")
    getNetworkType = JavaMethod("()I")
    getTimeSinceCreatedMillis = JavaMethod("()J")
    getMetricsBundle = JavaMethod("()Landroid/os/Bundle;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/metrics/NetworkEvent/Builder"
        __javaconstructor__ = [("()V", False)]
        setNetworkType = JavaMethod("(I)Landroid/media/metrics/NetworkEvent$Builder;")
        setTimeSinceCreatedMillis = JavaMethod("(J)Landroid/media/metrics/NetworkEvent$Builder;")
        setMetricsBundle = JavaMethod("(Landroid/os/Bundle;)Landroid/media/metrics/NetworkEvent$Builder;")
        build = JavaMethod("()Landroid/media/metrics/NetworkEvent;")