from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiAwareChannelInfo"]

class WifiAwareChannelInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/WifiAwareChannelInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getChannelFrequencyMhz = JavaMethod("()I")
    getChannelBandwidth = JavaMethod("()I")
    getSpatialStreamCount = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")