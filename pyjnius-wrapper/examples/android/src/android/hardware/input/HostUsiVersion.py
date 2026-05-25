from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HostUsiVersion"]

class HostUsiVersion(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/input/HostUsiVersion"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getMajorVersion = JavaMethod("()I")
    getMinorVersion = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")