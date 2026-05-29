from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParcelUuid"]

class ParcelUuid(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ParcelUuid"
    __javaconstructor__ = [("(Ljava/util/UUID;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getUuid = JavaMethod("()Ljava/util/UUID;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Landroid/os/ParcelUuid;")