from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PdfPageGotoLinkContent"]

class PdfPageGotoLinkContent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/content/PdfPageGotoLinkContent"
    __javaconstructor__ = [("(Ljava/util/List;Landroid/graphics/pdf/content/PdfPageGotoLinkContent$Destination;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getBounds = JavaMethod("()Ljava/util/List;")
    getDestination = JavaMethod("()Landroid/graphics/pdf/content/PdfPageGotoLinkContent$Destination;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Destination(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/content/PdfPageGotoLinkContent/Destination"
        __javaconstructor__ = [("(IFFF)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getPageNumber = JavaMethod("()I")
        getXCoordinate = JavaMethod("()F")
        getYCoordinate = JavaMethod("()F")
        getZoom = JavaMethod("()F")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")