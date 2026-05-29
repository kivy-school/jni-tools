from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangingCapabilities"]

class RangingCapabilities(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/RangingCapabilities"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DISABLED_REGULATORY = JavaStaticField("I")
    DISABLED_USER = JavaStaticField("I")
    DISABLED_USER_RESTRICTIONS = JavaStaticField("I")
    ENABLED = JavaStaticField("I")
    NOT_SUPPORTED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getCsCapabilities = JavaMethod("()Landroid/ranging/ble/cs/BleCsRangingCapabilities;")
    getRttRangingCapabilities = JavaMethod("()Landroid/ranging/wifi/rtt/RttRangingCapabilities;")
    getTechnologyAvailability = JavaMethod("()Ljava/util/Map;")
    getUwbCapabilities = JavaMethod("()Landroid/ranging/uwb/UwbRangingCapabilities;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")