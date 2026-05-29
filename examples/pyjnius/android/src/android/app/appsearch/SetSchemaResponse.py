from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SetSchemaResponse"]

class SetSchemaResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/SetSchemaResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDeletedTypes = JavaMethod("()Ljava/util/Set;")
    getMigratedTypes = JavaMethod("()Ljava/util/Set;")
    getIncompatibleTypes = JavaMethod("()Ljava/util/Set;")
    getMigrationFailures = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class MigrationFailure(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SetSchemaResponse$MigrationFailure"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/app/appsearch/AppSearchResult;)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getDocumentId = JavaMethod("()Ljava/lang/String;")
        getAppSearchResult = JavaMethod("()Landroid/app/appsearch/AppSearchResult;")
        toString = JavaMethod("()Ljava/lang/String;")
        getSchemaType = JavaMethod("()Ljava/lang/String;")
        getNamespace = JavaMethod("()Ljava/lang/String;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SetSchemaResponse$Builder"
        __javaconstructor__ = [("()V", False)]
        addDeletedType = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/SetSchemaResponse$Builder;")
        addDeletedTypes = JavaMethod("(Ljava/util/Collection;)Landroid/app/appsearch/SetSchemaResponse$Builder;")
        addIncompatibleType = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/SetSchemaResponse$Builder;")
        addIncompatibleTypes = JavaMethod("(Ljava/util/Collection;)Landroid/app/appsearch/SetSchemaResponse$Builder;")
        addMigratedType = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/SetSchemaResponse$Builder;")
        addMigratedTypes = JavaMethod("(Ljava/util/Collection;)Landroid/app/appsearch/SetSchemaResponse$Builder;")
        addMigrationFailure = JavaMethod("(Landroid/app/appsearch/SetSchemaResponse$MigrationFailure;)Landroid/app/appsearch/SetSchemaResponse$Builder;")
        addMigrationFailures = JavaMethod("(Ljava/util/Collection;)Landroid/app/appsearch/SetSchemaResponse$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/SetSchemaResponse;")