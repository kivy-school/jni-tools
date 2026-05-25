from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UserData"]

class UserData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/UserData"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTimezoneUtcOffset = JavaMethod("()Ljava/time/Duration;")
    getOrientation = JavaMethod("()I")
    getAvailableStorageBytes = JavaMethod("()J")
    getBatteryPercentage = JavaMethod("()I")
    getCarrier = JavaMethod("()Ljava/lang/String;")
    getNetworkCapabilities = JavaMethod("()Landroid/net/NetworkCapabilities;")
    getDataNetworkType = JavaMethod("()I")
    getAppInfos = JavaMethod("()Ljava/util/Map;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")