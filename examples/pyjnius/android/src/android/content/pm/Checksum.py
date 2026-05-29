from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Checksum"]

class Checksum(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/Checksum"
    __javaconstructor__ = [("(I[B)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_PARTIAL_MERKLE_ROOT_1M_SHA256 = JavaStaticField("I")
    TYPE_PARTIAL_MERKLE_ROOT_1M_SHA512 = JavaStaticField("I")
    TYPE_WHOLE_MD5 = JavaStaticField("I")
    TYPE_WHOLE_MERKLE_ROOT_4K_SHA256 = JavaStaticField("I")
    TYPE_WHOLE_SHA1 = JavaStaticField("I")
    TYPE_WHOLE_SHA256 = JavaStaticField("I")
    TYPE_WHOLE_SHA512 = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getValue = JavaMethod("()[B")
    getType = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")