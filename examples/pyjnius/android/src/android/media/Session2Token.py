from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Session2Token"]

class Session2Token(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/Session2Token"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/ComponentName;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_SESSION = JavaStaticField("I")
    TYPE_SESSION_SERVICE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")
    getUid = JavaMethod("()I")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getServiceName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")