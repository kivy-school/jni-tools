from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlobHandle"]

class BlobHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/blob/BlobHandle"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    createWithSha256 = JavaStaticMethod("([BLjava/lang/CharSequence;JLjava/lang/String;)Landroid/app/blob/BlobHandle;")
    getSha256Digest = JavaMethod("()[B")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getExpiryTimeMillis = JavaMethod("()J")
    getTag = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")