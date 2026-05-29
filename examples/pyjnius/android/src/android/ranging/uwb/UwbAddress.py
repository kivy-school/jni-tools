from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UwbAddress"]

class UwbAddress(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/uwb/UwbAddress"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTENDED_ADDRESS_BYTE_LENGTH = JavaStaticField("I")
    SHORT_ADDRESS_BYTE_LENGTH = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getAddressBytes = JavaMethod("()[B")
    createRandomShortAddress = JavaStaticMethod("()Landroid/ranging/uwb/UwbAddress;")
    fromBytes = JavaStaticMethod("([B)Landroid/ranging/uwb/UwbAddress;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")