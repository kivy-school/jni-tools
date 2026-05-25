from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SystemUpdateInfo"]

class SystemUpdateInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/SystemUpdateInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SECURITY_PATCH_STATE_FALSE = JavaStaticField("I")
    SECURITY_PATCH_STATE_TRUE = JavaStaticField("I")
    SECURITY_PATCH_STATE_UNKNOWN = JavaStaticField("I")
    getReceivedTime = JavaMethod("()J")
    getSecurityPatchState = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")