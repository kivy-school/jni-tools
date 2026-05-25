from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PdfPageLinkContent"]

class PdfPageLinkContent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/content/PdfPageLinkContent"
    __javaconstructor__ = [("(Ljava/util/List;Landroid/net/Uri;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getBounds = JavaMethod("()Ljava/util/List;")
    getUri = JavaMethod("()Landroid/net/Uri;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")