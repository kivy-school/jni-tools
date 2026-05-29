from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoveByDocumentIdRequest"]

class RemoveByDocumentIdRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/RemoveByDocumentIdRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getIds = JavaMethod("()Ljava/util/Set;")
    getNamespace = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/RemoveByDocumentIdRequest$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        addIds = JavaMultipleMethod([("(Ljava/util/Collection;)Landroid/app/appsearch/RemoveByDocumentIdRequest$Builder;", False, False), ("([Ljava/lang/String;)Landroid/app/appsearch/RemoveByDocumentIdRequest$Builder;", False, True)])
        build = JavaMethod("()Landroid/app/appsearch/RemoveByDocumentIdRequest;")