from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiSsidPolicy"]

class WifiSsidPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/WifiSsidPolicy"
    __javaconstructor__ = [("(ILjava/util/Set;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    WIFI_SSID_POLICY_TYPE_ALLOWLIST = JavaStaticField("I")
    WIFI_SSID_POLICY_TYPE_DENYLIST = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPolicyType = JavaMethod("()I")
    getSsids = JavaMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")