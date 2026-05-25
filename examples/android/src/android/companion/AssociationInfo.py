from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AssociationInfo"]

class AssociationInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/AssociationInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getId = JavaMethod("()I")
    getDeviceMacAddress = JavaMethod("()Landroid/net/MacAddress;")
    getDisplayName = JavaMethod("()Ljava/lang/CharSequence;")
    getDeviceProfile = JavaMethod("()Ljava/lang/String;")
    getAssociatedDevice = JavaMethod("()Landroid/companion/AssociatedDevice;")
    isSelfManaged = JavaMethod("()Z")
    getSystemDataSyncFlags = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")