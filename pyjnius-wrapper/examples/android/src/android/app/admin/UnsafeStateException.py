from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnsafeStateException"]

class UnsafeStateException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/UnsafeStateException"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getReasons = JavaMethod("()Ljava/util/List;")
    getMessage = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")