from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PdfPageImageContent"]

class PdfPageImageContent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/content/PdfPageImageContent"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getAltText = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")