from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ModuleInfo"]

class ModuleInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ModuleInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getName = JavaMethod("()Ljava/lang/CharSequence;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    isHidden = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")