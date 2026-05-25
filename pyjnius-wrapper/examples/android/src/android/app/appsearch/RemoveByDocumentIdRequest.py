from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoveByDocumentIdRequest"]

class RemoveByDocumentIdRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/RemoveByDocumentIdRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getNamespace = JavaMethod("()Ljava/lang/String;")
    getIds = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/RemoveByDocumentIdRequest/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        addIds = JavaMultipleMethod([("([Ljava/lang/String;)Landroid/app/appsearch/RemoveByDocumentIdRequest$Builder;", False, True), ("(Ljava/util/Collection;)Landroid/app/appsearch/RemoveByDocumentIdRequest$Builder;", False, False)])
        build = JavaMethod("()Landroid/app/appsearch/RemoveByDocumentIdRequest;")