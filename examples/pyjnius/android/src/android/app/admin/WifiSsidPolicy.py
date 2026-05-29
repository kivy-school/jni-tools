from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiSsidPolicy"]

class WifiSsidPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/WifiSsidPolicy"
    __javaconstructor__ = [("(ILjava/util/Set;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    WIFI_SSID_POLICY_TYPE_ALLOWLIST = JavaStaticField("I")
    WIFI_SSID_POLICY_TYPE_DENYLIST = JavaStaticField("I")
    getSsids = JavaMethod("()Ljava/util/Set;")
    getPolicyType = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")