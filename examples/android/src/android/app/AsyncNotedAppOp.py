from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsyncNotedAppOp"]

class AsyncNotedAppOp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/AsyncNotedAppOp"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getOp = JavaMethod("()Ljava/lang/String;")
    getNotingUid = JavaMethod("()I")
    getAttributionTag = JavaMethod("()Ljava/lang/String;")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getTime = JavaMethod("()J")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")