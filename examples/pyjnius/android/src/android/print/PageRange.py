from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PageRange"]

class PageRange(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PageRange"
    __javaconstructor__ = [("(II)V", False)]
    ALL_PAGES = JavaStaticField("Landroid/print/PageRange;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getStart = JavaMethod("()I")
    getEnd = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")