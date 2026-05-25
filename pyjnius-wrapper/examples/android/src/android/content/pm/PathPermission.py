from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathPermission"]

class PathPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/PathPermission"
    __javaconstructor__ = [("(Ljava/lang/String;ILjava/lang/String;Ljava/lang/String;)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getReadPermission = JavaMethod("()Ljava/lang/String;")
    getWritePermission = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")