from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetSchemaResponse"]

class GetSchemaResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/GetSchemaResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPubliclyVisibleSchemas = JavaMethod("()Ljava/util/Map;")
    getRequiredPermissionsForSchemaTypeVisibility = JavaMethod("()Ljava/util/Map;")
    getSchemaTypesNotDisplayedBySystem = JavaMethod("()Ljava/util/Set;")
    getSchemaTypesVisibleToConfigs = JavaMethod("()Ljava/util/Map;")
    getSchemaTypesVisibleToPackages = JavaMethod("()Ljava/util/Map;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSchemas = JavaMethod("()Ljava/util/Set;")
    getVersion = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/GetSchemaResponse$Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/app/appsearch/GetSchemaResponse;)V", False)]
        setVersion = JavaMethod("(I)Landroid/app/appsearch/GetSchemaResponse$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/GetSchemaResponse;")
        addSchema = JavaMethod("(Landroid/app/appsearch/AppSearchSchema;)Landroid/app/appsearch/GetSchemaResponse$Builder;")
        clearSchemas = JavaMethod("()Landroid/app/appsearch/GetSchemaResponse$Builder;")
        addSchemaTypeNotDisplayedBySystem = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GetSchemaResponse$Builder;")
        clearPubliclyVisibleSchema = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GetSchemaResponse$Builder;")
        clearRequiredPermissionsForSchemaTypeVisibility = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GetSchemaResponse$Builder;")
        clearSchemaTypeNotDisplayedBySystem = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GetSchemaResponse$Builder;")
        clearSchemaTypeVisibleToConfigs = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GetSchemaResponse$Builder;")
        clearSchemaTypeVisibleToPackages = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/GetSchemaResponse$Builder;")
        setPubliclyVisibleSchema = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/PackageIdentifier;)Landroid/app/appsearch/GetSchemaResponse$Builder;")
        setRequiredPermissionsForSchemaTypeVisibility = JavaMethod("(Ljava/lang/String;Ljava/util/Set;)Landroid/app/appsearch/GetSchemaResponse$Builder;")
        setSchemaTypeVisibleToConfigs = JavaMethod("(Ljava/lang/String;Ljava/util/Set;)Landroid/app/appsearch/GetSchemaResponse$Builder;")
        setSchemaTypeVisibleToPackages = JavaMethod("(Ljava/lang/String;Ljava/util/Set;)Landroid/app/appsearch/GetSchemaResponse$Builder;")