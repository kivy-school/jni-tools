from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentProviderResult"]

class ContentProviderResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentProviderResult"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(I)V", False), ("(Landroid/os/Parcel;)V", False), ("(Landroid/os/Bundle;)V", False), ("(Landroid/net/Uri;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    count = JavaField("Ljava/lang/Integer;")
    exception = JavaField("Ljava/lang/Throwable;")
    extras = JavaField("Landroid/os/Bundle;")
    uri = JavaField("Landroid/net/Uri;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")