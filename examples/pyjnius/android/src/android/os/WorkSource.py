from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WorkSource"]

class WorkSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/WorkSource"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/WorkSource;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    remove = JavaMethod("(Landroid/os/WorkSource;)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clear = JavaMethod("()V")
    add = JavaMethod("(Landroid/os/WorkSource;)Z")
    set = JavaMethod("(Landroid/os/WorkSource;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    diff = JavaMethod("(Landroid/os/WorkSource;)Z")