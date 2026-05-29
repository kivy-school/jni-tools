from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlobHandle"]

class BlobHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/blob/BlobHandle"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getExpiryTimeMillis = JavaMethod("()J")
    createWithSha256 = JavaStaticMethod("([BLjava/lang/CharSequence;JLjava/lang/String;)Landroid/app/blob/BlobHandle;")
    getSha256Digest = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getTag = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")