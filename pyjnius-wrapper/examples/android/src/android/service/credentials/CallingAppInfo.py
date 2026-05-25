from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallingAppInfo"]

class CallingAppInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/CallingAppInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/content/pm/SigningInfo;)V", False), ("(Ljava/lang/String;Landroid/content/pm/SigningInfo;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getSigningInfo = JavaMethod("()Landroid/content/pm/SigningInfo;")
    getOrigin = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")