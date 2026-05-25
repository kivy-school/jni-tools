from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VersionedPackage"]

class VersionedPackage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/VersionedPackage"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False), ("(Ljava/lang/String;J)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getVersionCode = JavaMethod("()I")
    getLongVersionCode = JavaMethod("()J")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")