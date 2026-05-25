from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EuiccInfo"]

class EuiccInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/euicc/EuiccInfo"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getOsVersion = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")