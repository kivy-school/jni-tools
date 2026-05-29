from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathPermission"]

class PathPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/PathPermission"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("(Ljava/lang/String;ILjava/lang/String;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PATTERN_ADVANCED_GLOB = JavaStaticField("I")
    PATTERN_LITERAL = JavaStaticField("I")
    PATTERN_PREFIX = JavaStaticField("I")
    PATTERN_SIMPLE_GLOB = JavaStaticField("I")
    PATTERN_SUFFIX = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getReadPermission = JavaMethod("()Ljava/lang/String;")
    getWritePermission = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")