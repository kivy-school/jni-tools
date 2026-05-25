from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObbInfo"]

class ObbInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/ObbInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    OBB_OVERLAY = JavaStaticField("I")
    filename = JavaField("Ljava/lang/String;")
    flags = JavaField("I")
    packageName = JavaField("Ljava/lang/String;")
    version = JavaField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")