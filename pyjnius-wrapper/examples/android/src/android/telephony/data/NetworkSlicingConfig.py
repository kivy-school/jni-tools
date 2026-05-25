from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkSlicingConfig"]

class NetworkSlicingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/data/NetworkSlicingConfig"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getUrspRules = JavaMethod("()Ljava/util/List;")
    getSliceInfo = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")