from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintDocumentInfo"]

class PrintDocumentInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PrintDocumentInfo"
    CONTENT_TYPE_DOCUMENT = JavaStaticField("I")
    CONTENT_TYPE_PHOTO = JavaStaticField("I")
    CONTENT_TYPE_UNKNOWN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PAGE_COUNT_UNKNOWN = JavaStaticField("I")
    getName = JavaMethod("()Ljava/lang/String;")
    getPageCount = JavaMethod("()I")
    getContentType = JavaMethod("()I")
    getDataSize = JavaMethod("()J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/print/PrintDocumentInfo/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setPageCount = JavaMethod("(I)Landroid/print/PrintDocumentInfo$Builder;")
        setContentType = JavaMethod("(I)Landroid/print/PrintDocumentInfo$Builder;")
        build = JavaMethod("()Landroid/print/PrintDocumentInfo;")