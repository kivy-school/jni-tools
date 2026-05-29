from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UserData"]

class UserData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/UserData"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCarrier = JavaMethod("()Ljava/lang/String;")
    getAppInfos = JavaMethod("()Ljava/util/Map;")
    getDataNetworkType = JavaMethod("()I")
    getAvailableStorageBytes = JavaMethod("()J")
    getBatteryPercentage = JavaMethod("()I")
    getNetworkCapabilities = JavaMethod("()Landroid/net/NetworkCapabilities;")
    getTimezoneUtcOffset = JavaMethod("()Ljava/time/Duration;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getOrientation = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")