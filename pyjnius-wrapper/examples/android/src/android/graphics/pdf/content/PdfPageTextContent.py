from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PdfPageTextContent"]

class PdfPageTextContent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/content/PdfPageTextContent"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getText = JavaMethod("()Ljava/lang/String;")
    getBounds = JavaMethod("()Ljava/util/List;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")