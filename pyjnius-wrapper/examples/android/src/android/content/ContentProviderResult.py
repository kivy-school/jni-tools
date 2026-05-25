from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentProviderResult"]

class ContentProviderResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentProviderResult"
    __javaconstructor__ = [("(Landroid/net/Uri;)V", False), ("(I)V", False), ("(Landroid/os/Bundle;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    count = JavaField("Ljava/lang/Integer;")
    exception = JavaField("Ljava/lang/Throwable;")
    extras = JavaField("Landroid/os/Bundle;")
    uri = JavaField("Landroid/net/Uri;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")