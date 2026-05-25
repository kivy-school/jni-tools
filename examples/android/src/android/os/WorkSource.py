from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WorkSource"]

class WorkSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/WorkSource"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/WorkSource;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    clear = JavaMethod("()V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    diff = JavaMethod("(Landroid/os/WorkSource;)Z")
    set = JavaMethod("(Landroid/os/WorkSource;)V")
    add = JavaMethod("(Landroid/os/WorkSource;)Z")
    remove = JavaMethod("(Landroid/os/WorkSource;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")