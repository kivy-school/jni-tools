from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObbInfo"]

class ObbInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/ObbInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    OBB_OVERLAY = JavaStaticField("I")
    filename = JavaField("Ljava/lang/String;")
    flags = JavaField("I")
    packageName = JavaField("Ljava/lang/String;")
    version = JavaField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")