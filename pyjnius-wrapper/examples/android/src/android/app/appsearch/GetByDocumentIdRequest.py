from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetByDocumentIdRequest"]

class GetByDocumentIdRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/GetByDocumentIdRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PROJECTION_SCHEMA_TYPE_WILDCARD = JavaStaticField("Ljava/lang/String;")
    getNamespace = JavaMethod("()Ljava/lang/String;")
    getIds = JavaMethod("()Ljava/util/Set;")
    getProjections = JavaMethod("()Ljava/util/Map;")
    getProjectionPaths = JavaMethod("()Ljava/util/Map;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/GetByDocumentIdRequest/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        addIds = JavaMultipleMethod([("([Ljava/lang/String;)Landroid/app/appsearch/GetByDocumentIdRequest$Builder;", False, True), ("(Ljava/util/Collection;)Landroid/app/appsearch/GetByDocumentIdRequest$Builder;", False, False)])
        addProjection = JavaMethod("(Ljava/lang/String;Ljava/util/Collection;)Landroid/app/appsearch/GetByDocumentIdRequest$Builder;")
        addProjectionPaths = JavaMethod("(Ljava/lang/String;Ljava/util/Collection;)Landroid/app/appsearch/GetByDocumentIdRequest$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/GetByDocumentIdRequest;")