from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SystemUpdateInfo"]

class SystemUpdateInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/SystemUpdateInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SECURITY_PATCH_STATE_FALSE = JavaStaticField("I")
    SECURITY_PATCH_STATE_TRUE = JavaStaticField("I")
    SECURITY_PATCH_STATE_UNKNOWN = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSecurityPatchState = JavaMethod("()I")
    getReceivedTime = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")