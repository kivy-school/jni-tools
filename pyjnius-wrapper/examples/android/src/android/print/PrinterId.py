from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrinterId"]

class PrinterId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PrinterId"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLocalId = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")