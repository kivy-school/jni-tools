from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URLSpan"]

class URLSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/URLSpan"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Landroid/os/Parcel;)V", False)]
    getSpanTypeId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getURL = JavaMethod("()Ljava/lang/String;")
    onClick = JavaMethod("(Landroid/view/View;)V")
    toString = JavaMethod("()Ljava/lang/String;")