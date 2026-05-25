from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppLinkInfo"]

class AppLinkInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/interactive/AppLinkInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getComponentName = JavaMethod("()Landroid/content/ComponentName;")
    getUri = JavaMethod("()Landroid/net/Uri;")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")