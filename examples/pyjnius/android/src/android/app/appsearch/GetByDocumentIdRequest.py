from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetByDocumentIdRequest"]

class GetByDocumentIdRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/GetByDocumentIdRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PROJECTION_SCHEMA_TYPE_WILDCARD = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getIds = JavaMethod("()Ljava/util/Set;")
    getProjectionPaths = JavaMethod("()Ljava/util/Map;")
    getProjections = JavaMethod("()Ljava/util/Map;")
    getNamespace = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/GetByDocumentIdRequest$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        addIds = JavaMultipleMethod([("(Ljava/util/Collection;)Landroid/app/appsearch/GetByDocumentIdRequest$Builder;", False, False), ("([Ljava/lang/String;)Landroid/app/appsearch/GetByDocumentIdRequest$Builder;", False, True)])
        addProjectionPaths = JavaMethod("(Ljava/lang/String;Ljava/util/Collection;)Landroid/app/appsearch/GetByDocumentIdRequest$Builder;")
        addProjection = JavaMethod("(Ljava/lang/String;Ljava/util/Collection;)Landroid/app/appsearch/GetByDocumentIdRequest$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/GetByDocumentIdRequest;")