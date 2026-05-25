from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParcelUuid"]

class ParcelUuid(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ParcelUuid"
    __javaconstructor__ = [("(Ljava/util/UUID;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Landroid/os/ParcelUuid;")
    getUuid = JavaMethod("()Ljava/util/UUID;")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")