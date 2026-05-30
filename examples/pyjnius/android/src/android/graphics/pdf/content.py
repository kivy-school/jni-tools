from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class PdfPageGotoLinkContent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/content/PdfPageGotoLinkContent"
    __javaconstructor__ = [("(Ljava/util/List;Landroid/graphics/pdf/content/PdfPageGotoLinkContent$Destination;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBounds = JavaMethod("()Ljava/util/List;")
    getDestination = JavaMethod("()Landroid/graphics/pdf/content/PdfPageGotoLinkContent$Destination;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Destination(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/content/PdfPageGotoLinkContent$Destination"
        __javaconstructor__ = [("(IFFF)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getPageNumber = JavaMethod("()I")
        getXCoordinate = JavaMethod("()F")
        getYCoordinate = JavaMethod("()F")
        getZoom = JavaMethod("()F")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class PdfPageTextContent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/content/PdfPageTextContent"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBounds = JavaMethod("()Ljava/util/List;")
    getText = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class PdfPageLinkContent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/content/PdfPageLinkContent"
    __javaconstructor__ = [("(Ljava/util/List;Landroid/net/Uri;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBounds = JavaMethod("()Ljava/util/List;")
    getUri = JavaMethod("()Landroid/net/Uri;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class PdfPageImageContent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/content/PdfPageImageContent"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getAltText = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")