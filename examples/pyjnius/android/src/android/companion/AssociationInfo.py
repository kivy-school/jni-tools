from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AssociationInfo"]

class AssociationInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/AssociationInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isSelfManaged = JavaMethod("()Z")
    getDeviceProfile = JavaMethod("()Ljava/lang/String;")
    getAssociatedDevice = JavaMethod("()Landroid/companion/AssociatedDevice;")
    getDeviceMacAddress = JavaMethod("()Landroid/net/MacAddress;")
    getSystemDataSyncFlags = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()I")
    getDeviceId = JavaMethod("()Landroid/companion/DeviceId;")
    getDisplayName = JavaMethod("()Ljava/lang/CharSequence;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")