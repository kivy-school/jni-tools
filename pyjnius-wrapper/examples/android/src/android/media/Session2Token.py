from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Session2Token"]

class Session2Token(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/Session2Token"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/ComponentName;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_SESSION = JavaStaticField("I")
    TYPE_SESSION_SERVICE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getUid = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getServiceName = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")
    getExtras = JavaMethod("()Landroid/os/Bundle;")