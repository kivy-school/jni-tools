from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintJobId"]

class PrintJobId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PrintJobId"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")