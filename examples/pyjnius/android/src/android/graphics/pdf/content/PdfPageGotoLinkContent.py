from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PdfPageGotoLinkContent"]

class PdfPageGotoLinkContent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/content/PdfPageGotoLinkContent"
    __javaconstructor__ = [("(Ljava/util/List;Landroid/graphics/pdf/content/PdfPageGotoLinkContent$Destination;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDestination = JavaMethod("()Landroid/graphics/pdf/content/PdfPageGotoLinkContent$Destination;")
    getBounds = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Destination(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/content/PdfPageGotoLinkContent$Destination"
        __javaconstructor__ = [("(IFFF)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getPageNumber = JavaMethod("()I")
        getYCoordinate = JavaMethod("()F")
        getXCoordinate = JavaMethod("()F")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getZoom = JavaMethod("()F")